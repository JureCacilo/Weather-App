"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: This module contains the weather controller
details: This module contains the wather controllr,
that invokes the XmlParser when fetching new data from ARSO.
"""

from typing import List, Dict
from weather_app.model.weather_model_item import WeatherModelItem
from weather_app.xml_parser.weather_parser import WeatherParser

citiesToXmlUrl = {
    "Ljubljana": "http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/60.xml",
    "Lesce": "http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/44.xml",
    "Logatec": "http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/409.xml",
    "Vrhnika": "http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/372.xml",
    "Boršt pri Gorenji vasi": "http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/45.xml",
    "Brnik": "http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/407.xml"
}

class WeatherController:
    """
    Weather controller class
    """
    def __init__(self, cities: List[str]) -> None:
        self._cities = cities
        self._weather_parsers: Dict[str, WeatherParser] = {}
        self._set_weather_parsers()


    def fetch_weather_data(self, refresh: bool = False):
        """
        Function that fetches calls XML parser for every weather station(city)
        and creates a dict of WeatherModelItems for every city.
        """
        if refresh:
            self._set_weather_parsers()

        data: Dict[str, WeatherModelItem] = {}
        for city, parser in self._weather_parsers.items():
            temperature_data = parser.get_temperature_data()
            wind_data = parser.get_wind_data()
            pressure_data = parser.get_pressure_data()

            data[city] = WeatherModelItem(
                city=city,
                temperature_data=temperature_data,
                wind_data=wind_data,
                pressure_data=pressure_data
            )

        return data

    def _set_weather_parsers(self):
        """
        Private function that refreshed the xml parsers for every city.
        """
        self._weather_parsers.clear()
        for city in self._cities:
            xml_url = citiesToXmlUrl.get(city, None)
            if xml_url is not None:
                self._weather_parsers[city]= WeatherParser(city = city, url=xml_url)
