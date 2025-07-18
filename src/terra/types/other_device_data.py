# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .device_data_type import DeviceDataType


class OtherDeviceData(UncheckedBaseModel):
    manufacturer: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device manufacturer name.
    """

    hardware_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hardware version of the device.
    """

    serial_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device Serial Number.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device name - note that this can also be the name of the application/package which the data comes from, if coming from a data aggregator such as Google Fit.
    """

    software_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device Software Version.
    """

    activation_timestamp: typing.Optional[str] = None
    data_provided: typing.Optional[typing.List[DeviceDataType]] = None
    last_upload_date: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
