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
from terra.models.v2.activity import DeviceData

__all__ = [
    "BreathsData",
    "HeartRateData",
    "HeartRateDataDetailed",
    "HeartRateDataSummary",
    "Metadata",
    "OxygenSaturationData",
    "ReadinessData",
    "RespirationData",
    "Sleep",
    "SleepDurationsAsleepData",
    "SleepDurationsAwakeData",
    "SleepDurationsData",
    "SleepDurationsOtherData",
    "SnoringData",
    "TemperatureData",
]


@dataclasses.dataclass
class Metadata(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)
    upload_type: typing.Optional[int] = dataclasses.field(default=None)
    is_nap: bool = dataclasses.field(default=False)


@dataclasses.dataclass
class ReadinessData(base_model.TerraDataModel):
    readiness: typing.Optional[float] = dataclasses.field(default=None)
    recovery_level: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class TemperatureData(base_model.TerraDataModel):
    delta: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class HeartRateDataSummary(base_model.TerraDataModel):
    avg_hr_bpm: typing.Optional[int] = dataclasses.field(default=None)
    max_hr_bpm: typing.Optional[int] = dataclasses.field(default=None)
    min_hr_bpm: typing.Optional[int] = dataclasses.field(default=None)
    avg_hrv_rmssd: typing.Optional[int] = dataclasses.field(default=None)
    avg_hrv_sdnn: typing.Optional[int] = dataclasses.field(default=None)
    user_max_hr_bpm: typing.Optional[int] = dataclasses.field(default=None)
    resting_hr_bpm: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class HeartRateDataDetailed(base_model.TerraDataModel):
    hr_samples: typing.List[samples_.HeartRateDataSample] = dataclasses.field(default_factory=list)
    hrv_samples_rmssd: typing.List[samples_.HeartRateVariabilityDataSampleRMSSD] = dataclasses.field(
        default_factory=list
    )
    hrv_samples_sdnn: typing.List[samples_.HeartRateVariabilityDataSampleSDNN] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class HeartRateData(base_model.TerraDataModel):
    summary: HeartRateDataSummary = dataclasses.field(default_factory=HeartRateDataSummary)
    detailed: HeartRateDataDetailed = dataclasses.field(default_factory=HeartRateDataDetailed)


@dataclasses.dataclass
class SleepDurationsAwakeData(base_model.TerraDataModel):
    sleep_latency_seconds: typing.Optional[float] = dataclasses.field(default=None)
    wake_up_latency_seconds: typing.Optional[float] = dataclasses.field(default=None)
    duration_awake_state_seconds: typing.Optional[float] = dataclasses.field(default=None)
    duration_short_interruption_seconds: typing.Optional[float] = dataclasses.field(default=None)
    duration_long_interruption_seconds: typing.Optional[float] = dataclasses.field(default=None)
    num_out_of_bed_events: typing.Optional[int] = dataclasses.field(default=None)
    num_wakeup_events: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class SleepDurationsAsleepData(base_model.TerraDataModel):
    duration_asleep_state_seconds: typing.Optional[float] = dataclasses.field(default=None)
    duration_deep_sleep_state_seconds: typing.Optional[float] = dataclasses.field(default=None)
    duration_light_sleep_state_seconds: typing.Optional[float] = dataclasses.field(default=None)
    duration_REM_sleep_state_seconds: typing.Optional[float] = dataclasses.field(default=None)
    num_REM_events: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class SleepDurationsOtherData(base_model.TerraDataModel):
    duration_unmeasurable_sleep_seconds: typing.Optional[float] = dataclasses.field(default=None)
    duration_in_bed_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class SleepDurationsData(base_model.TerraDataModel):
    sleep_efficiency: typing.Optional[float] = dataclasses.field(default=None)
    awake: SleepDurationsAwakeData = dataclasses.field(default_factory=SleepDurationsAwakeData)
    asleep: SleepDurationsAsleepData = dataclasses.field(default_factory=SleepDurationsAsleepData)
    other: SleepDurationsOtherData = dataclasses.field(default_factory=SleepDurationsOtherData)
    hypnogram_samples: typing.List[samples_.SleepHypnogramSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class OxygenSaturationData(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)
    avg_saturation_percentage: typing.Optional[float] = dataclasses.field(default=None)
    samples: typing.List[samples_.OxygenSaturationSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class BreathsData(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)
    on_demand_reading: typing.Optional[bool] = dataclasses.field(default=None)
    avg_breaths_per_min: typing.Optional[float] = dataclasses.field(default=None)
    max_breaths_per_min: typing.Optional[float] = dataclasses.field(default=None)
    min_breaths_per_min: typing.Optional[float] = dataclasses.field(default=None)
    samples: typing.List[samples_.BreathSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class SnoringData(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)
    total_snoring_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)
    num_snoring_events: typing.Optional[int] = dataclasses.field(default=None)
    samples: typing.List[samples_.SnoringSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class RespirationData(base_model.TerraDataModel):
    oxygen_saturation_data: OxygenSaturationData = dataclasses.field(default_factory=OxygenSaturationData)
    breaths_data: BreathsData = dataclasses.field(default_factory=BreathsData)
    snoring_data: SnoringData = dataclasses.field(default_factory=SnoringData)


@dataclasses.dataclass
class Sleep(base_model.TerraDataModel):
    metadata: Metadata = dataclasses.field(default_factory=Metadata)
    temperature_data: TemperatureData = dataclasses.field(default_factory=TemperatureData)
    readiness_data: ReadinessData = dataclasses.field(default_factory=ReadinessData)
    heart_rate_data: HeartRateData = dataclasses.field(default_factory=HeartRateData)
    sleep_durations_data: SleepDurationsData = dataclasses.field(default_factory=SleepDurationsData)
    respiration_data: RespirationData = dataclasses.field(default_factory=RespirationData)
    device_data: DeviceData = dataclasses.field(default_factory=DeviceData)
