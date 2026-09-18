
from enum import Enum


class WeatherSeverity(str, Enum):
    NORMAL = "normal"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    SEVERE = "severe"

class WeatherReason(str, Enum):
    HEAVY_SNOW = "heavy_snow"
    HAIL = "hail"
    HEAVY_RAIN = "heavy_rain"
    FREEZING_RAIN = "freezing_rain"
    ICE = "ice"
    HIGH_WIND = "high_wind"
    POOR_VISIBILITY = "poor_visibility"