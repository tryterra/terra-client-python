# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .oxygen_saturation_sample import OxygenSaturationSample
from .vo_2_max_sample import Vo2MaxSample


class OxygenData(UncheckedBaseModel):
    avg_saturation_percentage: typing.Optional[float] = pydantic.Field(default=None)
    """
    Average Oxygen Saturation percentage of the user during the day (SpO2 or SmO2).
    """

    saturation_samples: typing.Optional[typing.List[OxygenSaturationSample]] = pydantic.Field(default=None)
    """
    Array of Oxygen Saturation percentage datapoints sampled throughout the day.
    """

    vo_2_samples: typing_extensions.Annotated[
        typing.Optional[typing.List[Vo2MaxSample]], FieldMetadata(alias="vo2_samples")
    ] = pydantic.Field(default=None)
    """
    Array of VO2 datapoints sampled throughout the day.
    """

    vo_2_max_ml_per_min_per_kg: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="vo2max_ml_per_min_per_kg")
    ] = pydantic.Field(default=None)
    """
    VO2Max for the given user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
