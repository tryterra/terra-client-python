# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class DailyPatternSample(UncheckedBaseModel):
    time_from_midnight: typing.Optional[int] = pydantic.Field(default=None)
    """
    Hour of the day, represented as an integer from 0 to 23, where 0 is midnight and 23 is the hour before the next midnight.
    """

    percentile_5: typing.Optional[int] = pydantic.Field(default=None)
    """
    Percentile 5 of the glucose level at the given time of day.
    """

    percentile_25: typing.Optional[int] = pydantic.Field(default=None)
    """
    Percentile 25 of the glucose level at the given time of day.
    """

    percentile_50: typing.Optional[int] = pydantic.Field(default=None)
    """
    Percentile 50 of the glucose level at the given time of day.
    """

    percentile_75: typing.Optional[int] = pydantic.Field(default=None)
    """
    Percentile 75 of the glucose level at the given time of day.
    """

    percentile_95: typing.Optional[int] = pydantic.Field(default=None)
    """
    Percentile 95 of the glucose level at the given time of day.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
