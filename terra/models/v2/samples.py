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

__all__ = [
    "AFibClassificationSample",
    "ActivityLevelSample",
    "AmbientTemperatureSample",
    "BloodPressureSample",
    "BodyBatterySample",
    "BodyTemperatureSample",
    "BreathSample",
    "CadenceSample",
    "DistanceSample",
    "DrinkSample",
    "ElevationSample",
    "GlucoseDataSample",
    "HeartRateDataSample",
    "HeartRateVariabilityDataSampleRMSSD",
    "HeartRateVariabilityDataSampleSDNN",
    "HydrationMeasurementSample",
    "LapSample",
    "METSample",
    "MeasurementDataSample",
    "OtherDeviceData",
    "OxygenSaturationSample",
    "PositionSample",
    "PowerSample",
    "PulseVelocitySample",
    "RRIntervalSample",
    "SkinTemperatureSample",
    "SleepHypnogramSample",
    "SnoringSample",
    "SpeedSample",
    "StepSample",
    "StressSample",
    "TSSSample",
    "TemperatureSample",
    "Vo2MaxSample",
]


@dataclasses.dataclass
class GlucoseDataSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    blood_glucose_mg_per_dL: typing.Optional[int] = dataclasses.field(default=None)
    glucose_level_flag: typing.Optional[int] = dataclasses.field(default=None)
    trend_arrow: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class KetoneDataSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    ketone_mg_per_dL: typing.Optional[float] = dataclasses.field(default=None)
    sample_type: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class RawECGSample(base_model.TerraDataModel):
    potential_uV: typing.Optional[float] = dataclasses.field(default=None)
    timestamp: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class HeartRateDataSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    bpm: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)
    context: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class LapSample(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)
    distance_meters: typing.Optional[float] = dataclasses.field(default=None)
    calories: typing.Optional[float] = dataclasses.field(default=None)
    total_strokes: typing.Optional[float] = dataclasses.field(default=None)
    stroke_type: typing.Optional[str] = dataclasses.field(default=None)
    avg_hr_bpm: typing.Optional[str] = dataclasses.field(default=None)
    avg_speed_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class HeartRateVariabilityDataSampleRMSSD(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    hrv_rmssd: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class HeartRateVariabilityDataSampleSDNN(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    hrv_sdnn: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class DistanceSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    distance_meters: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class StepSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    steps: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class CalorieSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    calories: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class FloorsClimbedSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    floors_climbed: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class ElevationSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    elev_meters: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class PositionSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    coords_lat_lng_deg: typing.List[float] = dataclasses.field(default_factory=list)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class PowerSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    watts: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class TorqueSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    torque_newton_meters: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class SpeedSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    speed_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class CadenceSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    cadence_rpm: typing.Optional[float] = dataclasses.field(default=None)
    timer_duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class ActivityLevelSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    activity_level: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class METSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    level: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class TSSSample(base_model.TerraDataModel):
    planned: typing.Optional[float] = dataclasses.field(default=None)
    actual: typing.Optional[float] = dataclasses.field(default=None)
    method: typing.Optional[str] = dataclasses.field(default=None)
    intensity_factor_planned: typing.Optional[float] = dataclasses.field(default=None)
    intensity_factor_actual: typing.Optional[float] = dataclasses.field(default=None)
    normalized_power_watts: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class SleepHypnogramSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    level: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class OxygenSaturationSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    percentage: typing.Optional[float] = dataclasses.field(default=None)
    type: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class BreathSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    breaths_per_min: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class SnoringSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    duration_seconds: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class StressSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    level: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class BloodPressureSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    diastolic_bp: typing.Optional[float] = dataclasses.field(default=None)
    systolic_bp: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class MeasurementDataSample(base_model.TerraDataModel):
    """
    Represents a sample of body measurements, such as weight, height, and body composition.
    """

    measurement_time: typing.Optional[str] = dataclasses.field(default=None)
    """Time with which the record is associated, in ISO8601 format with microsecond precision. TimeZone info will be provided whenever possible. If absent, the time corresponds to the user's local time."""

    BMI: typing.Optional[float] = dataclasses.field(default=None)
    """User's Body Mass Index (BMI)."""

    BMR: typing.Optional[float] = dataclasses.field(default=None)
    """User's Basal Metabolic Rate - minimum amount of calories that a person's body needs to perform necessary functions."""

    RMR: typing.Optional[float] = dataclasses.field(default=None)
    """User's Resting Metabolic Rate - amount of energy that a person's body needs to function while at rest. RMR accounts for additional low-effort daily activities on top of basic body functions."""

    estimated_fitness_age: typing.Optional[str] = dataclasses.field(default=None)
    """Estimate of how fit the user is compared to their actual age, as measured by the device."""

    skin_fold_mm: typing.Optional[float] = dataclasses.field(default=None)
    """User's skin fold measurement."""

    bodyfat_percentage: typing.Optional[float] = dataclasses.field(default=None)
    """User's body fat percentage. Value between 0 and 100."""

    weight_kg: typing.Optional[float] = dataclasses.field(default=None)
    """User's body weight."""

    height_cm: typing.Optional[float] = dataclasses.field(default=None)
    """User's height."""

    bone_mass_g: typing.Optional[float] = dataclasses.field(default=None)
    """User's total bone mass."""

    muscle_mass_g: typing.Optional[float] = dataclasses.field(default=None)
    """User's total muscle mass (i.e. skeletal muscle mass)."""

    lean_mass_g: typing.Optional[float] = dataclasses.field(default=None)
    """Total lean mass of the user - calculated as the difference between total body weight and body fat weight."""

    water_percentage: typing.Optional[float] = dataclasses.field(default=None)
    """Total amount of fluid in the user's body. Value between 0.0 and 100.0."""

    insulin_units: typing.Optional[float] = dataclasses.field(default=None)
    """Quantity of insulin administered to the user."""

    insulin_type: typing.Optional[str] = dataclasses.field(default=None)
    """Type of insulin administered to the user."""

    urine_color: typing.Optional[str] = dataclasses.field(default=None)
    """Color of the user's urine."""

    user_notes: typing.Optional[str] = dataclasses.field(default=None)
    """User notes associated with the measurement."""


@dataclasses.dataclass
class BodyTemperatureSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    body_temperature_celsius: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class SkinTemperatureSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    skin_temperature_celsius: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class AmbientTemperatureSample(base_model.TerraDataModel):
    temperature_celsius: typing.Optional[float] = dataclasses.field(default=None)
    timestamp: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class TemperatureSample(base_model.TerraDataModel):
    temperature_celsius: typing.Optional[float] = dataclasses.field(default=None)
    timestamp: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class OtherDeviceData(base_model.TerraDataModel):
    name: typing.Optional[str] = dataclasses.field(default=None)
    manufacturer: typing.Optional[str] = dataclasses.field(default=None)
    serial_number: typing.Optional[str] = dataclasses.field(default=None)
    software_version: typing.Optional[str] = dataclasses.field(default=None)
    hardware_version: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class HydrationMeasurementSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    hydration_kg: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class Vo2MaxSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    vo2max_ml_per_min_per_kg: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class PulseVelocitySample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    pulse_wave_velocity_meters_per_second: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class AFibClassificationSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    afib_classification: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class DrinkSample(base_model.TerraDataModel):
    drink_unit: typing.Optional[str] = dataclasses.field(default=None)
    drink_volume: typing.Optional[str] = dataclasses.field(default=None)
    drink_name: typing.Optional[str] = dataclasses.field(default=None)
    timestamp: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class MenstruationFlowSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    flow: typing.Optional[int] = dataclasses.field(default=None)


@dataclasses.dataclass
class BodyBatterySample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    level: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class RRIntervalSample(base_model.TerraDataModel):
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    rr_interval_ms: typing.Optional[float] = dataclasses.field(default=None)
    hr_bpm: typing.Optional[float] = dataclasses.field(default=None)
