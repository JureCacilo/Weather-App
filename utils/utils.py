"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: This module contains util classes and functions
details: This module contains util classes and functions
"""

from datetime import datetime
import pyqtgraph as pg

def strip_weather_time(datetime_str: str):
    """
    Function that accepts a datime with the format (<%d.%m.%Y %H:%m CET >)
    and converts it to a valid datetime object"
    """
    try:
        # Substring untill the last 4 elements (CET ). Datetime cannot strip time zones
        datetime_str = datetime_str[:-4]

        return datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')

    except (IndexError, ValueError) as error:
        print("Exception", error)
        return None


class TimeAxisItem(pg.AxisItem):
    """
    Utility class for Plots which x axis is an item axis.
    Used for correctly displaying the datetime values on the x-axis
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTickSpacing(levels=[(10000, 0)])

    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(value).strftime("%d-%m %H:%m") for value in values]
