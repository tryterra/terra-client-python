from terra.base_client import Terra


def test_hash_sign():
    assert Terra(api_key="api", dev_id="dev", secret="secret").check_terra_signature(
        "b", "t=10,v1=ad2da523c6d08e6ba4d8c36d86d5ca1f31f26992aabde11659556ced1d96509b"
    )


def test_hash_sign_error():
    assert not Terra(api_key="api", dev_id="dev", secret="secret").check_terra_signature("b", "t=10,v1=azert")


def test_webhooks_false_sig():
    assert Terra(api_key="api", dev_id="dev", secret="secret").handle_webhook("b", "t=10,v1=3") is None
