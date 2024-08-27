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
from terra.models.v2.activity import ActiveDurationsData
from terra.models.v2.activity import CaloriesData
from terra.models.v2.activity import DeviceData
from terra.models.v2.activity import ElevationSummary
from terra.models.v2.activity import HeartRateData
from terra.models.v2.activity import METData
from terra.models.v2.activity import OxygenData
from terra.models.v2.activity import SwimmingSummary

__all__ = ["Daily"]


@dataclasses.dataclass
class Metadata(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)
    upload_type: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class DistanceDataDetailed(base_model.TerraDataModel):
    step_samples: typing.List[samples_.StepSample] = dataclasses.field(default_factory=list)
    distance_samples: typing.List[samples_.DistanceSample] = dataclasses.field(default_factory=list)
    elevation_samples: typing.List[samples_.ElevationSample] = dataclasses.field(default_factory=list)
    floors_climbed_samples: typing.List[samples_.FloorsClimbedSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class StrainData(base_model.TerraDataModel):
    strain_level: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class DistanceData(base_model.TerraDataModel):
    distance_meters: typing.Optional[float] = dataclasses.field(default=None)
    steps: typing.Optional[int] = dataclasses.field(default=None)
    floors_climbed: typing.Optional[int] = dataclasses.field(default=None)
    swimming: SwimmingSummary = dataclasses.field(default_factory=SwimmingSummary)
    elevation: ElevationSummary = dataclasses.field(default_factory=ElevationSummary)
    detailed: DistanceDataDetailed = dataclasses.field(default_factory=DistanceDataDetailed)


@dataclasses.dataclass
class TagEntry(base_model.TerraDataModel):
    tag_name: typing.Optional[str] = dataclasses.field(default=None)
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    notes: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class TagData(base_model.TerraDataModel):
    tags: typing.List[TagEntry] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class StressData(base_model.TerraDataModel):
    stress_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)
    rest_stress_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)
    activity_stress_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)
    low_stress_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)
    medium_stress_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)
    high_stress_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)
    avg_stress_level: typing.Optional[float] = dataclasses.field(default=None)
    max_stress_level: typing.Optional[float] = dataclasses.field(default=None)
    samples: typing.List[samples_.StressSample] = dataclasses.field(default_factory=list)
    body_battery_samples: typing.List[samples_.BodyBatterySample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Scores(base_model.TerraDataModel):
    recovery: typing.Optional[float] = dataclasses.field(default=None)
    activity: typing.Optional[float] = dataclasses.field(default=None)
    sleep: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class Daily(base_model.TerraDataModel):
    metadata: Metadata = dataclasses.field(default_factory=Metadata)
    tag_data: TagData = dataclasses.field(default_factory=TagData)
    active_durations_data: ActiveDurationsData = dataclasses.field(default_factory=ActiveDurationsData)
    distance_data: DistanceData = dataclasses.field(default_factory=DistanceData)
    heart_rate_data: HeartRateData = dataclasses.field(default_factory=HeartRateData)
    calories_data: CaloriesData = dataclasses.field(default_factory=CaloriesData)
    MET_data: METData = dataclasses.field(default_factory=METData)
    stress_data: StressData = dataclasses.field(default_factory=StressData)
    oxygen_data: OxygenData = dataclasses.field(default_factory=OxygenData)
    strain_data: StrainData = dataclasses.field(default_factory=StrainData)
    device_data: DeviceData = dataclasses.field(default_factory=DeviceData)
    scores: Scores = dataclasses.field(default_factory=Scores)
