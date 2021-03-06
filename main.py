import sys
from geo_functions import *
from map_design import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QLabel
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

        self.list_of_coordinates = []
        self.current_map = "map.png"
        self.current_kind = "map"
        self.current_z = 9

        self.set_object("Москва")

        self.btn_plus.clicked.connect(self.increase)
        self.btn_minus.clicked.connect(self.decrease)

        self.btn_left.clicked.connect(self.left)
        self.btn_right.clicked.connect(self.right)
        self.btn_up.clicked.connect(self.up)
        self.btn_down.clicked.connect(self.down)

        self.btn_scheme.clicked.connect(self.scheme)
        self.btn_satellite.clicked.connect(self.satellite)
        self.btn_hybrid.clicked.connect(self.hybrid)

        self.btn_search.clicked.connect(self.search)
        self.btn_clear.clicked.connect(self.clear)

        self.btn_find_address.clicked.connect(self.find_address)

    def set_map(self):
        self.pix_map = QPixmap(self.current_map)
        self.image = QLabel(self)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pix_map)

    def set_object(self, address):
        self.current_object = address
        self.current_coordinates = get_object_coordinates(self.current_object)
        scope = get_object_scope(self.current_object)
        if len(self.list_of_coordinates) > 0:
            _pt = []
            for i in range(len(self.list_of_coordinates)):
                _pt.append(','.join(list(map(str, self.list_of_coordinates[i])) + [f"pm2rdm{i+1}"]))
            _pt = "~".join(_pt)

            create_picture(
                get_object_on_map(",".join(list(map(str, self.current_coordinates))),
                                  self.current_kind, *scope, pt=_pt),
                self.current_map
            )
        else:
            create_picture(
                get_object_on_map(",".join(list(map(str, self.current_coordinates))), self.current_kind, *scope),
                self.current_map
            )
        try:
            self.image.deleteLater()
        except AttributeError:
            pass
        self.set_map()
        self.image.show()

    def change_picture(self):
        if len(self.list_of_coordinates) > 0:
            _pt = []
            for i in range(len(self.list_of_coordinates)):
                _pt.append(','.join(list(map(str, self.list_of_coordinates[i])) + [f"pm2rdm{i+1}"]))
            _pt = "~".join(_pt)

            create_picture(
                get_object_on_map(",".join(list(map(str, self.current_coordinates))), self.current_kind,
                                  z=self.current_z, pt=_pt),
                self.current_map
            )
        else:
            create_picture(
                get_object_on_map(",".join(list(map(str, self.current_coordinates))), self.current_kind,
                                  z=self.current_z),
                self.current_map
            )
        self.image.deleteLater()
        self.set_map()
        self.image.show()

    def increase(self):
        self.current_z = (self.current_z + 1) % 18
        self.change_picture()

    def decrease(self):
        self.current_z = (self.current_z - 1) % 18
        self.change_picture()

    def up(self):
        self.current_coordinates[1] += (20 / 111)
        self.change_picture()

    def down(self):
        self.current_coordinates[1] -= (20 / 111)
        self.change_picture()

    def left(self):
        self.current_coordinates[0] -= (20 / 111)
        self.change_picture()

    def right(self):
        self.current_coordinates[0] += (20 / 111)
        self.change_picture()

    def scheme(self):
        self.current_kind = "map"
        self.change_picture()

    def satellite(self):
        self.current_kind = "sat"
        self.change_picture()

    def hybrid(self):
        self.current_kind = "sat,skl"
        self.change_picture()

    def search(self):
        new_address = self.address.text()
        self.list_of_coordinates.append(get_object_coordinates(new_address))
        self.set_object(new_address)

    def clear(self):
        self.list_of_coordinates.clear()
        self.change_picture()

    def center_the_window(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)

    def find_address(self):
        address = get_object_address(self.current_object)
        self.address_of_object.setText(address)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _map = MapInterface()
    _map.show()
    sys.exit(app.exec_())
