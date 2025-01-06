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
from terra.models.v2 import activity
from terra.models.v2 import samples as samples_
from terra.models.v2.activity import OxygenData

__all__ = ["Body"]


@dataclasses.dataclass
class Metadata(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class ECGReading(base_model.TerraDataModel):
    start_timestamp: typing.Optional[str] = dataclasses.field(default=None)
    avg_hr_bpm: typing.Optional[float] = dataclasses.field(default=None)
    afib_classfication: typing.Optional[int] = dataclasses.field(default=None)
    raw_signal: typing.List[samples_.RawECGSample] = dataclasses.field(default_factory=list)


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
class MeasurementsData(base_model.TerraDataModel):
    measurements: typing.List[samples_.MeasurementDataSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class TemperatureData(base_model.TerraDataModel):
    ambient_temperature_samples: typing.List[samples_.TemperatureSample] = dataclasses.field(default_factory=list)
    body_temperature_samples: typing.List[samples_.TemperatureSample] = dataclasses.field(default_factory=list)
    skin_temperature_samples: typing.List[samples_.TemperatureSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class HydrationData(base_model.TerraDataModel):
    hydration_amount_samples: typing.List[samples_.HydrationMeasurementSample] = dataclasses.field(default_factory=list)
    day_total_water_consumption_ml: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class HeartData(base_model.TerraDataModel):
    heart_rate_data: activity.HeartRateData = dataclasses.field(default_factory=activity.HeartRateData)
    pulse_wave_velocity_samples: typing.List[samples_.PulseVelocitySample] = dataclasses.field(default_factory=list)
    afib_classification_samples: typing.List[samples_.AFibClassificationSample] = dataclasses.field(
        default_factory=list
    )
    ecg_signal: typing.List[ECGReading] = dataclasses.field(default_factory=list)
    rr_interval_samples: typing.List[samples_.RRIntervalSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class BloodPressureData(base_model.TerraDataModel):
    blood_pressure_samples: typing.List[samples_.BloodPressureSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class GlucoseData(base_model.TerraDataModel):
    day_avg_blood_glucose_mg_per_dL: typing.Optional[float] = dataclasses.field(default=None)
    blood_glucose_samples: typing.List[samples_.GlucoseDataSample] = dataclasses.field(default_factory=list)
    detailed_blood_glucose_samples: typing.List[samples_.GlucoseDataSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class KetoneData(base_model.TerraDataModel):
    ketone_samples: typing.List[samples_.KetoneDataSample] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Body(base_model.TerraDataModel):
    metadata: Metadata = dataclasses.field(default_factory=Metadata)
    measurements_data: MeasurementsData = dataclasses.field(default_factory=MeasurementsData)
    temperature_data: TemperatureData = dataclasses.field(default_factory=TemperatureData)
    hydration_data: HydrationData = dataclasses.field(default_factory=HydrationData)
    oxygen_data: OxygenData = dataclasses.field(default_factory=OxygenData)
    heart_data: HeartData = dataclasses.field(default_factory=HeartData)
    blood_pressure_data: BloodPressureData = dataclasses.field(default_factory=BloodPressureData)
    glucose_data: GlucoseData = dataclasses.field(default_factory=GlucoseData)
    device_data: DeviceData = dataclasses.field(default_factory=DeviceData)
    ketone_data: KetoneData = dataclasses.field(default_factory=KetoneData)
