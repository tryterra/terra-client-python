import pytest

from terra import exceptions
from terra import models
from terra.api import api_responses
from terra.models.user import User


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


def test_response_no_body():
    with pytest.raises(exceptions.NoBodyException):
        api_responses._parse_api_body(None, None, None)


def test_filter():
    # Bad test - what are you asserting here? there is no comparison
    assert models.v2.activity.Activity().filter_data("heart")


def test_get_attr():
    # Bad test - you want to check that it returns *all* the correct attrs not just a single one
    assert "device_data" in models.v2.activity.Activity().keys()
