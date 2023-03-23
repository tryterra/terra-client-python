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

__all__ = ["Activity"]


@dataclasses.dataclass
class Metadata(base_model.TerraDataModel):
    name: typing.Optional[str] = dataclasses.field(default=None)
    type: typing.Optional[int] = dataclasses.field(default=None)
    summary_id: typing.Optional[str] = dataclasses.field(default=None)
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)
    city: typing.Optional[str] = dataclasses.field(default=None)
    state: typing.Optional[str] = dataclasses.field(default=None)
    country: typing.Optional[str] = dataclasses.field(default=None)
    upload_type: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class LapData(base_model.TerraDataModel):
    laps: typing.List[samples_.LapSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class StrainData(base_model.TerraDataModel):
    strain_level: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class SwimmingSummary(base_model.TerraDataModel):
    num_laps: typing.Optional[int] = dataclasses.field(default=None)
    num_strokes: typing.Optional[int] = dataclasses.field(default=None)
    pool_length_meters: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class ElevationSummary(base_model.TerraDataModel):
    gain_planned_meters: typing.Optional[float] = dataclasses.field(default=None)
    gain_actual_meters: typing.Optional[float] = dataclasses.field(default=None)
    loss_actual_meters: typing.Optional[float] = dataclasses.field(default=None)
    min_meters: typing.Optional[float] = dataclasses.field(default=None)
    avg_meters: typing.Optional[float] = dataclasses.field(default=None)
    max_meters: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class DistanceDataSummary(base_model.TerraDataModel):
    distance_meters: typing.Optional[float] = dataclasses.field(default=None)
    steps: typing.Optional[int] = dataclasses.field(default=None)
    floors_climbed: typing.Optional[int] = dataclasses.field(default=None)
    swimming: SwimmingSummary = dataclasses.field(default_factory=SwimmingSummary)
    elevation: ElevationSummary = dataclasses.field(default_factory=ElevationSummary)


@dataclasses.dataclass
class DistanceDataDetailed(base_model.TerraDataModel):
    step_samples: typing.List[samples_.StepSample] = dataclasses.field(default_factory=list)
    distance_samples: typing.List[samples_.DistanceSample] = dataclasses.field(default_factory=list)
    elevation_samples: typing.List[samples_.ElevationSample] = dataclasses.field(default_factory=list)
    floors_climbed_samples: typing.List[samples_.FloorsClimbedSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class DistanceData(base_model.TerraDataModel):
    summary: DistanceDataSummary = dataclasses.field(default_factory=DistanceDataSummary)
    detailed: DistanceDataDetailed = dataclasses.field(default_factory=DistanceDataDetailed)


@dataclasses.dataclass
class PositionData(base_model.TerraDataModel):
    start_pos_lat_lng_deg: typing.List[float] = dataclasses.field(default_factory=list)
    center_pos_lat_lng_deg: typing.List[float] = dataclasses.field(default_factory=list)
    end_pos_lat_lng_deg: typing.List[float] = dataclasses.field(default_factory=list)
    position_samples: typing.List[samples_.PositionSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ActiveDurationsData(base_model.TerraDataModel):
    activity_seconds: typing.Optional[float] = dataclasses.field(default=None)
    inactivity_seconds: typing.Optional[float] = dataclasses.field(default=None)
    rest_seconds: typing.Optional[float] = dataclasses.field(default=None)
    low_intensity_seconds: typing.Optional[float] = dataclasses.field(default=None)
    moderate_intensity_seconds: typing.Optional[float] = dataclasses.field(default=None)
    vigorous_intensity_seconds: typing.Optional[float] = dataclasses.field(default=None)
    num_continuous_inactive_periods: typing.Optional[int] = dataclasses.field(default=None)
    activity_levels_samples: typing.List[samples_.ActivityLevelSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class METData(base_model.TerraDataModel):
    avg_level: typing.Optional[float] = dataclasses.field(default=None)
    num_inactive_minutes: typing.Optional[float] = dataclasses.field(default=None)
    num_low_intensity_minutes: typing.Optional[float] = dataclasses.field(default=None)
    num_moderate_intensity_minutes: typing.Optional[float] = dataclasses.field(default=None)
    num_high_intensity_minutes: typing.Optional[float] = dataclasses.field(default=None)
    MET_samples: typing.List[samples_.METSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class MovementData(base_model.TerraDataModel):
    avg_speed_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)
    max_speed_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)
    adjusted_max_speed_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)
    normalized_speed_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)
    avg_pace_minutes_per_kilometer: typing.Optional[float] = dataclasses.field(default=None)
    max_pace_minutes_per_kilometer: typing.Optional[float] = dataclasses.field(default=None)
    avg_velocity_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)
    max_velocity_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)
    avg_cadence_rpm: typing.Optional[float] = dataclasses.field(default=None)
    max_cadence_rpm: typing.Optional[float] = dataclasses.field(default=None)
    avg_torque_newton_meters: typing.Optional[float] = dataclasses.field(default=None)
    max_torque_newton_meters: typing.Optional[float] = dataclasses.field(default=None)
    cadence_samples: typing.List[samples_.CadenceSample] = dataclasses.field(default_factory=list)
    speed_samples: typing.List[samples_.SpeedSample] = dataclasses.field(default_factory=list)
    torque_samples: typing.List[samples_.TorqueSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class CaloriesData(base_model.TerraDataModel):
    net_activity_calories: typing.Optional[float] = dataclasses.field(default=None)
    BMR_calories: typing.Optional[float] = dataclasses.field(default=None)
    total_burned_calories: typing.Optional[float] = dataclasses.field(default=None)
    net_intake_calories: typing.Optional[float] = dataclasses.field(default=None)
    calorie_samples: typing.List[samples_.CalorieSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class WorkData(base_model.TerraDataModel):
    work_kilojoules: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class PowerData(base_model.TerraDataModel):
    avg_watts: typing.Optional[float] = dataclasses.field(default=None)
    max_watts: typing.Optional[float] = dataclasses.field(default=None)
    power_samples: typing.List[samples_.PowerSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class EnergyData(base_model.TerraDataModel):
    energy_kilojoules: typing.Optional[float] = dataclasses.field(default=None)
    energy_planned_kilojoules: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class TSSData(base_model.TerraDataModel):
    TSS_samples: typing.List[samples_.TSSSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class HeartRateZone(base_model.TerraDataModel):
    zone: typing.Optional[int] = dataclasses.field(default=None)
    start_percentage: typing.Optional[float] = dataclasses.field(default=None)
    end_percentage: typing.Optional[float] = dataclasses.field(default=None)
    name: typing.Optional[str] = dataclasses.field(default=None)
    duration_seconds: typing.Optional[float] = dataclasses.field(default=None)

    def __post_init__(self) -> None:
        if not any((self.start_percentage, self.end_percentage, self.name)):
            self.start_percentage, self.end_percentage, self.name = (None, None, None)


@dataclasses.dataclass
class HeartRateDataSummary(base_model.TerraDataModel):
    avg_hr_bpm: typing.Optional[float] = dataclasses.field(default=None)
    max_hr_bpm: typing.Optional[float] = dataclasses.field(default=None)
    min_hr_bpm: typing.Optional[float] = dataclasses.field(default=None)
    avg_hrv_rmssd: typing.Optional[float] = dataclasses.field(default=None)
    avg_hrv_sdnn: typing.Optional[float] = dataclasses.field(default=None)
    user_max_hr_bpm: typing.Optional[float] = dataclasses.field(default=None)
    resting_hr_bpm: typing.Optional[float] = dataclasses.field(default=None)
    hr_zone_data: typing.List[HeartRateZone] = dataclasses.field(default_factory=list)


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
class OxygenData(base_model.TerraDataModel):
    vo2max_ml_per_min_per_kg: typing.Optional[float] = dataclasses.field(default=None)
    avg_saturation_percentage: typing.Optional[float] = dataclasses.field(default=None)
    saturation_samples: typing.List[samples_.OxygenSaturationSample] = dataclasses.field(default_factory=list)
    vo2_samples: typing.List[samples_.Vo2MaxSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class PolylineMapData(base_model.TerraDataModel):
    summary_polyline: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class DeviceData(base_model.TerraDataModel):
    name: typing.Optional[str] = dataclasses.field(default=None)
    activation_timestamp: typing.Optional[str] = dataclasses.field(default=None)
    manufacturer: typing.Optional[str] = dataclasses.field(default=None)
    serial_number: typing.Optional[str] = dataclasses.field(default=None)
    software_version: typing.Optional[str] = dataclasses.field(default=None)
    hardware_version: typing.Optional[str] = dataclasses.field(default=None)
    other_devices: typing.List[samples_.OtherDeviceData] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Activity(base_model.TerraDataModel):
    metadata: Metadata = dataclasses.field(default_factory=Metadata)
    lap_data: LapData = dataclasses.field(default_factory=LapData)
    distance_data: DistanceData = dataclasses.field(default_factory=DistanceData)
    position_data: PositionData = dataclasses.field(default_factory=PositionData)
    active_durations_data: ActiveDurationsData = dataclasses.field(default_factory=ActiveDurationsData)
    MET_data: METData = dataclasses.field(default_factory=METData)
    movement_data: MovementData = dataclasses.field(default_factory=MovementData)
    calories_data: CaloriesData = dataclasses.field(default_factory=CaloriesData)
    work_data: WorkData = dataclasses.field(default_factory=WorkData)
    power_data: PowerData = dataclasses.field(default_factory=PowerData)
    energy_data: EnergyData = dataclasses.field(default_factory=EnergyData)
    TSS_data: TSSData = dataclasses.field(default_factory=TSSData)
    heart_rate_data: HeartRateData = dataclasses.field(default_factory=HeartRateData)
    strain_data: StrainData = dataclasses.field(default_factory=StrainData)
    oxygen_data: OxygenData = dataclasses.field(default_factory=OxygenData)
    polyline_map_data: PolylineMapData = dataclasses.field(default_factory=PolylineMapData)
    device_data: DeviceData = dataclasses.field(default_factory=DeviceData)
    cheat_detection: typing.Optional[float] = dataclasses.field(default=None)
