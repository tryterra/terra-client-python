# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from ...types.terra_user import TerraUser
from .nutrition_delete_response_processed_data_item import NutritionDeleteResponseProcessedDataItem


class NutritionDeleteResponse(UncheckedBaseModel):
    user: typing.Optional[TerraUser] = None
    processed_data: typing.Optional[typing.List[NutritionDeleteResponseProcessedDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
