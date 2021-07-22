# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsPopup.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.runCommand = QtWidgets.QLineEdit(Dialog)
        self.runCommand.setObjectName("runCommand")
        self.horizontalLayout.addWidget(self.runCommand)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Settings"))
        self.label_2.setWhatsThis(_translate("Dialog", "<html><head/><body><p>The command you would use to run Python in the terminal. Typically py on windows or python3 on Linux.</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Python Command"))
        self.runCommand.setPlaceholderText(_translate("Dialog", "e.g. python3"))
        self.closeButton.setText(_translate("Dialog", "Save and Close"))
