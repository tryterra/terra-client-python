# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class ElevationSample(UncheckedBaseModel):
    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    Time with which the record is associated, in ISO8601 format with microsecond precision. TimeZone info will be provided whenever possible. If absent, the time corresponds to the user's local time.
    """

    elev_meters: typing.Optional[float] = pydantic.Field(default=None)
    """
    User's altitude at a given point in time, in meters above sea level.
    """

    timer_duration_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    Time elapsed since the start of the workout, subtracting time during which the recording was paused
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
