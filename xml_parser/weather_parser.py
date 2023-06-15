"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: This module contains the Weather Parser logic
details: This module contains the Weather Parser logic
"""

from typing import List, Tuple
import xml.etree.ElementTree as ET
import urllib.request
from weather_app.utils.utils import strip_weather_time



class WeatherParser:
    """
    A class representing the Xml Weather Parser
    """
    def __init__(self, city: str, url: str):
        self._city = city

        response = urllib.request.urlopen(url).read()
        self._root = ET.fromstring(response)

    def get_temperature_data(self):
        """
        Function to fetch temperature data from xml file.
        "tavg" element is the xml element that stores the temperature value
        and valid is the timestamp.
        """
        temperature_data: List[Tuple[float, float]] = []
        for entry in self._root.findall("metData"):
            temp_element = entry.find("tavg")
            datetime_element = entry.find("valid")

            if temp_element is not None and datetime_element is not None:
                datetime_str = datetime_element.text
                datetime_object = strip_weather_time(datetime_str)
                temperature = float(temp_element.text)

                temperature_data.append((datetime_object.timestamp(), temperature))

        return temperature_data

    def get_wind_data(self):
        """
        Function to fetch wind data from xml file.
        "ffavg" element is the xml element that stores the wind value
         and valid is the timestamp.
        """
        wind_data: List[Tuple[float, float]] = []
        for entry in self._root.findall("metData"):
            wind_element = entry.find("ffavg")
            datetime_element = entry.find("valid")

            if wind_element is not None and datetime_element is not None:
                datetime_str = datetime_element.text
                datetime_object = strip_weather_time(datetime_str)
                wind = float(wind_element.text)

                wind_data.append((datetime_object.timestamp(), wind))

        return wind_data

    def get_pressure_data(self):
        """
        Function to fetch pressure data from xml file.
        "pavg" element is the xml element that stores the pressure value
         and valid is the timestamp.
        """
        pressure_data: List[Tuple[float, float]] = []
        for entry in self._root.findall("metData"):
            pressure_element = entry.find("pavg")
            datetime_element = entry.find("valid")

            if pressure_element is not None and datetime_element is not None:
                datetime_str = datetime_element.text
                datetime_object = strip_weather_time(datetime_str)
                pressure = float(pressure_element.text)

                pressure_data.append((datetime_object.timestamp(), pressure))

        return pressure_data
