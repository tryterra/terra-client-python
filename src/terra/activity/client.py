# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.activity import Activity
from .raw_client import AsyncRawActivityClient, RawActivityClient
from .types.activity_fetch_request_start_date import ActivityFetchRequestStartDate
from .types.activity_fetch_response import ActivityFetchResponse
from .types.activity_write_response import ActivityWriteResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ActivityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActivityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActivityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActivityClient
        """
        return self._raw_client

    def fetch(
        self,
        *,
        user_id: str,
        start_date: ActivityFetchRequestStartDate,
        end_date: typing.Optional[int] = None,
        to_webhook: typing.Optional[bool] = None,
        with_samples: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActivityFetchResponse:
        """
        Fetches completed workout sessions, with a defined start and end time and activity type (e.g. running, cycling, etc.)

        Parameters
        ----------
        user_id : str
            Terra user ID (UUID format) to retrieve data for

        start_date : ActivityFetchRequestStartDate
            Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)

        end_date : typing.Optional[int]
            End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)

        to_webhook : typing.Optional[bool]
            Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)

        with_samples : typing.Optional[bool]
            Boolean flag specifying whether to include detailed samples in the returned payload (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivityFetchResponse
            Returned upon successful data request

        Examples
        --------
        from terra import Terra

        client = Terra(
            dev_id="YOUR_DEV_ID",
            api_key="YOUR_API_KEY",
        )
        client.activity.fetch(
            user_id="user_id",
            start_date=1,
        )
        """
        _response = self._raw_client.fetch(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
            to_webhook=to_webhook,
            with_samples=with_samples,
            request_options=request_options,
        )
        return _response.data

    def write(
        self, *, data: typing.Sequence[Activity], request_options: typing.Optional[RequestOptions] = None
    ) -> ActivityWriteResponse:
        """
        Used to post activity data to a provider. This endpoint only works for users connected via Wahoo. Returns error for other providers.

        Parameters
        ----------
        data : typing.Sequence[Activity]
            List of user-tracked workouts to post to data provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivityWriteResponse
            Returned when activity was successfully created on the provider

        Examples
        --------
        from terra import Activity, ActivityMetadata, Terra

        client = Terra(
            dev_id="YOUR_DEV_ID",
            api_key="YOUR_API_KEY",
        )
        client.activity.write(
            data=[
                Activity(
                    metadata=ActivityMetadata(
                        end_time="2022-10-28T10:00:00.000000+01:00",
                        start_time="1999-11-23T09:00:00.000000+02:00",
                        summary_id="123e4567-e89b-12d3-a456-426614174000",
                        type=1.1,
                        upload_type=1.1,
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.write(data=data, request_options=request_options)
        return _response.data


class AsyncActivityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActivityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActivityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActivityClient
        """
        return self._raw_client

    async def fetch(
        self,
        *,
        user_id: str,
        start_date: ActivityFetchRequestStartDate,
        end_date: typing.Optional[int] = None,
        to_webhook: typing.Optional[bool] = None,
        with_samples: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActivityFetchResponse:
        """
        Fetches completed workout sessions, with a defined start and end time and activity type (e.g. running, cycling, etc.)

        Parameters
        ----------
        user_id : str
            Terra user ID (UUID format) to retrieve data for

        start_date : ActivityFetchRequestStartDate
            Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)

        end_date : typing.Optional[int]
            End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)

        to_webhook : typing.Optional[bool]
            Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)

        with_samples : typing.Optional[bool]
            Boolean flag specifying whether to include detailed samples in the returned payload (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivityFetchResponse
            Returned upon successful data request

        Examples
        --------
        import asyncio

        from terra import AsyncTerra

        client = AsyncTerra(
            dev_id="YOUR_DEV_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.activity.fetch(
                user_id="user_id",
                start_date=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
            to_webhook=to_webhook,
            with_samples=with_samples,
            request_options=request_options,
        )
        return _response.data

    async def write(
        self, *, data: typing.Sequence[Activity], request_options: typing.Optional[RequestOptions] = None
    ) -> ActivityWriteResponse:
        """
        Used to post activity data to a provider. This endpoint only works for users connected via Wahoo. Returns error for other providers.

        Parameters
        ----------
        data : typing.Sequence[Activity]
            List of user-tracked workouts to post to data provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivityWriteResponse
            Returned when activity was successfully created on the provider

        Examples
        --------
        import asyncio

        from terra import Activity, ActivityMetadata, AsyncTerra

        client = AsyncTerra(
            dev_id="YOUR_DEV_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.activity.write(
                data=[
                    Activity(
                        metadata=ActivityMetadata(
                            end_time="2022-10-28T10:00:00.000000+01:00",
                            start_time="1999-11-23T09:00:00.000000+02:00",
                            summary_id="123e4567-e89b-12d3-a456-426614174000",
                            type=1.1,
                            upload_type=1.1,
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write(data=data, request_options=request_options)
        return _response.data
