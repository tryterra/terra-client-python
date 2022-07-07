import json

import mock

from terra.api import api_responses
from terra.base_client import Terra
from terra.models.base_model import TerraDataModel
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

    filled: api_responses.DataReturned = api_responses.TerraWebhookResponse(
        dc, User(None, "lmao", None, None)
    ).parsed_response

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

    filled: api_responses.ProvidersResponse = api_responses.TerraWebhookResponse(
        dc, User(None, "lmao", None, None), "providers"
    ).parsed_response

    for p in filled.providers:
        assert p in dc["providers"]
