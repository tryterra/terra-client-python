# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class EnergyData(UncheckedBaseModel):
    energy_kilojoules: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total number of kiloJoules planned to be expended during the workout - represents the user's predefined goal for the workout
    """

    energy_planned_kilojoules: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total number of kiloJoules expended during the workout
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
