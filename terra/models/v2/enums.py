from enum import Enum, IntEnum
from typing import Any, TypeVar

T = TypeVar('T', bound=Enum)


class ForwardCompatibleIntEnum(IntEnum):
    """Base class for forward-compatible integer enums that preserves unknown values."""

    @classmethod
    def _missing_(cls, value: Any):
        """Handle unknown values by creating a custom instance that preserves the raw value."""
        obj = int.__new__(cls, value)
        obj._name_ = f"UNKNOWN_{value}"
        obj._value_ = value
        # Store the original raw value
        obj.raw_value = value
        return obj

    @property
    def raw_value(self):
        """Get the raw integer value of this enum instance."""
        try:
            return self._raw_value
        except AttributeError:
            return self._value_

    @raw_value.setter
    def raw_value(self, value: Any):
        """Set the raw integer value for this enum instance."""
        self._raw_value = value


class ForwardCompatibleEnum(str, Enum):
    """Base class for forward-compatible string enums that preserves unknown values."""

    @classmethod
    def _missing_(cls, value: Any):
        """Handle unknown values by creating a custom instance that preserves the raw value."""
        if isinstance(value, str):
            # For string enums, create a new instance with the unknown string
            obj = str.__new__(cls, value)
            obj._name_ = f"UNKNOWN_{value}"
            obj._value_ = value
            obj.raw_value = value
            return obj
        return None

    @property
    def raw_value(self):
        """Get the raw string value of this enum instance."""
        try:
            return self._raw_value
        except AttributeError:
            return self._value_

    @raw_value.setter
    def raw_value(self, value: Any):
        """Set the raw string value for this enum instance."""
        self._raw_value = value


class ActivityType(ForwardCompatibleIntEnum):
    """The type of activity performed for the associated workout."""

    IN_VEHICLE = 0
    """Activity type for when the user is in a vehicle, such as a car or bus."""

    BIKING = 1
    """Activity type for general biking or cycling."""

    STILL = 3
    """Activity type for when the user is still or not moving."""

    UNKNOWN = 4
    """Activity type is unknown or could not be determined."""

    TILTING = 5
    """Activity type for when the device detects a tilting motion."""

    WALKING = 7
    """Activity type for general walking."""

    RUNNING = 8
    """Activity type for general running."""

    AEROBICS = 9
    """Activity type for aerobic exercises and workouts."""

    BADMINTON = 10
    """Activity type for playing badminton."""

    BASEBALL = 11
    """Activity type for playing baseball."""

    BASKETBALL = 12
    """Activity type for playing basketball."""

    BIATHLON = 13
    """Activity type for biathlon, combining cross-country skiing and rifle shooting."""

    HANDBIKING = 14
    """Activity type for hand biking, using a hand-powered bicycle."""

    MOUNTAIN_BIKING = 15
    """Activity type for off-road cycling on rough terrain."""

    ROAD_BIKING = 16
    """Activity type for cycling on paved roads."""

    SPINNING = 17
    """Activity type for indoor cycling classes or spinning."""

    STATIONARY_BIKING = 18
    """Activity type for exercising on a stationary bicycle."""

    UTILITY_BIKING = 19
    """Activity type for cycling for transportation or utility purposes."""

    BOXING = 20
    """Activity type for boxing training or matches."""

    CALISTHENICS = 21
    """Activity type for bodyweight exercises focusing on rhythm and flow."""

    CIRCUIT_TRAINING = 22
    """Activity type for workout consisting of a series of exercises performed in rotation."""

    CRICKET = 23
    """Activity type for playing cricket."""

    DANCING = 24
    """Activity type for various forms of dance."""

    ELLIPTICAL = 25
    """Activity type for exercising on an elliptical trainer."""

    FENCING = 26
    """Activity type for fencing sport."""

    AMERICAN_FOOTBALL = 27
    """Activity type for playing American football."""

    AUSTRALIAN_FOOTBALL = 28
    """Activity type for playing Australian rules football."""

    ENGLISH_FOOTBALL = 29
    """Activity type for playing soccer/football."""

    FRISBEE = 30
    """Activity type for playing frisbee or disc sports."""

    GARDENING = 31
    """Activity type for gardening and yard work."""

    GOLF = 32
    """Activity type for playing golf."""

    GYMNASTICS = 33
    """Activity type for performing gymnastics."""

    HANDBALL = 34
    """Activity type for playing handball."""

    HIKING = 35
    """Activity type for hiking or walking on trails."""

    HOCKEY = 36
    """Activity type for playing hockey."""

    HORSEBACK_RIDING = 37
    """Activity type for horseback riding."""

    HOUSEWORK = 38
    """Activity type for household chores and cleaning."""

    JUMPING_ROPE = 39
    """Activity type for skipping or jumping rope."""

    KAYAKING = 40
    """Activity type for kayaking on water."""

    KETTLEBELL_TRAINING = 41
    """Activity type for exercises using kettlebells."""

    KICKBOXING = 42
    """Activity type for kickboxing training or matches."""

    KITESURFING = 43
    """Activity type for kitesurfing or kiteboarding."""

    MARTIAL_ARTS = 44
    """Activity type for general martial arts training."""

    MEDITATION = 45
    """Activity type for meditation practice."""

    MIXED_MARTIAL_ARTS = 46
    """Activity type for MMA training or fighting."""

    P90X_EXERCISES = 47
    """Activity type for P90X home fitness program."""

    PARAGLIDING = 48
    """Activity type for paragliding sport."""

    PILATES = 49
    """Activity type for pilates exercises."""

    POLO = 50
    """Activity type for playing polo."""

    RACQUETBALL = 51
    """Activity type for playing racquetball."""

    ROCK_CLIMBING = 52
    """Activity type for rock climbing."""

    ROWING = 53
    """Activity type for rowing on water."""

    ROWING_MACHINE = 54
    """Activity type for exercising on a rowing machine."""

    RUGBY = 55
    """Activity type for playing rugby."""

    JOGGING = 56
    """Activity type for jogging at a leisurely pace."""

    RUNNING_ON_SAND = 57
    """Activity type for running on beach or sandy surface."""

    TREADMILL_RUNNING = 58
    """Activity type for running on a treadmill."""

    SAILING = 59
    """Activity type for sailing on water."""

    SCUBA_DIVING = 60
    """Activity type for scuba diving underwater."""

    SKATEBOARDING = 61
    """Activity type for skateboarding."""

    SKATING = 62
    """Activity type for general skating."""

    CROSS_SKATING = 63
    """Activity type for cross skating or nordic skating."""

    INDOOR_ROLLERBLADING = 64
    """Activity type for rollerblading indoors."""

    SKIING = 65
    """Activity type for general skiing."""

    BACK_COUNTRY_SKIING = 66
    """Activity type for backcountry or off-piste skiing."""

    CROSS_COUNTRY_SKIING = 67
    """Activity type for cross-country skiing."""

    DOWNHILL_SKIING = 68
    """Activity type for alpine or downhill skiing."""

    KITE_SKIING = 69
    """Activity type for skiing with a kite for propulsion."""

    ROLLER_SKIING = 70
    """Activity type for roller skiing on wheels."""

    SLEDDING = 71
    """Activity type for sledding or tobogganing."""

    SNOWBOARDING = 73
    """Activity type for snowboarding."""

    SNOWMOBILE = 74
    """Activity type for riding a snowmobile."""

    SNOWSHOEING = 75
    """Activity type for walking with snowshoes."""

    SQUASH = 76
    """Activity type for playing squash."""

    STAIR_CLIMBING = 77
    """Activity type for climbing stairs."""

    STAIR_CLIMBING_MACHINE = 78
    """Activity type for exercising on a stair climbing machine."""

    STAND_UP_PADDLEBOARDING = 79
    """Activity type for stand-up paddleboarding."""

    STRENGTH_TRAINING = 80
    """Activity type for resistance training or weight lifting."""

    SURFING = 81
    """Activity type for surfing on waves."""

    SWIMMING = 82
    """Activity type for general swimming."""

    SWIMMING_SWIMMING_POOL = 83
    """Activity type for swimming in a swimming pool."""

    SWIMMING_OPEN_WATER = 84
    """Activity type for swimming in open water like oceans, lakes or rivers."""

    TABLE_TENNIS = 85
    """Activity type for playing table tennis or ping pong."""

    TEAM_SPORTS = 86
    """Activity type for general team sports not otherwise classified."""

    TENNIS = 87
    """Activity type for playing tennis."""

    TREADMILL = 88
    """Activity type for exercising on a treadmill."""

    VOLLEYBALL = 89
    """Activity type for general volleyball."""

    VOLLEYBALL_BEACH = 90
    """Activity type for playing volleyball on a beach."""

    VOLLEYBALL_INDOOR = 91
    """Activity type for playing volleyball indoors."""

    WAKEBOARDING = 92
    """Activity type for wakeboarding on water."""

    WALKING_FITNESS = 93
    """Activity type for walking specifically for exercise."""

    NORDIC_WALKING = 94
    """Activity type for walking with poles."""

    WALKING_TREADMILL = 95
    """Activity type for walking on a treadmill."""

    WATERPOLO = 96
    """Activity type for playing water polo."""

    WEIGHTLIFTING = 97
    """Activity type for weightlifting exercises."""

    WHEELCHAIR = 98
    """Activity type for wheelchair-based movement."""

    WINDSURFING = 99
    """Activity type for windsurfing on water."""

    YOGA = 100
    """Activity type for practicing yoga."""

    ZUMBA = 101
    """Activity type for Zumba dance fitness."""

    DIVING = 102
    """Activity type for diving or jumping into water."""

    ERGOMETER = 103
    """Activity type for exercising on an ergometer."""

    ICE_SKATING = 104
    """Activity type for skating on ice."""

    INDOOR_SKATING = 105
    """Activity type for skating indoors."""

    CURLING = 106
    """Activity type for playing curling on ice."""

    OTHER = 108
    """Activity type for activities that don't fit into other categories."""

    CROSSFIT = 113
    """Activity type for CrossFit training."""

    HIIT = 114
    """Activity type for high-intensity interval training."""

    INTERVAL_TRAINING = 115
    """Activity type for general interval training workouts."""

    WALKING_STROLLER = 116
    """Activity type for walking while pushing a stroller."""

    ELEVATOR = 117
    """Activity type for riding in an elevator."""

    ESCALATOR = 118
    """Activity type for riding on an escalator."""

    ARCHERY = 119
    """Activity type for practicing archery."""

    SOFTBALL = 120
    """Activity type for playing softball."""

    GUIDED_BREATHING = 122
    """Activity type for practicing guided breathing exercises."""

    CARDIO_TRAINING = 123
    """Activity type for general cardiovascular exercise."""

    LACROSSE = 124
    """Activity type for playing lacrosse."""

    STRETCHING = 125
    """Activity type for stretching exercises."""

    TRIATHLON = 126
    """Activity type for triathlon events combining swimming, cycling and running."""

    INLINE_SKATING = 127
    """Activity type for inline skating or rollerblading."""

    SKY_DIVING = 128
    """Activity type for sky diving or parachuting."""

    PADDLING = 129
    """Activity type for general paddling activities."""

    MOUNTAINEERING = 130
    """Activity type for mountaineering or alpine climbing."""

    FISHING = 131
    """Activity type for fishing activities."""

    WATER_SKIING = 132
    """Activity type for water skiing."""

    INDOOR_RUNNING = 133
    """Activity type for running indoors."""

    PADEL_TENNIS = 134
    """Activity type for playing padel tennis."""

    DRIVING = 135
    """Activity type for driving a vehicle."""

    OFF_ROAD_DRIVING = 136
    """Activity type for driving off-road or on unpaved surfaces."""

    MOTORBIKING = 137
    """Activity type for riding a motorcycle."""

    MOTOR_RACING = 138
    """Activity type for motorsport racing."""

    ENDURO = 139
    """Activity type for enduro motorcycle racing."""

    CANOEING = 140
    """Activity type for canoeing on water."""

    ORIENTEERING = 141
    """Activity type for orienteering navigation sport."""

    HANG_GLIDING = 142
    """Activity type for hang gliding."""

    FLYING = 143
    """Activity type for piloting an aircraft."""

    HOT_AIR_BALLOONING = 144
    """Activity type for hot air balloon flying."""

    JET_SKIING = 145
    """Activity type for riding a jet ski on water."""

    POWER_BOATING = 146
    """Activity type for operating a motorized boat."""

    GAELIC_FOOTBALL = 147
    """Activity type for playing Gaelic football."""

    HURLING = 148
    """Activity type for playing hurling."""


class AFibFlag(ForwardCompatibleIntEnum):
    """Flag indicating the atrial fibrillation classification of the individual"""

    NEGATIVE = 0
    """AFib was not detected in the heart rhythm analysis."""

    POSITIVE = 1
    """AFib was detected in the heart rhythm analysis."""

    INCONCLUSIVE = 2
    """The heart rhythm analysis couldn't determine whether AFib was present or absent."""


class DeviceDataType(ForwardCompatibleEnum):
    """Represents data types that a certain device contributed to."""

    STEPS = "STEPS"
    """Count of steps taken by the user."""

    ACTIVE_MINUTES = "ACTIVE_MINUTES"
    """Duration of time the user spent in physical activity."""

    BMR = "BMR"
    """User's basal metabolic rate - calories burned at rest."""

    CALORIES = "CALORIES"
    """Calories burned by the user during activity."""

    DISTANCE = "DISTANCE"
    """Distance traveled by the user during activity."""

    HEART_RATE = "HEART_RATE"
    """User's heart rate measurements."""

    OXYGEN_SATURATION = "OXYGEN_SATURATION"
    """Blood oxygen saturation level (SpO2) of the user."""

    SLEEP_TYPE = "SLEEP_TYPE"
    """Classification of user's sleep stages or types."""

    SPEED = "SPEED"
    """User's movement speed during activity."""

    CADENCE = "CADENCE"
    """Rate of movement repetition during activity (steps per minute)."""


class ActivityLevel(ForwardCompatibleIntEnum):
    """Intensity of the user's activity at an instant in time"""

    UNKNOWN = 0
    """Activity level is unknown or could not be determined."""

    REST = 1
    """User is at rest, with minimal to no physical activity."""

    INACTIVE = 2
    """User is awake but inactive or sedentary."""

    LOW_INTENSITY = 3
    """User is engaged in light physical activity such as casual walking."""

    MEDIUM_INTENSITY = 4
    """User is engaged in moderate physical activity such as brisk walking or light exercise."""

    HIGH_INTENSITY = 5
    """User is engaged in vigorous physical activity such as running or intense exercise."""


class HeartRateZone(ForwardCompatibleIntEnum):
    """Represents the heart rate zone the user is currently in during a workout or activity"""

    ZONE_0 = 0
    """Resting heart rate zone."""

    ZONE_1 = 1
    """Very light activity zone."""

    ZONE_2 = 2
    """Light activity zone."""

    ZONE_3 = 3
    """Moderate activity zone."""

    ZONE_4 = 4
    """Hard activity zone."""

    ZONE_5 = 5
    """Maximum effort zone."""

    OTHER = 6
    """Heart rate zone that doesn't fit into the standard zones or couldn't be classified."""


class SleepLevel(ForwardCompatibleIntEnum):
    """Represents the sleep level of the user during a sleep session, indicating the depth and quality of sleep"""

    UNKNOWN = 0
    """Sleep level is unknown or could not be determined."""

    AWAKE = 1
    """User is awake during the sleep session."""

    SLEEPING = 2
    """User is in a general sleep state."""

    OUT_OF_BED = 3
    """User has left the bed during a sleep session."""

    LIGHT = 4
    """User is in light sleep stage."""

    DEEP = 5
    """User is in deep sleep stage."""

    REM = 6
    """User is in REM sleep stage."""


class UploadType(ForwardCompatibleIntEnum):
    """The type of upload for the associated workout, providing information on how the workout data was recorded or entered"""

    UNKNOWN = 0
    """The upload type is unknown or could not be determined."""

    AUTOMATIC = 1
    """The workout was automatically detected and recorded by a device or service."""

    MANUAL = 2
    """The workout was manually entered by the user."""

    UPDATE = 3
    """The workout data represents an update to a previously recorded workout."""

    DELETE = 4
    """The workout was marked for deletion."""

    PENDING = 5
    """The workout upload is pending processing or confirmation."""

    THIRD_PARTY_UPLOAD = 6
    """The workout was uploaded or synced from a third-party service or application."""


class SleepUploadType(ForwardCompatibleIntEnum):
    """The upload type for the associated workout, providing information on whether this was an automatic workout or user-entered"""

    UNKNOWN = 0
    """The sleep data upload type is unknown or could not be determined."""

    MANUAL = 1
    """The sleep data was manually entered by the user."""

    AUTOMATIC = 2
    """The sleep data was automatically detected and recorded by a device or service."""

    TENTATIVE = 3
    """The sleep data is preliminary or tentative and may be subject to change."""

    INDETERMINATE = 4
    """The sleep data upload type cannot be clearly categorized."""


class StrokeType(ForwardCompatibleEnum):
    """Stroke type used for the workout step (e.g. breaststroke)"""

    OTHER = "other"
    """Any swimming stroke style that doesn't fit the standard categories."""

    FREESTYLE = "freestyle"
    """Front crawl stroke where swimmers alternate arm movements with face in water."""

    BACKSTROKE = "backstroke"
    """Swimming stroke performed on the back with alternating arm movements."""

    BREASTSTROKE = "breaststroke"
    """Swimming stroke where arms move simultaneously in a heart-shaped pattern with a frog kick."""

    BUTTERFLY = "butterfly"
    """Swimming stroke with simultaneous overhead arm movements and dolphin kick."""


class GlucoseFlag(ForwardCompatibleIntEnum):
    """Flag indicating state of user's blood glucose level"""

    NORMAL = 0
    """Blood glucose level is within the normal/healthy range."""

    HIGH = 1
    """Blood glucose level is above the normal range (hyperglycemia)."""

    LOW = 2
    """Blood glucose level is below the normal range (hypoglycemia)."""


class NutritionUnits(ForwardCompatibleIntEnum):
    """Represents units used for nutrition measurements"""

    UNKNOWN = 0
    """The unit of measurement is unknown or not specified."""

    GRAM = 1
    """Measurement in grams, a metric unit of mass."""

    TEASPOON = 2
    """Measurement in teaspoons, approximately 5 milliliters."""

    TABLESPOON = 3
    """Measurement in tablespoons, approximately 15 milliliters."""

    CUP = 4
    """Measurement in cups, approximately 240 milliliters."""

    MEDIUM_EGG = 5
    """Quantity measured in medium-sized eggs."""

    LARGE_EGG = 6
    """Quantity measured in large-sized eggs."""

    SMALL_EGG = 7
    """Quantity measured in small-sized eggs."""

    MILLILITER = 8
    """Measurement in milliliters, a metric unit of volume."""

    OUNCE = 9
    """Measurement in ounces, approximately 28 grams."""

    COUNT = 10
    """Quantity measured by individual count or number of items."""

    SCOOP = 11
    """Quantity measured in scoops, typically used for protein powder or supplements."""

    FLUID_OUNCE = 12
    """Measurement in fluid ounces, approximately 30 milliliters."""


class RecoveryLevel(ForwardCompatibleIntEnum):
    """User's recovery score for a given day, resulting from the sleep session"""

    UNKNOWN = 0
    """Recovery level could not be determined or is not available."""

    VERY_POOR = 1
    """Extremely low recovery."""

    POOR = 2
    """Low recovery level."""

    COMPROMISED = 3
    """Below average recovery."""

    OK = 4
    """Moderate recovery level."""

    GOOD = 5
    """Above average recovery."""

    VERY_GOOD = 6
    """Excellent recovery level."""


class TrendArrow(ForwardCompatibleIntEnum):
    """Flag indicating the current trend in the user's blood glucose level (e.g. rising, constant, falling)"""

    UNKNOWN = 0
    """Glucose trend cannot be determined."""

    FALLING_QUICKLY = 1
    """Glucose level is decreasing rapidly."""

    FALLING = 2
    """Glucose level is decreasing gradually."""

    FLAT = 3
    """Glucose level is remaining stable."""

    RISING = 4
    """Glucose level is increasing gradually."""

    RISING_QUICKLY = 5
    """Glucose level is increasing rapidly."""


class MenstruationFlow(ForwardCompatibleIntEnum):
    """Flag indicating the strength of the user's menstrual flow"""

    UNKNOWN = 0
    """Flow status is unknown or not recorded."""

    NONE = 1
    """No menstrual flow present."""

    LIGHT = 2
    """Light menstrual flow."""

    MEDIUM = 3
    """Moderate menstrual flow."""

    HEAVY = 4
    """Heavy menstrual flow."""

    HAD = 5
    """Menstrual flow occurred but intensity not specified."""


class MealType(ForwardCompatibleIntEnum):
    """Enum representing the category the consumed food/meal falls under (i.e. Breakfast/Lunch/Dinner etc)"""

    UNKNOWN = 0
    """Meal type is unknown or could not be determined."""

    BREAKFAST = 1
    """Meal consumed in the morning, typically the first meal of the day."""

    MORNING_SNACK = 2
    """Light meal or snack consumed in the morning, between breakfast and lunch."""

    LUNCH = 3
    """Meal consumed around midday, typically the second meal of the day."""

    AFTERNOON_SNACK = 4
    """Light meal or snack consumed in the afternoon, between lunch and dinner."""

    DINNER = 5
    """Meal consumed in the evening, typically the last main meal of the day."""

    SNACK = 6
    """Any light meal or snack consumed at any time, not fitting into main meal categories."""


class StressLevel(ForwardCompatibleIntEnum):
    """Represents stress level ranges."""

    UNKNOWN = 0
    """Stress level is unknown or could not be determined."""

    REST = 1
    """Very low stress level (range 1-25)."""

    LOW = 2
    """Low stress level (range 26-50)."""

    MEDIUM = 3
    """Moderate stress level (range 51-75)."""

    HIGH = 4
    """High stress level (range 76-100)."""


class HeartRateContext(ForwardCompatibleIntEnum):
    """Represents the context in which heart rate was measured."""

    NOT_SET = 0
    """Heart rate measurement context is not specified."""

    ACTIVE = 1
    """Heart rate was measured during physical activity or exercise."""

    NOT_ACTIVE = 2
    """Heart rate was measured during rest or non-active periods."""


class MenstrualPhase(ForwardCompatibleEnum):
    """Represents menstrual cycle phases."""

    MENSTRUAL = "menstrual"
    """The menstrual phase when bleeding occurs."""

    FOLLICULAR = "follicular"
    """The follicular phase when follicles in ovaries develop."""

    OVULATION = "ovulation"
    """The ovulation phase when an egg is released."""

    LUTEAL = "luteal"
    """The luteal phase following ovulation."""

    PMS = "pms"
    """Premenstrual syndrome phase before menstruation begins."""

    FERTILE = "fertile"
    """The fertile window when conception is most likely."""

    FIRST_TRIMESTER = "first_trimester"
    """First third of pregnancy, weeks 1-12."""

    SECOND_TRIMESTER = "second_trimester"
    """Middle third of pregnancy, weeks 13-26."""

    THIRD_TRIMESTER = "third_trimester"
    """Final third of pregnancy, weeks 27-40."""

    UNKNOWN = "unknown"
    """Menstrual cycle phase could not be determined."""


class KetoneSampleType(ForwardCompatibleIntEnum):
    """Flag indicating the ketone sample type (e.g. blood, breath, urine)"""

    UNKNOWN = 0
    """The type of ketone sample is unknown or not specified."""

    BLOOD = 1
    """Ketone sample taken from blood."""

    URINE = 2
    """Ketone sample taken from urine."""

    BREATH = 3
    """Ketone sample taken from breath."""


class EventType(ForwardCompatibleEnum):
    """Event types in the Terra system."""

    AUTH = "auth"
    DEAUTH = "deauth"
    USER_REAUTH = "user_reauth"
    ACCESS_REVOKED = "access_revoked"
    CONNECTION_ERROR = "connection_error"
    GOOGLE_NO_DATASOURCE = "google_no_datasource"
    PROCESSING = "processing"
    LARGE_REQUEST_SENDING = "large_request_sending"
    RATE_LIMIT_HIT = "rate_limit_hit"
    LARGE_REQUEST_PROCESSING = "large_request_processing"
    ACTIVITY = "activity"
    ATHLETE = "athlete"
    BODY = "body"
    DAILY = "daily"
    MENSTRUATION = "menstruation"
    NUTRITION = "nutrition"
    SLEEP = "sleep"
    HEALTHCHECK = "healthcheck"
    S3_UPLOAD = "s3_upload"


class TimestampLocalization(ForwardCompatibleIntEnum):
    """Indicates whether the timestamps in this payload are localized (LOCAL) or in UTC."""

    UTC = 0
    """UTC timestamps with +00:00 offset. This avoids "Z" notation to ensure compatibility across parsers."""

    LOCAL = 1
    """LOCAL timestamps that may include or exclude the timezone, following ISO8601."""
