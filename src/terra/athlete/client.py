# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAthleteClient, RawAthleteClient
from .types.athlete_fetch_response import AthleteFetchResponse


class AthleteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAthleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAthleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAthleteClient
        """
        return self._raw_client

    def fetch(
        self,
        *,
        user_id: str,
        to_webhook: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AthleteFetchResponse:
        """
        Fetches relevant profile info such as first & last name, birth date etc. for a given user ID

        Parameters
        ----------
        user_id : str
            Terra user ID (UUID format) to retrieve data for

        to_webhook : typing.Optional[bool]
            Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AthleteFetchResponse
            Returned upon successful data request

        Examples
        --------
        from terra import Terra

        client = Terra(
            dev_id="YOUR_DEV_ID",
            api_key="YOUR_API_KEY",
        )
        client.athlete.fetch(
            user_id="user_id",
        )
        """
        _response = self._raw_client.fetch(user_id=user_id, to_webhook=to_webhook, request_options=request_options)
        return _response.data


class AsyncAthleteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAthleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAthleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAthleteClient
        """
        return self._raw_client

    async def fetch(
        self,
        *,
        user_id: str,
        to_webhook: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AthleteFetchResponse:
        """
        Fetches relevant profile info such as first & last name, birth date etc. for a given user ID

        Parameters
        ----------
        user_id : str
            Terra user ID (UUID format) to retrieve data for

        to_webhook : typing.Optional[bool]
            Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AthleteFetchResponse
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
            await client.athlete.fetch(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch(
            user_id=user_id, to_webhook=to_webhook, request_options=request_options
        )
        return _response.data
