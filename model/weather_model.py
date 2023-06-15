"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: This module contains the Weather model
details: This module contains the weather model.
The weather model data is a dict of cities as keys
and WeatherModelItems as values
"""

from typing import Dict
from weather_app.model.weather_model_item import WeatherModelItem


class WeatherModel:
    """
    Weather model class
    """
    def __init__(self, data: Dict[str, WeatherModelItem]=None):
        self._data = data or {}

    def set_data(self, data: Dict[str, WeatherModelItem]):
        """
        Function that sets the _data class property
        """
        self._data = data

    def get_weather_model_item(self, city: str) -> WeatherModelItem:
        """
        Function that return the WeatherModelItem based on the city.
        If city is not in data, it return None.
        """
        return self._data.get(city, None)
