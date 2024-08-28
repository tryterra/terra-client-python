import requests

from terra.base_client import Terra


def test_hash_sign():
    assert Terra(api_key="api", dev_id="dev", secret="secret").check_terra_signature(
        "b", "t=10,v1=ad2da523c6d08e6ba4d8c36d86d5ca1f31f26992aabde11659556ced1d96509b"
    )


def test_hash_sign_error():
    assert not Terra(api_key="api", dev_id="dev", secret="secret").check_terra_signature("b", "t=10,v1=azert")


def test_webhooks_false_sig():
    assert Terra(api_key="api", dev_id="dev", secret="secret").handle_webhook("b", "t=10,v1=3") is None


def test_passing_requests_session():
    # No session explicitly passed
    client_default = Terra(api_key="api", dev_id="dev", secret="secret")
    # One should be automatically added to the client
    assert isinstance(client_default._session, requests.Session)

    # Passing None should do the same as the default
    client_none = Terra(api_key="api", dev_id="dev", secret="secret", session=None)
    # One should be automatically added to the client
    isinstance(client_none._session, requests.Session)

    # The two sessions should be different objects
    assert client_default._session != client_none._session

    # Passing a session should use that session
    session = requests.Session()
    client_session = Terra(api_key="api", dev_id="dev", secret="secret", session=session)
    assert client_session._session == session
