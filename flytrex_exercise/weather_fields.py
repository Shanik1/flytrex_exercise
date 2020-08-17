from enum import Enum


class WeatherFields(Enum):
    DATETIME = 'dt_iso'
    WIND_SPEED = 'wind_speed'
    TEMPERATURE = 'temp'
    RAIN_ONE_HOUR = 'rain_1h'
    RAIN_THREE_HOURS = 'rain_3h'
    SNOW_ONE_HOUR = 'snow_1h'
    SNOW_THREE_HOURS = 'snow_3h'
