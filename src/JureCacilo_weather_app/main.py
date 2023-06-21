"""
COPYRIGHT(c) 2023 RLS d.o.o, Pod vrbami 2, 1218 Komenda, Slovenia
brief: Main file
details: Main file
"""


import sys
from PyQt5.QtWidgets import QApplication
from JureCacilo_weather_app.controller.main_controller import MainController

cities = ["Ljubljana", "Lesce", "Boršt pri Gorenji vasi", "Brnik", "Logatec", "Vrhnika"]

def main():
    """
    Function that is called when starting the app.
    It creates the QApplication and Main Controller and show the view.
    """
    app = QApplication(sys.argv)
    main_controller = MainController(cities=cities)
    main_controller.show_view()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
