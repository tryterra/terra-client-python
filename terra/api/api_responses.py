#  Copyright 2022 Terra Enabling Developers Limited
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from cgitb import Hook
import dataclasses
from email.policy import default
import json.decoder
import typing

import requests

from terra import models
from terra.models import base_model
from terra.models import user as user_



class TerraParsedApiResponse(base_model.TerraDataModel):
    pass


def _parse_api_body(
    dtype: str, body: dict, user: models.user.User
) -> TerraParsedApiResponse:
    user = models.user.User.from_dict(body["user"]) if body.get("user") else user

    if dtype in USER_DATATYPES:
        return DataReturned(
            user=user,
            data=[MODEL_MAPPING[dtype].from_dict(item) for item in body["data"]]
            if body.get("data") or body.get("data")==[]
            else [MODEL_MAPPING[dtype].from_dict(body["athlete"])],
            type=dtype
        )
    elif dtype in DTYPE_TO_RESPONSE.keys():
        print("here")
        return DTYPE_TO_RESPONSE[dtype]().from_dict(body, True)




class TerraApiResponse(TerraParsedApiResponse):
    def __init__(self, resp: requests.Response, user=None, dtype=None):
        self.response_code = resp.status_code
        self.raw_body = resp.content.decode(resp.encoding)
        self.json = None
        self.dtype = dtype
        try:
            body = resp.json()
            self.json = body
            self.dtype = body.get("type", dtype)
            self.parsed_response = _parse_api_body(self.dtype, body, user)

        except json.decoder.JSONDecodeError:
            resp.raise_for_status()

class TerraWebhookResponse(TerraParsedApiResponse):
    def __init__(self, resp,user=None, dtype=None):
        self.dtype = dtype
        body = resp
        self.json = body
        self.dtype = body.get("type", dtype)
        
        self.parsed_response = _parse_api_body(self.dtype, body, user)


@dataclasses.dataclass
class WidgetSession(TerraParsedApiResponse):
    expires_in : int = dataclasses.field(default=900)
    status: str = dataclasses.field(default=None)
    session_id: str = dataclasses.field(default=None)
    url: str = dataclasses.field(default=None)


@dataclasses.dataclass
class UserInfo(TerraParsedApiResponse):
    status: str = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)
    is_authenticated: bool = dataclasses.field(default=True)


@dataclasses.dataclass
class UserDeauthResp(TerraParsedApiResponse):
    status: str = dataclasses.field(default="success")

@dataclasses.dataclass
class HookResponse(TerraParsedApiResponse):
    status: str = dataclasses.field(default="success")
    type: str = dataclasses.field(default=None)
    user: user_.User = dataclasses.field(default=None)


@dataclasses.dataclass
class SubscribedUsers(TerraParsedApiResponse):
    users: typing.Optional[typing.List[models.user.User]] = dataclasses.field(
        default_factory=list
    )


@dataclasses.dataclass
class UserAuthUrl(TerraParsedApiResponse):
    status: str = dataclasses.field(default=None)
    user_id: str = dataclasses.field(default=None)
    auth_url: str = dataclasses.field(default=None)


@dataclasses.dataclass
class RequestProcessing(TerraParsedApiResponse):
    status: str = dataclasses.field(default="Request is processing, try again later")
    auth_url: str = dataclasses.field(default=None)
    retry_after_seconds: int = dataclasses.field(default=180)
    type: str = dataclasses.field(default="processing")


@dataclasses.dataclass
class NoDataReturned(TerraParsedApiResponse):
    user: user_.User = dataclasses.field(default=None)
    status: str = dataclasses.field(default="not_available")
    message: str = dataclasses.field(
        default="Data type requested not available from provider"
    )


@dataclasses.dataclass
class DataReturned(TerraParsedApiResponse):
    user: user_.User = dataclasses.field(default=None)
    type: typing.Optional[str] = dataclasses.field(default=None)
    data: typing.List[TerraParsedApiResponse] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class NutritionDeletedData(TerraParsedApiResponse):
    type: typing.Optional[str] = dataclasses.field(default=None)
    processed_logs: typing.List[dict] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class RequestProcessing(TerraParsedApiResponse):
    retry_after_seconds: float = dataclasses.field(default=180)
    status: str = dataclasses.field(default="Request is processing, try again later")
    type: str = dataclasses.field(default="processing")


@dataclasses.dataclass
class DataSentToWebhook(TerraParsedApiResponse):
    reference: str = dataclasses.field(default=None)
    message: str = dataclasses.field(default="Data sent to webhook")
    type: str = dataclasses.field(default="sent_to_webhook")


@dataclasses.dataclass
class UserAuthenticated(TerraParsedApiResponse):
    status: typing.Optional[str] = dataclasses.field(default=None)
    widget_session_id: typing.Optional[str] = dataclasses.field(default=None)
    reference_id: typing.Optional[str] = dataclasses.field(default=None)
    message: str = dataclasses.field(default="User has successfully authenticated")
    type: str = dataclasses.field(default="auth")


@dataclasses.dataclass
class AuthenticationFailed(TerraParsedApiResponse):
    status: str = dataclasses.field(default="error")
    widget_session_id: typing.Optional[str] = dataclasses.field(default=None)
    reference_id: typing.Optional[str] = dataclasses.field(default=None)
    message: str = dataclasses.field(
        default="User failed to authenticate and has been deleted"
    )
    type: str = dataclasses.field(default="auth")
    reason: str = dataclasses.field(default="auth_cancelled")


@dataclasses.dataclass
class ConnectionDegraded(TerraParsedApiResponse):
    status: str = dataclasses.field(default="warning")
    message: str = dataclasses.field(default="User connection degraded")
    type: str = dataclasses.field(default="connection_error")

@dataclasses.dataclass
class ProvidersResponse(TerraParsedApiResponse):
    status: str = dataclasses.field(default="warning")
    providers: typing.Optional[typing.List[str]] = dataclasses.field(default=None)




__all__ = [
    "NoDataReturned",
    "DataReturned",
    "RequestProcessing",
    "DataSentToWebhook",
    "UserAuthenticated",
    "AuthenticationFailed",
    "ConnectionDegraded",
]

USER_DATATYPES = ["activity", "athlete", "body", "daily", "menstruation", "sleep"]
MODEL_MAPPING = {
    "activity": models.v2022_03_16.activity.Activity,
    "body": models.v2022_03_16.body.Body,
    "daily": models.v2022_03_16.daily.Daily,
    "sleep": models.v2022_03_16.sleep.Sleep,
    "menstruation": models.v2022_03_16.menstruation.Menstruation,
    "athlete": models.v2022_03_16.athlete.Athlete,
}


DTYPE_TO_RESPONSE = {
    "widget_session": WidgetSession,
    "auth_url": UserAuthUrl,
    "user_info": UserInfo,
    "subscriptions": SubscribedUsers,
    "providers" : ProvidersResponse,

}

HOOK_TYPES = ["auth", "user_reauth", "access_revoked", "deauth", "google_no_datasource", "connexion_error"]

HOOK_RESPONSE = {
    "auth":HookResponse, 
    "user_reauth":HookResponse,
    "access_revoked":HookResponse,
    "deauth":HookResponse, 
    "google_no_datasource":HookResponse, 
    "connexion_error":HookResponse
}
