# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 454)
        MainWindow.setStyleSheet("background-color: rgb(114, 159, 207)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.newResourceButton = QtWidgets.QPushButton(self.centralwidget)
        self.newResourceButton.setObjectName("newResourceButton")
        self.gridLayout.addWidget(self.newResourceButton, 6, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: white;border-radius: 15px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 50, 211, 201))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("background-color: white;border-radius: 15px;")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 241, 191))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        self.newProjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.newProjectButton.setObjectName("newProjectButton")
        self.gridLayout.addWidget(self.newProjectButton, 6, 0, 1, 1)
        self.openProjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.openProjectButton.setObjectName("openProjectButton")
        self.gridLayout.addWidget(self.openProjectButton, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML Programming IDE"))
        self.newResourceButton.setText(_translate("MainWindow", "Learn something new"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Icons/Screenshot from 2021-07-21 14-52-14.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Icons/Screenshot from 2021-07-21 14-52-33.png\"/></p></body></html>"))
        self.newProjectButton.setText(_translate("MainWindow", "Create a new project"))
        self.openProjectButton.setText(_translate("MainWindow", "Open an existing project"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Welcome Back</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "[Current Level = Beginner]"))
import icons_rc
