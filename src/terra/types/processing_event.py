# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .terra_user import TerraUser


class ProcessingEvent(UncheckedBaseModel):
    """
    Processing event returned when data is being fetched asynchronously
    """

    type: typing.Literal["processing"] = "processing"
    status: typing.Literal["success"] = pydantic.Field(default="success")
    """
    Status of the processing
    """

    message: str = pydantic.Field()
    """
    Information about the processing
    """

    user: TerraUser = pydantic.Field()
    """
    User whose data is being processed
    """

    retry_after_seconds: int = pydantic.Field()
    """
    Seconds to wait before retrying
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
