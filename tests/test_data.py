# TODO - ------------------------------------------------------------
# TODO - There is no file in the repository called 'data.py', what
# TODO - file is this testing? You should have separate test files
# TODO - for each project file you are testing, and the structure
# TODO - should be the same as the project structure. I.e. if you are
# TODO - testing 'terra/api/api_responses.py', the file would be
# TODO - 'tests/api/test_api_responses.py'
# TODO - ------------------------------------------------------------
import datetime

import pytest

from terra import exceptions
from terra import models
from terra.api import api_responses
from terra.base_client import Terra
from terra.models.user import User


def test_parsing_user():
    filled = User().from_dict({"user_id": "lmao"})
    assert filled.user_id == "lmao"


def test_parsing_data():

    dc = {
        "status": "success",
        "user": {"user_id": "lmao", "provider": "GARMIN", "last_webhook_update": None},
        "data": [],
        "type": "body",
    }

    filled = api_responses.TerraWebhookResponse(dc, User(None, "lmao", None, None)).parsed_response
    assert isinstance(filled, api_responses.DataReturned)
    assert filled.type == "body"


def test_parsing_integrations():
    dc = {
        "status": "success",
        "providers": [
            "FITBIT",
            "OURA",
            "TRAININGPEAKS",
            "WITHINGS",
            "SUUNTO",
            "PELOTON",
            "ZWIFT",
            "GARMIN",
            "EIGHT",
            "WAHOO",
            "GOOGLE",
            "POLAR",
            "WEAROS",
            "FREESTYLELIBRE",
            "TEMPO",
            "IFIT",
            "CONCEPT2",
            "FATSECRET",
            "CRONOMETER",
            "MYFITNESSPAL",
            "NUTRACHECK",
            "UNDERARMOUR",
            "OMRON",
            "RENPHO",
            "DEXCOM",
        ],
    }

    filled = api_responses.TerraWebhookResponse(dc, User(None, "lmao", None, None), "providers").parsed_response
    assert isinstance(filled, api_responses.ProvidersResponse)
    for p in filled.providers:
        assert p in dc["providers"]


def test_hash_sign():
    assert Terra(api_key="api", dev_id="dev", secret="secret").check_terra_signature(
        "b", "t=10,v1=ad2da523c6d08e6ba4d8c36d86d5ca1f31f26992aabde11659556ced1d96509b"
    )


def test_hash_sign_error():
    assert not Terra(api_key="api", dev_id="dev", secret="secret").check_terra_signature("b", "t=10,v1=azert")


def test_webhooks_false_sig():
    assert Terra(api_key="api", dev_id="dev", secret="secret").handle_webhook("b", "t=10,v1=3") is None


def test_no_client_user():
    user = User()
    with pytest.raises(exceptions.NoClientAvailable):
        user.get_activity(datetime.datetime.today())


def test_response_no_body():
    with pytest.raises(exceptions.NoBodyException):
        api_responses._parse_api_body(None, None, None)


def test_filter():
    # Bad test - what are you asserting here? there is no comparison
    assert models.v2.activity.Activity().filter_data("heart")


def test_get_attr():
    # Bad test - you want to check that it returns *all* the correct attrs not just a single one
    assert "device_data" in models.v2.activity.Activity().keys()
