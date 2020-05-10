# pyuic5 map_design.ui -o map_design.py

import sys
from geo_functions import *
from map_real_design import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap


def create_picture(image):
    new_file = "map.png"

    with open(new_file, "wb") as file:
        file.write(image)


class MapInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Map')
        self.center_the_window()

        self.current = "map.png"
        self.set_default()
        self.set_map()

    def center_the_window(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)

    @staticmethod
    def set_default():
        coordinates = get_object_coordinates("Москва")
        scope = get_object_scope("Москва")
        create_picture(get_object_on_map(coordinates, *scope, "map"))

    def set_map(self):
        self.pix_map = QPixmap(self.current).scaled(900, 675)
        self.image = QLabel(self)
        self.image.resize(900, 675)
        self.image.setPixmap(self.pix_map)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _map = MapInterface()
    _map.show()
    sys.exit(app.exec_())
