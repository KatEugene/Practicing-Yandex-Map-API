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
        MainWindow.resize(900, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(660, 30, 41, 41))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(660, 90, 41, 41))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_up = QtWidgets.QPushButton(self.centralwidget)
        self.btn_up.setGeometry(QtCore.QRect(800, 10, 41, 41))
        self.btn_up.setObjectName("btn_up")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(750, 60, 41, 41))
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(850, 60, 41, 41))
        self.btn_right.setObjectName("btn_right")
        self.btn_down = QtWidgets.QPushButton(self.centralwidget)
        self.btn_down.setGeometry(QtCore.QRect(800, 110, 41, 41))
        self.btn_down.setObjectName("btn_down")
        self.btn_scheme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_scheme.setGeometry(QtCore.QRect(780, 340, 81, 41))
        self.btn_scheme.setObjectName("btn_scheme")
        self.btn_satellite = QtWidgets.QPushButton(self.centralwidget)
        self.btn_satellite.setGeometry(QtCore.QRect(780, 220, 81, 41))
        self.btn_satellite.setObjectName("btn_satellite")
        self.btn_hybrid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hybrid.setGeometry(QtCore.QRect(780, 280, 81, 41))
        self.btn_hybrid.setObjectName("btn_hybrid")
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
