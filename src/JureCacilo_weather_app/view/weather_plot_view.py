"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: This module contains the plot View class
details: This module contains the plot View class, with the 3 plot widgets
"""
from typing import List
from PyQt5 import QtWidgets
import pyqtgraph as pg
from JureCacilo_weather_app.utils.utils import TimeAxisItem


class PlotView:
    """
    Plot view class
    """
    def __init__(self):
        self.plot_layout = QtWidgets.QVBoxLayout()

        self.temp_plot_widget = self.get_plot_widget(name="Temperature", unit=u"\u00b0" + "C")
        self.wind_plot_widget = self.get_plot_widget(name="Wind", unit="m/s")
        self.pressure_plot_widget = self.get_plot_widget(name="Pressure", unit="hPa")

        self.plot_layout.addWidget(self.temp_plot_widget)
        self.plot_layout.addWidget(self.wind_plot_widget)
        self.plot_layout.addWidget(self.pressure_plot_widget)

    def get_plot_widget(self, name: str, unit: str):
        """
        Function that return a Plot Widget.
        X axis is time. Unit is the label of the y axis
        """
        date_axis = TimeAxisItem(orientation='bottom')
        plot_widget = pg.PlotWidget(axisItems={'bottom': date_axis})
        plot_widget.addLegend(offset=20)
        plot_widget.plot([], [])
        plot_widget.setTitle(name)
        plot_widget.setLabel("bottom", text="čas")
        plot_widget.setLabel("left", text=unit)

        return plot_widget

    def update_weather_graph(self, data: List[List[float]], graph_type:str):
        """
        Function that updates the weather graph with new data.
        Based upon the type it updates the correct graph
        """
        x_coords = []
        y_coords = []
        if len(data) > 0:
            x_coords = data[0]
            y_coords = data[1]

        if graph_type == "temperature":
            self.temp_plot_widget.plot(x_coords, y_coords, clear=True)

        elif graph_type == "wind":
            self.wind_plot_widget.plot(x_coords, y_coords, clear=True)

        elif graph_type == "pressure":
            self.pressure_plot_widget.plot(x_coords, y_coords, clear=True)

        else:
            raise NotImplementedError("Type of graph is not implemented")
