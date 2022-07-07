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
import dataclasses
import typing

from terra.models import base_model
from terra.models import user as user_

__all__ = ["Athlete", "AthleteCollection"]


@dataclasses.dataclass
class Athlete(base_model.TerraDataModel):
    first_name: typing.Optional[str] = dataclasses.field(default=None)
    last_name: typing.Optional[str] = dataclasses.field(default=None)
    gender: typing.Optional[str] = dataclasses.field(default=None)
    sex: typing.Optional[str] = dataclasses.field(default=None)
    age: typing.Optional[int] = dataclasses.field(default=None)
    date_of_birth: typing.Optional[str] = dataclasses.field(default=None)
    bio: typing.Optional[str] = dataclasses.field(default=None)
    email: typing.Optional[str] = dataclasses.field(default=None)
    city: typing.Optional[str] = dataclasses.field(default=None)
    state: typing.Optional[str] = dataclasses.field(default=None)
    country: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class AthleteCollection(base_model.TerraDataModel):
    user: user_.User = dataclasses.field()
    athlete: Athlete = dataclasses.field()
    type: typing.Optional[str] = dataclasses.field(default=None)
