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
from terra.models.v2.samples import DrinkSample

__all__ = ["Nutrition"]


@dataclasses.dataclass
class Metadata(base_model.TerraDataModel):
    start_time: typing.Optional[str] = dataclasses.field(default=None)
    end_time: typing.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class Macros(base_model.TerraDataModel):
    calories: typing.Optional[float] = dataclasses.field(default=None)
    protein_g: typing.Optional[float] = dataclasses.field(default=None)
    carbohydrates_g: typing.Optional[float] = dataclasses.field(default=None)
    fat_g: typing.Optional[float] = dataclasses.field(default=None)
    trans_fat_g: typing.Optional[float] = dataclasses.field(default=None)
    saturated_fat_g: typing.Optional[float] = dataclasses.field(default=None)
    sugar_g: typing.Optional[float] = dataclasses.field(default=None)
    cholesterol_mg: typing.Optional[float] = dataclasses.field(default=None)
    fiber_g: typing.Optional[float] = dataclasses.field(default=None)
    sodium_mg: typing.Optional[float] = dataclasses.field(default=None)
    alcohol_g: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class Micros(base_model.TerraDataModel):
    biotin_mg: typing.Optional[float] = dataclasses.field(default=None)
    caffeine_mg: typing.Optional[float] = dataclasses.field(default=None)
    chloride_mg: typing.Optional[float] = dataclasses.field(default=None)
    chromium_mg: typing.Optional[float] = dataclasses.field(default=None)
    copper_mg: typing.Optional[float] = dataclasses.field(default=None)
    calcium_mg: typing.Optional[float] = dataclasses.field(default=None)
    folate_mg: typing.Optional[float] = dataclasses.field(default=None)
    folic_acid_mg: typing.Optional[float] = dataclasses.field(default=None)
    iodine_mg: typing.Optional[float] = dataclasses.field(default=None)
    iron_mg: typing.Optional[float] = dataclasses.field(default=None)
    magnesium_mg: typing.Optional[float] = dataclasses.field(default=None)
    manganese_mg: typing.Optional[float] = dataclasses.field(default=None)
    molybdenum_mg: typing.Optional[float] = dataclasses.field(default=None)
    monounsaturated_fat_g: typing.Optional[float] = dataclasses.field(default=None)
    niacin_mg: typing.Optional[float] = dataclasses.field(default=None)
    pantothenic_acid_mg: typing.Optional[float] = dataclasses.field(default=None)
    phosphorus_mg: typing.Optional[float] = dataclasses.field(default=None)
    polyunsaturated_fat_g: typing.Optional[float] = dataclasses.field(default=None)
    potassium_mg: typing.Optional[float] = dataclasses.field(default=None)
    riboflavin_mg: typing.Optional[float] = dataclasses.field(default=None)
    selenium_mg: typing.Optional[float] = dataclasses.field(default=None)
    thiamin_mg: typing.Optional[float] = dataclasses.field(default=None)
    vitamin_A_mg: typing.Optional[float] = dataclasses.field(default=None)
    vitamin_B12_mg: typing.Optional[float] = dataclasses.field(default=None)
    vitamin_B6_mg: typing.Optional[float] = dataclasses.field(default=None)
    vitamin_C_mg: typing.Optional[float] = dataclasses.field(default=None)
    vitamin_D_mg: typing.Optional[float] = dataclasses.field(default=None)
    vitamin_E_mg: typing.Optional[float] = dataclasses.field(default=None)
    vitamin_K_mg: typing.Optional[float] = dataclasses.field(default=None)
    zinc_mg: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class Quantity(base_model.TerraDataModel):
    unit: typing.Optional[int] = dataclasses.field(default=None)
    amount: typing.Optional[float] = dataclasses.field(default=None)


@dataclasses.dataclass
class Meal(base_model.TerraDataModel):
    name: typing.Optional[str] = dataclasses.field(default=None)
    id: typing.Optional[str] = dataclasses.field(default=None)
    timestamp: typing.Optional[str] = dataclasses.field(default=None)
    type: typing.Optional[int] = dataclasses.field(default=0)
    quantity: Quantity = dataclasses.field(default_factory=Quantity)
    macros: Macros = dataclasses.field(default_factory=Macros)
    micros: Micros = dataclasses.field(default_factory=Micros)


@dataclasses.dataclass
class NutritionSummary(base_model.TerraDataModel):
    water_ml: typing.Optional[float] = dataclasses.field(default=None)
    macros: Macros = dataclasses.field(default_factory=Macros)
    drink_ml: typing.Optional[float] = dataclasses.field(default=None)
    micros: Micros = dataclasses.field(default_factory=Micros)


@dataclasses.dataclass
class Nutrition(base_model.TerraDataModel):
    metadata: Metadata = dataclasses.field(default_factory=Metadata)
    summary: NutritionSummary = dataclasses.field(default_factory=NutritionSummary)
    meals: typing.List[Meal] = dataclasses.field(default_factory=list)
    drink_samples: typing.List[DrinkSample] = dataclasses.field(default_factory=list)
