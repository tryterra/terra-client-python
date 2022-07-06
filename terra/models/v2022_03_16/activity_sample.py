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

__all__ = ["ActivitySample"]


@dataclasses.dataclass
class ActivitySample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    active_duration_seconds: typing.Optional[int] = dataclasses.field(default=None)
    altitude_in_meters: typing.Optional[float] = dataclasses.field(default=None)
    calories: typing.Optional[float] = dataclasses.field(default=None)
    distance_in_km: typing.Optional[float] = dataclasses.field(default=None)
    heartrate_bpm: typing.Optional[float] = dataclasses.field(default=None)
    coordinates_lat_lng: typing.List[float] = dataclasses.field(default_factory=list)
    rep_count: typing.Optional[int] = dataclasses.field(default=None)
    resting_duration_seconds: typing.Optional[int] = dataclasses.field(default=None)
    speed_in_meters_per_seconds: typing.Optional[float] = dataclasses.field(default=None)
    spo2_percentage: typing.Optional[float] = dataclasses.field(default=None)
    status: typing.Optional[str] = dataclasses.field(default=None)
    swimming_laps: typing.Optional[float] = dataclasses.field(default=None)
    swimming_strokes: typing.Optional[int] = dataclasses.field(default=None)
    vo2_volume_ml_per_min_per_kg: typing.Optional[float] = dataclasses.field(default=None)
    vo2_max_volume_ml_per_min_per_kg: typing.Optional[float] = dataclasses.field(default=None)
