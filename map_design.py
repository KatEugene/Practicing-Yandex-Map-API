# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(700, 310, 41, 41))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(700, 380, 41, 41))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_up = QtWidgets.QPushButton(self.centralwidget)
        self.btn_up.setGeometry(QtCore.QRect(870, 280, 41, 41))
        self.btn_up.setObjectName("btn_up")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(820, 330, 41, 41))
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(920, 330, 41, 41))
        self.btn_right.setObjectName("btn_right")
        self.btn_down = QtWidgets.QPushButton(self.centralwidget)
        self.btn_down.setGeometry(QtCore.QRect(870, 380, 41, 41))
        self.btn_down.setObjectName("btn_down")
        self.btn_scheme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_scheme.setGeometry(QtCore.QRect(690, 220, 81, 41))
        self.btn_scheme.setObjectName("btn_scheme")
        self.btn_satellite = QtWidgets.QPushButton(self.centralwidget)
        self.btn_satellite.setGeometry(QtCore.QRect(800, 220, 81, 41))
        self.btn_satellite.setObjectName("btn_satellite")
        self.btn_hybrid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hybrid.setGeometry(QtCore.QRect(910, 220, 81, 41))
        self.btn_hybrid.setObjectName("btn_hybrid")
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(820, 20, 171, 22))
        self.address.setObjectName("address")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(860, 70, 93, 28))
        self.btn_search.setObjectName("btn_search")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 20, 131, 20))
        self.label.setObjectName("label")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(700, 70, 93, 28))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_find_address = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find_address.setGeometry(QtCore.QRect(740, 130, 171, 28))
        self.btn_find_address.setObjectName("btn_find_address")
        self.address_of_object = QtWidgets.QLabel(self.centralwidget)
        self.address_of_object.setGeometry(QtCore.QRect(650, 180, 341, 21))
        self.address_of_object.setText("")
        self.address_of_object.setObjectName("address_of_object")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_up.setText(_translate("MainWindow", "▲"))
        self.btn_left.setText(_translate("MainWindow", "⮜"))
        self.btn_right.setText(_translate("MainWindow", "⮞"))
        self.btn_down.setText(_translate("MainWindow", "▼"))
        self.btn_scheme.setText(_translate("MainWindow", "Схема"))
        self.btn_satellite.setText(_translate("MainWindow", "Спутник"))
        self.btn_hybrid.setText(_translate("MainWindow", "Гибрид"))
        self.btn_search.setText(_translate("MainWindow", "Искать"))
        self.label.setText(_translate("MainWindow", "Введите ваш запрос:"))
        self.btn_clear.setText(_translate("MainWindow", "Очистить"))
        self.btn_find_address.setText(_translate("MainWindow", "Определить адрес объекта:"))
