import hashlib
import hmac
import time
from typing import List, Optional, Tuple


class WebhookVerificationError(Exception):
    """Custom exception for webhook verification failures"""
    pass


def verify_terra_webhook_signature(
    payload: str,
    signature_header: str,
    signing_secret: str,
    tolerance: int = 300
) -> bool:
    """
    Verify Terra webhook signature using HMAC-SHA256.

    Args:
        payload: The raw JSON payload from the request body
        signature_header: The 'terra-signature' header value
        signing_secret: The webhook endpoint's signing secret
        tolerance: Maximum age of the webhook in seconds (default: 5 minutes)

    Returns:
        bool: True if signature is valid and within tolerance

    Raises:
        WebhookVerificationError: If verification fails
    """
    if not payload or not signature_header or not signing_secret:
        raise WebhookVerificationError("Missing required parameters")

    # Step 1: Extract timestamp and signatures from header
    timestamp, signatures = _extract_timestamp_and_signatures(signature_header)

    if not timestamp:
        raise WebhookVerificationError("No timestamp found in signature header")

    if not signatures:
        raise WebhookVerificationError("No v1 signatures found in signature header")

    # Step 2: Prepare the signed payload string
    signed_payload = f"{timestamp}.{payload}"

    # Step 3: Determine the expected signature
    expected_signature = _compute_signature(signed_payload, signing_secret)

    # Step 4: Compare signatures and check timestamp tolerance
    _verify_signatures(signatures, expected_signature)
    _verify_timestamp(timestamp, tolerance)

    return True


def _extract_timestamp_and_signatures(signature_header: str) -> Tuple[Optional[str], List[str]]:
    """
    Extract timestamp and v1 signatures from the terra-signature header.

    Args:
        signature_header: The terra-signature header value

    Returns:
        tuple: (timestamp, list of v1 signatures)
    """
    timestamp = None
    signatures = []

    # Split by comma to get individual elements
    elements = signature_header.split(',')

    for element in elements:
        element = element.strip()
        if '=' not in element:
            continue

        prefix, value = element.split('=', 1)
        prefix = prefix.strip()
        value = value.strip()

        if prefix == 't':
            timestamp = value
        elif prefix == 'v1':  # Only accept v1 signatures to prevent downgrade attacks
            signatures.append(value)

    return timestamp, signatures


def _compute_signature(signed_payload: str, signing_secret: str) -> str:
    """
    Compute HMAC-SHA256 signature for the signed payload.

    Args:
        signed_payload: The concatenated timestamp.payload string
        signing_secret: The webhook signing secret

    Returns:
        str: Hexadecimal HMAC-SHA256 signature
    """
    return hmac.new(
        signing_secret.encode('utf-8'),
        signed_payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()


def _verify_signatures(received_signatures: List[str], expected_signature: str) -> None:
    """
    Verify that at least one received signature matches the expected signature.
    Uses constant-time comparison to prevent timing attacks.

    Args:
        received_signatures: List of signatures from the header
        expected_signature: The computed expected signature

    Raises:
        WebhookVerificationError: If no signatures match
    """
    for signature in received_signatures:
        if hmac.compare_digest(signature, expected_signature):
            return  # Valid signature found

    raise WebhookVerificationError("No matching signature found")


def _verify_timestamp(timestamp_str: str, tolerance: int) -> None:
    """
    Verify that the timestamp is within the acceptable tolerance.

    Args:
        timestamp_str: Timestamp as string from the header
        tolerance: Maximum age in seconds

    Raises:
        WebhookVerificationError: If timestamp is invalid or too old
    """
    try:
        webhook_timestamp = int(timestamp_str)
    except ValueError:
        raise WebhookVerificationError("Invalid timestamp format")

    current_timestamp = int(time.time())
    age = current_timestamp - webhook_timestamp

    if age > tolerance:
        raise WebhookVerificationError(
            f"Webhook timestamp too old: {age}s > {tolerance}s tolerance"
        )

    # Also check for timestamps in the future (clock skew protection)
    if age < -tolerance:
        raise WebhookVerificationError(
            f"Webhook timestamp too far in future: {abs(age)}s > {tolerance}s tolerance"
        )
