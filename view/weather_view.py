"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: This module the view of the app
details: This module the view of the app.
The Comobobx Widget, refresh button widget, and the three PlotWigets with the ColumLayout.
"""

from typing import List
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from view.weather_plot_view import PlotView

class MainWindow(QtWidgets.QMainWindow):
    """
    Main window View class
    """
    def __init__(self, cities: List[str]):
        super().__init__()

        self._title = "Weather App"
        self._cities = cities

        self.setWindowTitle(self._title)
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.init_ui(title=self._title, items=self._cities)


    def init_ui(self, title: str, items: List[str]):
        """
        Function that initializes the Main window with all the widgets
        """
        self.title_widget = self.get_title_widget(title=title)

        self.combobox_widget = self.get_combobox_widget(items=items)

        self.plot_view = PlotView()

        self.refresh_button = QtWidgets.QPushButton("Refresh data", self)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.title_widget)
        self.layout.addWidget(self.combobox_widget, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.layout.addLayout(self.plot_view.plot_layout)
        self.layout.addWidget(self.refresh_button, alignment=Qt.AlignHCenter | Qt.AlignBottom)

        self.show()

    def get_title_widget(self, title:str):
        """
        Function that return a title Widget
        """
        title_widget = QtWidgets.QLabel(title, self)
        title_widget.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        title_widget.setStyleSheet("font-size: 20px; font-weight: bold;")
        return title_widget

    def get_combobox_widget(self, items: List[str]):
        """
        Function that return a combobox widget with the passed items
        """
        combobox = QtWidgets.QComboBox(self)
        combobox.addItems(items)
        return combobox

    def update_weather_graphs(self, temperature_data: List[List[float]],wind_data: List[List[float]], pressure_data: List[List[float]]):
        """
        Function that updates the weather plot widgets.
        """
        self.plot_view.update_weather_graph(temperature_data, graph_type="temperature")
        self.plot_view.update_weather_graph(wind_data, graph_type="wind")
        self.plot_view.update_weather_graph(pressure_data, graph_type="pressure")
