import pytest
from PyQt5.QtWidgets import QApplication
from JureCacilo_weather_app.controller.main_controller import MainController

cities = ["Ljubljana", "Lesce"]

@pytest.fixture
def app():
    app = QApplication([])
    yield app
    app.quit()

def test_change_city(app):
    main_controller = MainController(cities=cities)

    weather_model = main_controller.get_weather_model()
    lj_weather_model_item = weather_model.get_weather_model_item("Ljubljana")

    lesce_weather_model_item = weather_model.get_weather_model_item("Lesce")

    # Assert that temperature data is not None
    assert lj_weather_model_item is not None
    assert len(lj_weather_model_item.get_temperature_data()) > 0

    assert lesce_weather_model_item is not None
    assert len(lesce_weather_model_item.get_temperature_data()) > 0
