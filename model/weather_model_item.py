"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: This module contains the Weather model item
details: This module contains the Weather model item
"""
from typing import List, Tuple


class WeatherModelItem:
    """
    Weather model item class. Contains temperature,
    pressure and wind data for the spccified city.
    """
    def __init__(self, city: str,
                 temperature_data: List[Tuple[float, float]] = None,
                 wind_data: List[Tuple[float, float]] = None,
                 pressure_data: List[Tuple[float, float]] = None):
        self.city = city
        self._temperature_data = temperature_data or []
        self._wind_data = wind_data
        self._pressure_data = pressure_data

    def get_temperature_data(self):
        """
        Function that return transforms temperature data to list with 2 lists.
        The first list contains the x-coords and the second contain the y-coords.
        """
        return [list(coords) for coords in zip(*self._temperature_data)]

    def get_wind_data(self):
        """
        Function that return transforms wind data to list with 2 lists.
        The first list contains the x-coords and the second contain the y-coords.
        """
        return [list(coords) for coords in zip(*self._wind_data)]

    def get_pressure_data(self):
        """
        Function that return transforms pressure data to list with 2 lists.
        The first list contains the x-coords and the second contain the y-coords.
        """
        return [list(coords) for coords in zip(*self._pressure_data)]
