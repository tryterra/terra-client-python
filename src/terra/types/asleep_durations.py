# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel


class AsleepDurations(UncheckedBaseModel):
    duration_asleep_state_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total duration for which the user was asleep, in any state.
    """

    duration_deep_sleep_state_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total duration for which the user was in a state of deep sleep.
    """

    duration_light_sleep_state_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total duration for which the user was in a state of light sleep.
    """

    duration_rem_sleep_state_seconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="duration_REM_sleep_state_seconds")
    ] = pydantic.Field(default=None)
    """
    Total duration for which the user was in a state of REM sleep.
    """

    num_rem_events: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="num_REM_events")] = (
        pydantic.Field(default=None)
    )
    """
    Number of periods of REM sleep captured during the sleep session.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
