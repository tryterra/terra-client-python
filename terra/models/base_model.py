#  Copyright 2022 Terra Enabling Developers Limited
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from __future__ import annotations

__all__ = ["TerraDataModel"]

import dataclasses
import enum
import pydoc
import typing

PRIMITIVES = (str, int, bool, float, type(None), dict)
DatamodelT = typing.TypeVar("DatamodelT", bound="TerraDataModel")


class TerraDataModel:
    """Base class for all data models that terra returns."""

    def _get_attrs(self) -> typing.Iterable[str]:
        return filter(
            lambda a: not a.startswith("_"),
            set(dir(self)).difference(set(dir(TerraDataModel))),
        )

    def keys(self) -> typing.Generator[str, None, None]:
        yield from self._get_attrs()

    def values(self) -> typing.Generator[typing.Any, None, None]:
        attrs = self._get_attrs()
        yield from (getattr(self, attr) for attr in attrs)

    def items(self) -> typing.Generator[typing.Tuple[str, typing.Any], None, None]:
        attrs = self._get_attrs()
        for attr in attrs:
            yield attr, getattr(self, attr)

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """
        Get the dictionary (json) representation of the data model.

        This method inspects the attributes of the instance that it is being called on
        to determine how to build the correct payload from the data stored.

        Returns:
            :obj:`dict`: Dictionary representation of the data model.
        """
        attrs = self._get_attrs()

        output: typing.Dict[typing.Any, typing.Any] = {}
        for attr in attrs:
            attr_val = getattr(self, attr)
            if isinstance(attr_val, enum.IntEnum):
                output[attr] = int(attr_val)
            elif type(attr_val) in PRIMITIVES:
                output[attr] = attr_val
            elif isinstance(attr_val, list):
                if (attr_val and type(attr_val[0]) in PRIMITIVES) or not attr_val:  # type: ignore
                    output[attr] = attr_val
                else:
                    output[attr] = [item.to_dict() for item in attr_val]  # type: ignore
            else:
                output[attr] = attr_val.to_dict()
        return output

    def filter_data(self: TerraDataModel, term: str) -> typing.Generator[DatamodelT, None, None]:  # type: ignore
        """
        Returns a generator of all the data models that match the filter.

        Args:
            term:obj:`str`: the word to filter with

        Returns:
            :obj:`typing.Generator[datamodelT]`
        """
        fields_dict = {field.name: field.type for field in dataclasses.fields(self)}  # type: ignore
        # print(fields_dict)

        for field_name, field_type in fields_dict.items():  # type: ignore
            try:
                if isinstance(getattr(self, field_name, None), TerraDataModel):
                    for sub_term in field_name.lower().split("_"):
                        if sub_term.lower() == term.lower():
                            yield typing.cast(DatamodelT, getattr(self, field_name, None))
                    # print(getattr(self, field_name , None))
                    typing.cast(DatamodelT, getattr(self, field_name, None)).filter_data(term)

            except Exception:
                try:
                    for sub_term in field_name.lower().split("_"):
                        if sub_term.lower() == term.lower():
                            yield typing.cast(DatamodelT, getattr(self, field_name, None))

                    for inner_item in typing.cast(typing.List[TerraDataModel], getattr(self, field_name, None)):
                        # print(inner_item)
                        inner_item.filter_data(term)

                except Exception:
                    # print(traceback.format_exc())
                    pass

    @classmethod
    def from_dict(
        cls: typing.Type[DatamodelT], model_dict: typing.Dict[str, typing.Any], safe: bool = True
    ) -> DatamodelT:
        """
        Return the Class data model representation of the dictionary (json).

        This method inspects the attributes of the class that it is being called on
        to determine how to build the correct payload from the data stored.

        Args:
            model_dict:obj:`dict`:
            safe:obj:`bool`:

        Returns:
            :obj:`terra.models.base_model.TerraDataModel`
        """
        # TODO - I don't like this function at all. It can definitely be more elegant
        data_model = cls()
        for k, v in model_dict.items():
            if (
                (inner_item := getattr(data_model, k, *(("NOT_FOUND",) if safe else ()))) in [None, []]
                or isinstance(inner_item, TerraDataModel)
                or isinstance(v, list)
                or (inner_item := getattr(data_model, k, *(("NOT_FOUND",) if safe else ()))) != v  # Added this
                # condition because the data model has a default status: warning and this condition allows it to
                # get overwritten
            ):
                if inner_item == "NOT_FOUND":
                    continue

                if isinstance(inner_item, TerraDataModel):
                    v = inner_item.from_dict(v)  # type: ignore

                # if it's a list
                if isinstance(v, list) and v:
                    # getting all the field types of the current class
                    fields_dict = {field.name: field.type for field in dataclasses.fields(cls())}  # type: ignore

                    # getting the current field type as a string and removing the 't.optional'
                    current_field_type = str(fields_dict[k]).split("[")[1].split("]")[0]
                    current_field_type2 = str(fields_dict[k]).split("[")[1].split("]")[0]

                    # adding terra before the models name
                    if current_field_type.split(".")[0] == "models":
                        current_field_type = "terra." + current_field_type

                    if current_field_type2.split(".")[0] == "models":
                        current_field_type2 = "terra-client." + current_field_type2

                    # check if the elements of the list are Terra Data Models
                    if current_field_type.split(".")[0] == "terra":
                        result = []

                        # for each json object inside the list
                        for inner_dict in v:  # type: ignore
                            # an instance of a data model of the type of items inside the list
                            inner_data_model = typing.cast(
                                typing.Type[TerraDataModel], pydoc.locate(current_field_type)
                            )()

                            # fill up the model
                            inner_data_model = inner_data_model.from_dict(inner_dict)  # type: ignore

                            # append the model to the result list
                            result.append(inner_data_model)  # type: ignore

                        v = result

                setattr(data_model, k, v)

        return data_model

    def populate_from_dict(
        self: DatamodelT, model_dict: typing.Dict[str, typing.Any], safe: bool = False
    ) -> DatamodelT:
        """
        Populates missing data fields in the class given a dictionary (json).

        This method inspects the attributes of the instance that it is being called on
        to determine how to build the correct payload from the data stored.

        Args:
            model_dict:obj:`dict`:
            safe:obj:`bool`:

        Returns:
            :obj:`terra.models.base_model.TerraDataModel`
        """
        for k, v in model_dict.items():
            if getattr(self, k, *(("NOT_FOUND",) if safe else ())) is None:
                setattr(self, k, v)

        return self
