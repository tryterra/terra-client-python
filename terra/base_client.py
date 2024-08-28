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

__all__ = ["Terra"]

import hashlib
import hmac
import json
import typing

from requests import Session

from terra import constants
from terra import utils
from terra.api import api_responses
from terra.models import user as user_

if typing.TYPE_CHECKING:
    import datetime

    import flask


class Terra:
    """
    Constructor of the Terra class.

    Args:
        api_key (:obj:`str`) : Your API Key
        dev_id (:obj:`str`) : Your dev ID
        secret (:obj:`str`, optional): Your terra secret (for web hooks). Defaults to None.
    """

    def __init__(
        self,
        api_key: str,
        dev_id: str,
        secret: typing.Optional[str] = None,
        session: typing.Optional[Session] = None,
    ) -> None:
        self.api_key = api_key
        self.dev_id = dev_id
        self.secret = secret
        self._session = session if session is not None else Session()

    @property
    def _auth_headers(self) -> typing.Dict[str, str]:
        """
        Internal method used to fill in authentication headers for all requests to the API.

        Returns:
            :obj:`dict`: Dictionary of required auth headers
        """
        return {"x-api-key": self.api_key, "dev-id": self.dev_id}

    def from_user_id(self, user_id: str) -> user_.User:
        """
        Creates a User instance out of a UUID corresponding to a registered User on the API.

        Args:
            user_id (:obj:`str`): UUID corresponding to a user currently authenticated on the API

        Returns:
            :obj:`User`: Created User instance
        """
        user = user_.User(user_id=user_id, client=self)
        user.fill_in_user_info()
        return user

    def _get_arbitrary_data(self, user: user_.User, dtype: str, **kwargs: typing.Any) -> api_responses.TerraApiResponse:
        """
        Internal method used to retrieve data for a given User.

        Args:
            user (:obj:`models.user.User`): The user to retrieve data for
            dtype (:obj:`str`): datatype to be fetched
            **kwargs: optional additional parameters for the request

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occured
        """
        params = {"user_id": user.user_id}
        params = utils.update_if_not_none(params, kwargs)

        data_resp = self._session.get(
            f"{constants.BASE_URL}/{dtype}",
            params=params,
            headers=self._auth_headers,
        )
        data_resp.raise_for_status()

        return api_responses.TerraApiResponse(data_resp, user=user, dtype=dtype)

    def get_activity_for_user(
        self,
        user: user_.User,
        start_date: datetime.datetime,
        end_date: typing.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: typing.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves workouts/activity data for a given User object. By default, data will be asynchronously sent
        to registered webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will
                default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
            with_samples (:obj:`bool`): Whether to respond with samples (e.g heartrate samples) included or not
            **kwargs: Extra kwargs to pass to the request method

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occurred
        """
        return user.get_activity(
            start_date=start_date,
            end_date=end_date if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_body_for_user(
        self,
        user: user_.User,
        start_date: datetime.datetime,
        end_date: typing.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: typing.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves body metrics data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will
                default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
            with_samples (:obj:`bool`): Whether to respond with samples (e.g heartrate samples) included or not
            **kwargs: Extra kwargs to pass to the request method

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occured
        """
        return user.get_body(
            start_date=start_date,
            end_date=end_date if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_daily_for_user(
        self,
        user: user_.User,
        start_date: datetime.datetime,
        end_date: typing.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: typing.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves daily summary data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will
                default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
            with_samples (:obj:`bool`): Whether to respond with samples (e.g heartrate samples) included or not
            **kwargs: Extra kwargs to pass to the request method

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occured
        """
        return user.get_daily(
            start_date=start_date,
            end_date=end_date if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_sleep_for_user(
        self,
        user: user_.User,
        start_date: datetime.datetime,
        end_date: typing.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: typing.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves sleep data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will
                default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
            with_samples (:obj:`bool`): Whether to respond with samples (e.g heartrate samples) included or not
            **kwargs: Extra kwargs to pass to the request method

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occured
        """
        return user.get_sleep(
            start_date=start_date,
            end_date=end_date if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_athlete_for_user(
        self,
        user: user_.User,
        to_webhook: bool = True,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves profile info/athlete data for a given User object. By default, data will be asynchronously sent to
        registered webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occured

        """
        return self._get_arbitrary_data(user, "athlete", to_webhook=to_webhook)

    def get_menstruation_for_user(
        self,
        user: user_.User,
        start_date: datetime.datetime,
        end_date: typing.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: typing.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves daily summary data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set,
                will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
            with_samples (:obj:`bool`): Whether to respond with samples (e.g heartrate samples) included or not
            **kwargs: Extra kwargs to pass to the request method

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occured
        """
        return user.get_menstruation(
            start_date=start_date,
            end_date=end_date if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_nutrition_for_user(
        self,
        user: user_.User,
        start_date: datetime.datetime,
        end_date: typing.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: typing.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves daily summary data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will
                default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
            with_samples (:obj:`bool`): Whether to respond with samples (e.g heartrate samples) included or not
            **kwargs: Extra kwargs to pass to the request method

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occurred
        """
        return user.get_nutrition(
            start_date=start_date,
            end_date=end_date if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def generate_widget_session(
        self,
        providers: typing.List[str],
        auth_success_redirect_url: typing.Optional[str] = None,
        auth_failure_redirect_url: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        reference_id: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Generates a widget session used to allow an end user to authenticate through the API. Users should be
        redirected to the given URL in order to complete authentication.

        Args:
            providers (List[:obj:`str`]): Providers to display on widget wearable selection screen, by leaving
                it empty it will use all default providers
            auth_success_redirect_url (Optional[:obj:`str`]): URL to redirect to upon successful authentication
            auth_failure_redirect_url (Optional[:obj:`str`]): URL to redirect to upon unsuccessful authentication
            language (Optional[:obj:`str`]): Language to display widget in
            reference_id (Optional[:obj:`str`]): ID of a user in your app, which will be returned at the end of
                a successful auth
            **kwargs: Optional additional arguments to be passed in to the body of the request

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing WidgetSession parsed
                response object if no error has occurred
        """
        maybe_body_payload = {
            "providers": ",".join(providers) if providers else None,
            "auth_success_redirect_url": auth_success_redirect_url,
            "auth_failure_redirect_url": auth_failure_redirect_url,
            "language": language,
            "reference_id": reference_id,
        }
        body_payload = utils.update_if_not_none({}, maybe_body_payload)
        body_payload.update(kwargs)

        widget_resp = self._session.post(
            f"{constants.BASE_URL}/auth/generateWidgetSession",
            headers=self._auth_headers,
            json=body_payload,
        )
        widget_resp.raise_for_status()
        return api_responses.TerraApiResponse(widget_resp, dtype="widget_session")

    def generate_authentication_url(
        self,
        resource: str,
        auth_success_redirect_url: typing.Optional[str] = None,
        auth_failure_redirect_url: typing.Optional[str] = None,
        reference_id: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Generates an authentication URL to allow an end user to authenticate through the API. Users should be
        redirected to the given URL in order to complete authentication. User ID will be provided in the response
        for convenience (note that at this stage, said user will have yet to complete the auth flow).

        Args:
            resource (:obj:`str`): Provider to authenticate user with
            auth_success_redirect_url (Optional[:obj:`str`]): URL to redirect to upon successful authentication
            auth_failure_redirect_url (Optional[:obj:`str`]): URL to redirect to upon unsuccessful authentication
            reference_id (Optional[:obj:`str`]): ID of a user in your app, which will be returned at the
                end of a successful auth
            **kwargs: Optional additional arguments to be passed in to the body of the request

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing UserAuthUrl parsed
                response object if no error has occurred
        """
        body_payload = {
            "resource": resource,
            "auth_success_redirect_url": auth_success_redirect_url,
            "auth_failure_redirect_url": auth_failure_redirect_url,
            "reference_id": reference_id,
        }
        body_payload.update(kwargs)

        auth_resp = self._session.post(
            f"{constants.BASE_URL}/auth/authenticateUser",
            headers=self._auth_headers,
            json=body_payload,
        )
        auth_resp.raise_for_status()

        return api_responses.TerraApiResponse(auth_resp, dtype="auth_url")

    def get_user_info(self, user: user_.User) -> api_responses.TerraApiResponse:
        """
        Retrieve information on a given User, including is_authenticated status, indicating if the user has
        successfully completed auth flow, or has yet to do so.

        Args:
            user (:obj:`models.user.User`): User to retrieve information for

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing UserInfo parsed
                response object if no error has occurred

        Note:
            Also updates information on user object passed as an argument
        """
        user_resp = self._session.get(
            f"{constants.BASE_URL}/userInfo",
            params={"user_id": user.user_id},
            headers=self._auth_headers,
        )
        user_resp.raise_for_status()
        return api_responses.TerraApiResponse(user_resp, dtype="user_info")

    def deauthenticate_user(self, user: user_.User) -> api_responses.TerraApiResponse:
        """
        Deauthenticates the given User from the Api. If successful, this will trigger a `deauth` webhook event.

        Args:
            user (:obj:`models.user.User`): User to Deauthenticate from the API

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing UserDeauthResp parsed
                response object if no error has occurred
        """
        deauth_resp = self._session.delete(
            f"{constants.BASE_URL}/auth/deauthenticateUser",
            params={"user_id": user.user_id},
            headers=self._auth_headers,
        )
        deauth_resp.raise_for_status()
        return api_responses.TerraApiResponse(deauth_resp, dtype="user_deauth")

    def list_users(self) -> api_responses.TerraApiResponse:
        """
        Lists all users registered under Client's credentials on the API.

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing SubscribedUsers parsed
                response object if no error has occurred
        """
        users_resp = self._session.get(f"{constants.BASE_URL}/subscriptions", headers=self._auth_headers)
        users_resp.raise_for_status()
        return api_responses.TerraApiResponse(users_resp, dtype="subscriptions", client=self)

    def list_providers(self) -> api_responses.TerraApiResponse:
        """
        Lists all providers on the API.

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing ProvidersResponse
                parsed response object if no error has occurred
        """
        providers_resp = self._session.get(f"{constants.BASE_URL}/integrations", headers=self._auth_headers)
        providers_resp.raise_for_status()
        return api_responses.TerraApiResponse(providers_resp, dtype="providers")

    def check_terra_signature(self, body: str, header: str) -> bool:
        """
        Function to test if the body of an API response comes from terra using SHA256.

        Args:
            body (:obj:`str`): The body from API response as a string
            header (:obj:`str`): The header from API response as a string

        Returns:
            :obj:`bool`: True if the API response comes from Terra
        """
        if self.secret is None:
            raise ValueError("A valid 'secret' is required for web hooks. Please provide your Terra secret.")

        t, sig = (pair.split("=")[-1] for pair in header.split(","))

        computed_signature = hmac.new(
            bytes(self.secret, "utf-8"),
            msg=bytes(f"{t}.{body}", "utf-8"),
            digestmod=hashlib.sha256,
        ).hexdigest()

        return computed_signature == sig

    def handle_flask_webhook(self, request: flask.Request) -> typing.Optional[api_responses.TerraWebhookResponse]:
        """
        Parses Terra webhooks from a flask request.

        Args:
            request (:obj:`flask.request`): the flask request object

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing ProvidersResponse parsed
                response object if no error has occurred
        """
        if not self.check_terra_signature(request.get_data().decode("utf-8"), request.headers["terra-signature"]):
            return None
        ff = api_responses.TerraWebhookResponse(request.get_json(), dtype="hook")

        return ff

    def handle_webhook(
        self, payload: str, terra_signature_header: str
    ) -> typing.Optional[api_responses.TerraWebhookResponse]:
        """
        Function to Parse web hooks from Terra.

        Args:
            payload (:obj:`str`): The body from API response as a string
            terra_signature_header (:obj:`str`): The terra_signature header from API response as a string

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing ProvidersResponse parsed
                response object if no error has occurred
        """
        if not self.check_terra_signature(payload, terra_signature_header):
            return None
        return api_responses.TerraWebhookResponse(json.loads(payload), dtype="hook")
