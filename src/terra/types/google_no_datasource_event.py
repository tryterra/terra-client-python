# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .terra_user import TerraUser


class GoogleNoDatasourceEvent(UncheckedBaseModel):
    """
    Google no datasource event
    """

    type: typing.Literal["google_no_datasource"] = "google_no_datasource"
    user: TerraUser = pydantic.Field()
    """
    Affected user
    """

    status: typing.Literal["warning"] = pydantic.Field(default="warning")
    """
    Status of the event
    """

    message: str = pydantic.Field()
    """
    Information about the issue
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
