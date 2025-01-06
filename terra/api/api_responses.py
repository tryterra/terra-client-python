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
from __future__ import annotations

__all__ = [
    "AccessRevokedHookResponse",
    "AuthHookResponse",
    "AuthenticationFailed",
    "ConnectionDegraded",
    "ConnectionErrorHookResponse",
    "DataReturned",
    "GenericMessage",
    "GoogleNoDataSourceHookResponse",
    "HookResponse",
    "NoDataReturned",
    "ProvidersResponse",
    "RequestCompletedHookResponse",
    "RequestProcessingHookResponse",
    "SentToWebhook",
    "SubscribedUsers",
    "TerraApiResponse",
    "TerraParsedApiResponse",
    "TerraWebhookResponse",
    "UserAuthUrl",
    "UserDeauthHookResponse",
    "UserDeauthResp",
    "UserInfo",
    "UserReauthHookResponse",
    "WidgetSession",
]

import dataclasses
import json.decoder
import typing

import requests

from terra import exceptions
from terra import models
from terra.models import base_model
from terra.models import user as user_

if typing.TYPE_CHECKING:
    from terra.base_client import Terra


# TODO - should use a mixin/trait here instead of a redundant subclass probably
class TerraParsedApiResponse(base_model.TerraDataModel):
    pass


def _parse_api_body(
    dtype: typing.Optional[str],
    body: typing.Optional[typing.Dict[str, typing.Any]],
    user: typing.Optional[models.user.User],
) -> TerraParsedApiResponse:
    if not body:
        raise exceptions.NoBodyException

    a_user = user
    if "user" in body:
        a_user = models.user.User.from_dict(body["user"])

    if ("status" in body) and (body["status"] in STATUS.keys()) and (body["status"] != "warning"):  # noqa: SIM118
        response = STATUS[body["status"]]().from_dict(body)

    elif dtype in USER_DATATYPES:
        if not dtype:
            raise exceptions.NoDtypeException

        return DataReturned(
            user=a_user,
            data=(  # type: ignore
                [MODEL_MAPPING[dtype]().from_dict(item) for item in body["data"]]
                if body.get("data") or body.get("data") == []
                else []
            ),
            type=dtype,
        )
    elif dtype in DTYPE_TO_RESPONSE.keys():  # noqa: SIM118
        if not dtype:
            raise exceptions.NoDtypeException

        response = DTYPE_TO_RESPONSE[dtype]().from_dict(body)

    elif dtype in HOOK_RESPONSE.keys():  # noqa: SIM118
        if not dtype:
            raise exceptions.NoDtypeException
        response = HOOK_RESPONSE[dtype]().from_dict(body)

    else:
        response = GenericMessage().from_dict(body)

    try:
        setattr(response, "user", a_user)

    finally:
        try:
            if "old_user" in body:
                setattr(
                    response,
                    "old_user",
                    models.user.User.from_dict(body["old_user"]),
                )
            if "new_user" in body:
                setattr(
                    response,
                    "new_user",
                    models.user.User.from_dict(body["new_user"]),
                )
        finally:
            return typing.cast(TerraParsedApiResponse, response)


class TerraApiResponse(TerraParsedApiResponse):
    def __init__(
        self,
        resp: requests.Response,
        dtype: str,
        user: typing.Optional[user_.User] = None,
        client: typing.Optional[Terra] = None,
    ) -> None:
        self.response_code: int = resp.status_code
        self.raw_body: typing.Optional[str] = resp.text
        self.json: typing.Optional[typing.Dict[str, typing.Any]] = None
        self.dtype: typing.Optional[str] = dtype
        try:
            body: typing.Dict[str, typing.Any] = resp.json()
            self.json = body
            self.dtype = body.get("type", dtype)
            self.parsed_response: TerraParsedApiResponse = _parse_api_body(self.dtype, body, user)
            if client:
                for e in typing.cast(SubscribedUsers, self.parsed_response).users:
                    e._client = client
        except json.decoder.JSONDecodeError:
            resp.raise_for_status()

    def get_parsed_response(self) -> TerraParsedApiResponse:
        """
        Get the parsed representation of the api response.

        Returns:
            :obj:`TerraParsedApiResponse`: Parsed representation of the data model.
        """
        return self.parsed_response

    def get_json(self) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """
        Get the dictionary (json) representation of the api response.

        Returns:
            :obj:`dict`: Dictionary representation of the api response.
        """
        return self.json


class TerraWebhookResponse(TerraParsedApiResponse):
    def __init__(
        self,
        resp: typing.Union[typing.Dict[str, typing.Any], requests.Response],
        user: typing.Optional[user_.User] = None,
        dtype: typing.Optional[str] = None,
    ) -> None:
        self.json: typing.Dict[str, typing.Any] = resp.json() if isinstance(resp, requests.Response) else resp
        self.dtype: typing.Optional[str] = self.json.get("type", dtype)
        self.parsed_response: TerraParsedApiResponse = _parse_api_body(self.dtype, self.json, user)

    def get_parsed_response(self) -> TerraParsedApiResponse:
        """
        Get the parsed representation of the api response.

        Returns:
            :obj:`TerraParsedApiResponse`: Parsed representation of the data model.
        """
        return self.parsed_response

    def get_json(self) -> typing.Dict[str, typing.Any]:
        """
        Get the dictionary (json) representation of the api response.

        Returns:
            :obj:`dict`: Dictionary representation of the api response.
        """
        return self.json


@dataclasses.dataclass
class GenericMessage(TerraParsedApiResponse):
    message: typing.Optional[str] = dataclasses.field(default=None)
    status: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class WidgetSession(TerraParsedApiResponse):
    expires_in: int = dataclasses.field(default=900)
    status: typing.Optional[str] = dataclasses.field(default=None)
    session_id: typing.Optional[str] = dataclasses.field(default=None)
    url: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class UserInfo(TerraParsedApiResponse):
    status: typing.Optional[str] = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)
    is_authenticated: bool = dataclasses.field(default=True)


@dataclasses.dataclass
class UserDeauthResp(TerraParsedApiResponse):
    status: typing.Optional[str] = dataclasses.field(default="success")


@dataclasses.dataclass
class HookResponse(TerraParsedApiResponse):
    status: typing.Optional[str] = dataclasses.field(default="success")
    type: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class AuthHookResponse(HookResponse):
    reference_id: typing.Optional[str] = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)
    widget_session_id: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class UserReauthHookResponse(HookResponse):
    message: typing.Optional[str] = dataclasses.field(default=None)
    old_user: typing.Optional[models.user.User] = dataclasses.field(default=None)
    new_user: typing.Optional[models.user.User] = dataclasses.field(default=None)


@dataclasses.dataclass
class UserDeauthHookResponse(HookResponse):
    message: typing.Optional[str] = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)


@dataclasses.dataclass
class AccessRevokedHookResponse(HookResponse):
    message: typing.Optional[str] = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)


@dataclasses.dataclass
class GoogleNoDataSourceHookResponse(HookResponse):
    message: typing.Optional[str] = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)


@dataclasses.dataclass
class ConnectionErrorHookResponse(HookResponse):
    message: typing.Optional[str] = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)


@dataclasses.dataclass
class RequestProcessingHookResponse(HookResponse):
    message: typing.Optional[str] = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)


@dataclasses.dataclass
class RequestCompletedHookResponse(HookResponse):
    message: typing.Optional[str] = dataclasses.field(default=None)
    reference: typing.Optional[str] = dataclasses.field(default=None)
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)


@dataclasses.dataclass
class SubscribedUsers(TerraParsedApiResponse):
    users: typing.List[models.user.User] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class UserAuthUrl(TerraParsedApiResponse):
    status: typing.Optional[str] = dataclasses.field(default=None)
    expires_in: int = dataclasses.field(default=900)
    auth_url: typing.Optional[str] = dataclasses.field(default=None)
    user_id: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class NoDataReturned(TerraParsedApiResponse):
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)
    status: typing.Optional[str] = dataclasses.field(default="not_available")
    message: typing.Optional[str] = dataclasses.field(default="Data type requested not available from provider")


@dataclasses.dataclass
class DataReturned(TerraParsedApiResponse):
    user: typing.Optional[models.user.User] = dataclasses.field(default=None)
    type: typing.Optional[str] = dataclasses.field(default=None)
    data: list[TerraParsedApiResponse] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class AuthenticationFailed(TerraParsedApiResponse):
    status: str = dataclasses.field(default="error")
    widget_session_id: typing.Optional[str] = dataclasses.field(default=None)
    reference_id: typing.Optional[str] = dataclasses.field(default=None)
    message: typing.Optional[str] = dataclasses.field(default="User failed to authenticate and has been deleted")
    type: str = dataclasses.field(default="auth")
    reason: str = dataclasses.field(default="auth_cancelled")


@dataclasses.dataclass
class ConnectionDegraded(TerraParsedApiResponse):
    status: typing.Optional[str] = dataclasses.field(default="warning")
    message: typing.Optional[str] = dataclasses.field(default="User connection degraded")
    type: typing.Optional[str] = dataclasses.field(default="connection_error")


@dataclasses.dataclass
class ProvidersResponse(TerraParsedApiResponse):
    status: typing.Optional[str] = dataclasses.field(default="warning")
    providers: typing.Optional[typing.List[str]] = dataclasses.field(default=None)
    sdk_providers: typing.Optional[typing.List[str]] = dataclasses.field(default=None)


@dataclasses.dataclass
class SentToWebhook(TerraParsedApiResponse):
    status: typing.Optional[str] = dataclasses.field(default=None)
    message: typing.Optional[str] = dataclasses.field(default=None)


USER_DATATYPES = [
    "activity",
    "athlete",
    "body",
    "daily",
    "menstruation",
    "sleep",
    "nutrition",
]
MODEL_MAPPING = {
    "activity": models.v2.activity.Activity,
    "body": models.v2.body.Body,
    "daily": models.v2.daily.Daily,
    "sleep": models.v2.sleep.Sleep,
    "menstruation": models.v2.menstruation.Menstruation,
    "athlete": models.v2.athlete.Athlete,
    "nutrition": models.v2.nutrition.Nutrition,
}

DTYPE_TO_RESPONSE = {
    "widget_session": WidgetSession,
    "auth_url": UserAuthUrl,
    "user_info": UserInfo,
    "subscriptions": SubscribedUsers,
    "providers": ProvidersResponse,
    "sent_to_webhook": SentToWebhook,
}

HOOK_TYPES = {
    "auth",
    "user_reauth",
    "access_revoked",
    "deauth",
    "google_no_datasource",
    "connexion_error",
    "request_processing",
    "request_completed",
}

HOOK_RESPONSE = {
    "auth": AuthHookResponse,
    "user_reauth": UserReauthHookResponse,
    "access_revoked": AccessRevokedHookResponse,
    "deauth": UserDeauthHookResponse,
    "google_no_datasource": GoogleNoDataSourceHookResponse,
    "connexion_error": ConnectionErrorHookResponse,
    "request_completed": RequestCompletedHookResponse,
    "request_processing": RequestProcessingHookResponse,
}

STATUS = {
    "not_available": NoDataReturned,
    "warning": ConnectionDegraded,
    "error": ConnectionDegraded,
}
