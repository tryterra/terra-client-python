# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .auth_event import AuthEvent
from .terra_user import TerraUser


class AuthErrorEvent(AuthEvent):
    """
    Authentication error event
    """

    user: TerraUser = pydantic.Field()
    """
    User who attempted to authenticate
    """

    provider: str = pydantic.Field()
    """
    Provider information
    """

    message: str = pydantic.Field()
    """
    Error message
    """

    reason: str = pydantic.Field()
    """
    Reason for the error
    """

    reference_id: str = pydantic.Field()
    """
    Client-provided reference ID
    """

    widget_session_id: str = pydantic.Field()
    """
    Widget session identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
