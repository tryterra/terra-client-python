# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .hr_below_planned_workout_step_duration_duration_type import HrBelowPlannedWorkoutStepDurationDurationType


class HrBelowPlannedWorkoutStepDuration(UncheckedBaseModel):
    hr_below_bpm: typing.Optional[int] = pydantic.Field(default=None)
    """
    Threshold heart rate goal to complete the workout step - once the user's heart rate reaches below this value, the step will be completed
    """

    duration_type: typing.Optional[HrBelowPlannedWorkoutStepDurationDurationType] = pydantic.Field(default=None)
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
