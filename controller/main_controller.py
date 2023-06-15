"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: This module contains the main controller of the App
details: This module contains the main controller of the App
"""

from typing import List
from controller.weather_controller import WeatherController
from weather_app.model.weather_model import WeatherModel
from weather_app.view.weather_view import MainWindow

class MainController:
    """
    Main controller class
    """
    def __init__(self, cities: List[str]):
        # Fetch weather data and store it in model
        self._weather_controller = WeatherController(cities=cities)
        data = self._weather_controller.fetch_weather_data()

        self._weather_model = WeatherModel(data=data)

        self._view = MainWindow(cities=cities)
        self._view.combobox_widget.activated[str].connect(self.load_city_weather)
        self._view.refresh_button.pressed.connect(self.refresh_weather_data)

        self.load_city_weather(city=cities[0])

    def refresh_weather_data(self):
        """
        Function that refreshed the fetches new weather data from the weather controller
        and calls the main window to display it.
        """
        data = self._weather_controller.fetch_weather_data(refresh=True)
        self._weather_model.set_data(data=data)

        city = self._view.combobox_widget.currentText()
        weather_model_item = self._weather_model.get_weather_model_item(city)
        temperature_data = weather_model_item.get_temperature_data()
        wind_data = weather_model_item.get_wind_data()
        pressure_data = weather_model_item.get_pressure_data()

        self._view.update_weather_graphs(
            temperature_data=temperature_data,
            wind_data=wind_data,
            pressure_data=pressure_data
        )

    def load_city_weather(self, city: str) -> None:
        """
        Function that gets the weather data from the choosen city and
         calls the main view to display the changes
        """
        weather_model_item = self._weather_model.get_weather_model_item(city)
        temperature_data = weather_model_item.get_temperature_data()
        wind_data = weather_model_item.get_wind_data()
        pressure_data = weather_model_item.get_pressure_data()

        self._view.update_weather_graphs(
            temperature_data=temperature_data,
            wind_data=wind_data,
            pressure_data=pressure_data
        )

    def show_view(self):
        self._view.showMaximized()

    def get_weather_model(self):
        return self._weather_model
