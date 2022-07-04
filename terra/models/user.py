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

import datetime
import typing as t

import requests

from terra import checks
from terra import constants
from terra import models
from terra import utils
from terra.models.base_model import TerraDataModel

if t.TYPE_CHECKING:
    from terra import base_client

__all__ = ["User"]


class User(TerraDataModel):
    def __init__(
        self,
        user_id: t.Optional[str] = None,
        provider: t.Optional[str] = None,
        last_webhook_update: t.Optional[str] = None,
        client: t.Optional[base_client.Terra] = None,
    ) -> None:
        self.user_id = user_id
        self.provider = provider
        self.last_webhook_update = last_webhook_update
        self._client = client
        self._resource = None

    def fill_in_user_info(self):
        if self._client:
            user_info = self._client.get_user_info(self)
            self.provider = user_info["resource"]
            self.last_webhook_update = user_info["last_webhook_update"]

    def _get_arbitrary_data(
        self, dtype: str, **kwargs
    ) -> models.api_responses.TerraApiResponse:
        """
        Internal method used to retrieve data for User

        Args:
            dtype (:obj:`str`): datatype to be fetched
            **kwargs: optional additional parameters for the request

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        params = {"user_id": self.user_id}
        params = utils.update_if_not_none(params, kwargs)
        data_resp = requests.get(
            f"{constants.BASE_URL}/{dtype}",
            params=params,
            headers=self._client._auth_headers,
        )
        return models.api_responses.TerraApiResponse(data_resp, self)

    @checks.check_has_client
    def get_activity(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> models.api_responses.TerraApiResponse:
        """
        Retrieves workouts/activity data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._get_arbitrary_data(
            "activity",
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
        )

    @checks.check_has_client
    def get_body(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> models.api_responses.TerraApiResponse:
        """
        Retrieves body metrics data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._get_arbitrary_data(
            "body",
            start_date=start_date,
            end_date=end_date,
            to_webhook=to_webhook,
        )

    @checks.check_has_client
    def get_daily(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> models.api_responses.TerraApiResponse:
        """
        Retrieves daily summary data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._get_arbitrary_data(
            "daily",
            start_date=start_date,
            end_date=end_date,
            to_webhook=to_webhook,
        )

    @checks.check_has_client
    def get_sleep(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> models.api_responses.TerraApiResponse:
        """
        Retrieves sleep data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            user (:obj:`models.user.User`): User for whom to fetch data
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._get_arbitrary_data(
            "sleep",
            start_date=start_date,
            end_date=end_date,
            to_webhook=to_webhook,
        )

    @checks.check_has_client
    def get_athlete(
        self,
        to_webhook=True,
    ) -> models.api_responses.TerraApiResponse:
        """
        Retrieves profile info/athlete data for a given User object. By default, data will be asynchronously sent to
        registered webhook URL.

        Args:
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._get_arbitrary_data(self, "athlete", to_webhook=to_webhook)

    @checks.check_has_client
    def get_menstruation(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> t.Optional[models.api_responses.TerraApiResponse]:
        """
        Retrieves daily summary data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._get_arbitrary_data(
            "menstruation",
            start_date=start_date,
            end_date=end_date,
            to_webhook=to_webhook,
        )
