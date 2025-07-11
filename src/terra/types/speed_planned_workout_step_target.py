# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .speed_planned_workout_step_target_target_type import SpeedPlannedWorkoutStepTargetTargetType


class SpeedPlannedWorkoutStepTarget(UncheckedBaseModel):
    target_type: typing.Optional[SpeedPlannedWorkoutStepTargetTargetType] = pydantic.Field(default=None)
    """
    Type of target for the workout - i.e. metric type for which a criterion must be met for the workout to be completed
    """

    speed_percentage_high: typing.Optional[float] = pydantic.Field(default=None)
    """
    Maximum speed threshold for the workout step - i.e. the user is to stay under this value during the workout step
    """

    speed_percentage_low: typing.Optional[float] = pydantic.Field(default=None)
    """
    Minimum speed threshold for the workout step - i.e. the user is to stay above this value during the workout step
    """

    speed_percentage: typing.Optional[float] = pydantic.Field(default=None)
    """
    Ideal percentage of user's Threshold Speed, based off their Threshold Pace, to be maintained workout step. Usually, the Threshold Pace is defined as the pace one could race at for 50 to 60 minutes
    """

    speed_meters_per_second: typing.Optional[float] = pydantic.Field(default=None)
    """
    Ideal speed value to be maintained for the workout step
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
