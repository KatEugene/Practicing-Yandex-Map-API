import sys
from geo_functions import *
from map_design import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap


def create_picture(image, name_of_file):
    with open(name_of_file, "wb") as file:
        file.write(image)


class MapInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Map')
        self.center_the_window()

        self.current_object = "Москва"
        self.current_map = "map.png"
        self.current_kind = "map"

        self.set_default()

        self.btn_plus.clicked.connect(self.bring_closer)
        self.btn_minus.clicked.connect(self.put_away)

    def center_the_window(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)

    def set_map(self):
        self.pix_map = QPixmap(self.current_map)
        self.image = QLabel(self)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pix_map)

    def set_default(self):
        coordinates = get_object_coordinates(self.current_object)
        scope = get_object_scope(self.current_object)
        create_picture(get_object_on_map(coordinates, *scope, self.current_kind), self.current_map)
        self.set_map()

    def bring_closer(self):
        coordinates = get_object_coordinates(self.current_object)
        scope = list(map(lambda x: x - 0.1, get_object_scope(self.current_object)))
        create_picture(get_object_on_map(coordinates, *scope, self.current_kind), self.current_map)
        self.set_map()

    def put_away(self):
        coordinates = get_object_coordinates(self.current_object)
        scope = list(map(lambda x: x + 0.1, get_object_scope(self.current_object)))
        create_picture(get_object_on_map(coordinates, *scope, self.current_kind), self.current_map)
        self.set_map()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _map = MapInterface()
    _map.show()
    sys.exit(app.exec_())
