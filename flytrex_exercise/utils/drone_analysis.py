import json
import os

import pandas

from flytrex_exercise.weather_fields import WeatherFields

with open(os.path.join(os.path.dirname(__file__), 'drone_limitations.json'), 'r') as fd:
    DRONE_LIMITATIONS = json.loads(fd.read())


def can_drone_fly(record: pandas.Series, drone_type: str) -> bool:
    """
    Return whether the drone can fly in the state described in the record.
    """
    record_snow_values = record[WeatherFields.SNOW_ONE_HOUR.value] + record[WeatherFields.SNOW_THREE_HOURS.value]
    record_rain_values = record[WeatherFields.RAIN_ONE_HOUR.value] + record[WeatherFields.RAIN_THREE_HOURS.value]

    can_fly = record[WeatherFields.WIND_SPEED.value] <= DRONE_LIMITATIONS[drone_type]['wind']['max']
    can_fly = can_fly and record[WeatherFields.TEMPERATURE.value] >= DRONE_LIMITATIONS[drone_type]['temperature'][
        'min']
    can_fly = can_fly and record[WeatherFields.TEMPERATURE.value] <= DRONE_LIMITATIONS[drone_type]['temperature'][
        'max']
    can_fly = can_fly and record_snow_values == 0
    can_fly = can_fly and record_rain_values <= DRONE_LIMITATIONS[drone_type]['precipitation_ml_resistance']
    return can_fly
