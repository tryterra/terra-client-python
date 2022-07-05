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

import dataclasses
import datetime
import typing as t

from terra import exceptions
from terra import models
from terra.models.base_model import TerraDataModel

if t.TYPE_CHECKING:
    from terra import base_client
    from terra.api import api_responses

__all__ = ["User"]


def check_has_client(f : function) -> function:
    def wrapper(*args, **kwargs) -> function:
        """
        Check used on a User object's methods which require it to be initialized from a Client instance

        Args:
            user (:obj:`models.User`): User object

        Returns:
            ``None``
        """

        if args[0]._client is None:
            raise exceptions.NoClientAvailable

        return f(*args, **kwargs)

    return wrapper


@dataclasses.dataclass
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

    def _has_client(self) -> bool:
        return self._client is not None

    def fill_in_user_info(self) -> None:
        """
        Internal method used to retrieve data for User

        Args:
            dtype (:obj:`str`): datatype to be fetched
            **kwargs: optional additional parameters for the request

        Returns:
            None
        """
        if self._client:
            user_info = self._client.get_user_info(self)

            self.provider = user_info.json["user"]["provider"]
            self.last_webhook_update = user_info.json["user"]["provider"]

    # @check_has_client
    # def get_bulk(
    #     self,
    #     start_date: datetime.datetime,
    #     end_date: datetime.datetime = None,
    #     to_webhook=True,
    # ) -> models.api_responses.TerraApiResponse:
    #     """
    #     Retrieves bulk data for a given User object. By default, data will be asynchronously sent to registered
    #     webhook URL.

    #     Args:

    #         start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
    #         end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
    #         to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

    #     Returns:
    #         :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

    #     """
    #     return self._client._get_arbitrary_data(
    #         dtype="bulkUserInfo",
    #         user=self,
    #         start_date=int(start_date.timestamp()),
    #         end_date=int(end_date.timestamp()) if end_date is not None else None,
    #         to_webhook=to_webhook,
    #     )

    @check_has_client
    def get_activity(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves workouts/activity data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:

            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._client._get_arbitrary_data(
            dtype="activity",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
        )

    @check_has_client
    def get_body(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> api_responses.TerraApiResponse:
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
        return self._client._get_arbitrary_data(
            dtype="body",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
        )

    @check_has_client
    def get_nutrition(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves nutrition data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:
            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._client._get_arbitrary_data(
            dtype="nutrition",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
        )

    @check_has_client
    def get_daily(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> api_responses.TerraApiResponse:
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
        return self._client._get_arbitrary_data(
            dtype="daily",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
        )

    @check_has_client
    def get_sleep(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves sleep data for a given User object. By default, data will be asynchronously sent to registered
        webhook URL.

        Args:

            start_date (:obj:`datetime.datetime`): Datetime object for which to fetch data
            end_date:obj (:`datetime.datetime`): Optional end_date for which to fetch data - if not set, will default to start_date + 24h according to current API specifications
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body

        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._client._get_arbitrary_data(
            dtype="sleep",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
        )

    @check_has_client
    def get_athlete(
        self,
        to_webhook=True,
    ) -> api_responses.TerraApiResponse:
        """
        Retrieves profile info/athlete data for a given User object. By default, data will be asynchronously sent to
        registered webhook URL.

        Args:
            to_webhook (:obj:`bool`): Whether to send data to registered webhook URL or return as a response body
        Returns:
            :obj:`models.api_responses.TerraApiResponse`: API response object containing DataReturned parsed response object if no error has occured

        """
        return self._client._get_arbitrary_data("athlete", self, to_webhook=to_webhook)

    @check_has_client
    def get_menstruation(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime = None,
        to_webhook=True,
    ) -> t.Optional[api_responses.TerraApiResponse]:
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
        return self._client._get_arbitrary_data(
            dtype="menstruation",
            user=self,
            start_date=int(start_date.timestamp()),
            end_date=int(end_date.timestamp()) if end_date is not None else None,
            to_webhook=to_webhook,
        )
