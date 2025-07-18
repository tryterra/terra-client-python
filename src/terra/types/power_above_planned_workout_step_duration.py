# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .power_above_planned_workout_step_duration_duration_type import PowerAbovePlannedWorkoutStepDurationDurationType


class PowerAbovePlannedWorkoutStepDuration(UncheckedBaseModel):
    power_above_watts: typing.Optional[int] = pydantic.Field(default=None)
    """
    Threshold power goal to complete the workout step - once the user reaches above this power level, the step will be completed
    """

    duration_type: typing.Optional[PowerAbovePlannedWorkoutStepDurationDurationType] = pydantic.Field(default=None)
    """
    Type of condition that must be fulfilled to consider the workout step complete
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
