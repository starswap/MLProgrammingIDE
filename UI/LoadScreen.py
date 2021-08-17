# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("background-color: white;border-radius: 15px;")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 241, 191))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        self.userProficiencyLevelLabel = QtWidgets.QLabel(self.centralwidget)
        self.userProficiencyLevelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userProficiencyLevelLabel.setObjectName("userProficiencyLevelLabel")
        self.gridLayout.addWidget(self.userProficiencyLevelLabel, 7, 1, 1, 1)
        self.newProjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.newProjectButton.setObjectName("newProjectButton")
        self.gridLayout.addWidget(self.newProjectButton, 6, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: white;border-radius: 15px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 50, 211, 201))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.newResourceButton = QtWidgets.QPushButton(self.centralwidget)
        self.newResourceButton.setObjectName("newResourceButton")
        self.gridLayout.addWidget(self.newResourceButton, 6, 1, 1, 1)
        self.openProjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.openProjectButton.setObjectName("openProjectButton")
        self.gridLayout.addWidget(self.openProjectButton, 7, 0, 1, 1)
        self.WelcomeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WelcomeLabel.sizePolicy().hasHeightForWidth())
        self.WelcomeLabel.setSizePolicy(sizePolicy)
        self.WelcomeLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.gridLayout.addWidget(self.WelcomeLabel, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 21))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Icons/Screenshot from 2021-07-21 14-52-33.png\"/></p></body></html>"))
        self.userProficiencyLevelLabel.setText(_translate("MainWindow", "[Current Level = Beginner]"))
        self.newProjectButton.setText(_translate("MainWindow", "Create a new project"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Icons/Screenshot from 2021-07-21 14-52-14.png\"/></p></body></html>"))
        self.newResourceButton.setText(_translate("MainWindow", "Learn something new"))
        self.openProjectButton.setText(_translate("MainWindow", "Open an existing project"))
        self.WelcomeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Welcome Back</span></p></body></html>"))
import icons_rc
