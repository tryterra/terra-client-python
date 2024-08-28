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

__all__ = ["User"]

import dataclasses
import typing as t

from terra import exceptions
from terra.models.base_model import TerraDataModel

if t.TYPE_CHECKING:
    import datetime

    from terra import base_client
    from terra.api import api_responses


@dataclasses.dataclass
class User(TerraDataModel):
    def __init__(
        self,
        client: t.Optional[base_client.Terra] = None,
        user_id: t.Optional[str] = None,
        reference_id: t.Optional[str] = None,
        provider: t.Optional[str] = None,
        last_webhook_update: t.Optional[str] = None,
        scopes: t.Optional[str] = None,
    ) -> None:
        self.user_id = user_id
        self.reference_id = reference_id
        self.provider = provider
        self.last_webhook_update = last_webhook_update
        self.scopes = scopes
        self._client = client
        self._resource = None

    def _has_client(self) -> bool:
        return self._client is not None

    def fill_in_user_info(self) -> None:
        """
        Internal method used to retrieve data for User.

        Args:
            dtype (:obj:`str`): datatype to be fetched
        """
        if self._client is None:
            raise exceptions.NoClientAvailable

        if self._client:
            user_info = self._client.get_user_info(self)
            if not user_info.json or user_info.json.get("status") == "error":
                raise exceptions.NoUserInfoException

            self.provider = user_info.json["user"]["provider"]
            self.last_webhook_update = user_info.json["user"]["last_webhook_update"]
            self.scopes = user_info.json["user"]["scopes"]

    def _check_client(self) -> None:
        """
        Internal method used to check if user is connected to a client.

        Returns:
            :obj:`None`
        """
        if self._client is None:
            raise exceptions.NoClientAvailable

    def get_activity(
        self,
        start_date: datetime.datetime,
        end_date: t.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: t.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves workouts/activity data for a given User object. By default, data will be asynchronously sent to
        registered webhook URL.

        Args:
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
        if self._client is None:
            raise exceptions.NoClientAvailable

        return self._client._get_arbitrary_data(
            dtype="activity",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_body(
        self,
        start_date: datetime.datetime,
        end_date: t.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: t.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves body metrics data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
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
        if self._client is None:
            raise exceptions.NoClientAvailable

        return self._client._get_arbitrary_data(
            dtype="body",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_nutrition(
        self,
        start_date: datetime.datetime,
        end_date: t.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: t.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves nutrition data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
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
        if self._client is None:
            raise exceptions.NoClientAvailable

        return self._client._get_arbitrary_data(
            dtype="nutrition",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_daily(
        self,
        start_date: datetime.datetime,
        end_date: t.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: t.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves daily summary data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
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
        if self._client is None:
            raise exceptions.NoClientAvailable

        return self._client._get_arbitrary_data(
            dtype="daily",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_sleep(
        self,
        start_date: datetime.datetime,
        end_date: t.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: t.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves sleep data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:

            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default
                to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
            with_samples (:obj:`bool`): Whether to respond with samples (e.g heartrate samples) included or not
            **kwargs: Extra kwargs to pass to the request method

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occurred
        """
        if self._client is None:
            raise exceptions.NoClientAvailable

        return self._client._get_arbitrary_data(
            dtype="sleep",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )

    def get_athlete(
        self,
        to_webhook: bool = True,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves profile info/athlete data for a given User object. By default, data will be asynchronously sent to
        registered webhook URL.

        Args:
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed
                response object if no error has occurred
        """
        if self._client is None:
            raise exceptions.NoClientAvailable

        return self._client._get_arbitrary_data(dtype="athlete", user=self, to_webhook=to_webhook)

    def get_menstruation(
        self,
        start_date: datetime.datetime,
        end_date: t.Optional[datetime.datetime] = None,
        to_webhook: bool = True,
        with_samples: bool = True,
        **kwargs: t.Any,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves daily summary data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default
                to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
            with_samples (:obj:`bool`): Whether to respond with samples (e.g heartrate samples) included or not
            **kwargs: Extra kwargs to pass to the request method

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response
                object if no error has occurred

        """
        if self._client is None:
            raise exceptions.NoClientAvailable

        return self._client._get_arbitrary_data(
            dtype="menstruation",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
            with_samples=with_samples,
            **kwargs,
        )
