import os
from datetime import datetime
from typing import Callable, AnyStr
from zipfile import ZipFile
import pytemperature

import pandas

from flytrex_exercise.weather_fields import WeatherFields

START_TIME_HOUR = 10
END_TIME_HOUR = 22


def get_normalized_filtered_weather_data() -> pandas.DataFrame:
    """
    Return the normalized weather data as a DataFrame, and filter the data to the relevant time periods.
    """
    with ZipFile(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'weather_data.csv.zip'),
                 'r') as zip_file:
        with zip_file.open('weather_data.csv') as csv_file:
            data_parser: Callable[[AnyStr], datetime] = lambda value: pandas.datetime.strptime(value,
                                                                                               '%Y-%m-%d %H:%M:%S %z %Z')
            df = pandas.read_csv(csv_file, parse_dates=[WeatherFields.DATETIME.value], date_parser=data_parser)
    df = df[(df[WeatherFields.DATETIME.value].dt.hour >= START_TIME_HOUR) & (
            df[WeatherFields.DATETIME.value].dt.hour <= END_TIME_HOUR)]
    df = df.fillna(value=0)
    df[WeatherFields.TEMPERATURE.value] = df.apply(lambda row: pytemperature.k2c(row[WeatherFields.TEMPERATURE.value]), axis=1)
    return df
