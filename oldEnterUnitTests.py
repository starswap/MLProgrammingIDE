# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnterUnitTests2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(528, 526)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Functions = QtWidgets.QVBoxLayout()
        self.Functions.setObjectName("Functions")
        self.verticalLayout.addLayout(self.Functions)
        self.FunctionName = QtWidgets.QLineEdit(Dialog)
        self.FunctionName.setObjectName("FunctionName")
        self.verticalLayout.addWidget(self.FunctionName)
        self.addFunctionButton = QtWidgets.QPushButton(Dialog)
        self.addFunctionButton.setObjectName("addFunctionButton")
        self.verticalLayout.addWidget(self.addFunctionButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Unit Test Entry"))
        self.label.setText(_translate("Dialog", "Enter Unit Tests"))
        self.FunctionName.setText(_translate("Dialog", "FunctionName"))
        self.addFunctionButton.setText(_translate("Dialog", "Add Function"))
