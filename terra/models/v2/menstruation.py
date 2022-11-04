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
from terra.models.v2 import samples as samples_

__all__ = ["Menstruation"]


@dataclasses.dataclass
class Metadata(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class MenstruationData(base_model.TerraDataModel):
    period_start_date: typing.Optional[str] = dataclasses.field(default=None)
    day_in_cycle: typing.Optional[int] = dataclasses.field(default=None)
    period_length_days: typing.Optional[int] = dataclasses.field(default=None)
    current_phase: typing.Optional[int] = dataclasses.field(default=None)
    length_of_current_phase_days: typing.Optional[int] = dataclasses.field(default=None)
    days_until_next_phase: typing.Optional[int] = dataclasses.field(default=None)
    predicted_cycle_length_days: typing.Optional[int] = dataclasses.field(default=None)
    is_predicted_cycle: typing.Optional[str] = dataclasses.field(default=None)
    cycle_length_days: typing.Optional[str] = dataclasses.field(default=None)
    last_updated_time: typing.Optional[str] = dataclasses.field(default=None)
    menstruation_flow: typing.List[samples_.MenstruationFlowSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Menstruation(base_model.TerraDataModel):
    metadata: Metadata = dataclasses.field(default_factory=Metadata)
    menstruation_data: MenstruationData = dataclasses.field(default_factory=MenstruationData)
