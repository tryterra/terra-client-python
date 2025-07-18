# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .indeterminate import Indeterminate
from .timestamp_localization import TimestampLocalization


class SleepMetadata(UncheckedBaseModel):
    end_time: str = pydantic.Field()
    """
    The end time of the associated sleep session, in ISO8601 format with microsecond precision. TimeZone info will be provided whenever possible. If absent, the time corresponds to the user's local time.
    """

    is_nap: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Flag indicating whether the sleep session was a nap, or the user's main sleep session for the day.
    """

    start_time: str = pydantic.Field()
    """
    The start time of the associated sleep session, in ISO8601 format with microsecond precision. Will always fall on midnight of any given day, and will always be equal to 24h before end_time. TimeZone info will be provided whenever possible. If absent, the time corresponds to the user's local time.
    """

    summary_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the sleep session.
    """

    timestamp_localization: typing.Optional[TimestampLocalization] = None
    upload_type: Indeterminate = pydantic.Field()
    """
    The upload type for the associated sleep session, providing information on whether this was an automatic sleep or user-entered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
