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
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 508, 344))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Functions = QtWidgets.QVBoxLayout()
        self.Functions.setObjectName("Functions")
        self.verticalLayout_2.addLayout(self.Functions)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.FunctionName = QtWidgets.QLineEdit(Dialog)
        self.FunctionName.setText("")
        self.FunctionName.setObjectName("FunctionName")
        self.horizontalLayout_2.addWidget(self.FunctionName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.FunctionFileName = QtWidgets.QLineEdit(Dialog)
        self.FunctionFileName.setText("")
        self.FunctionFileName.setObjectName("FunctionFileName")
        self.horizontalLayout_3.addWidget(self.FunctionFileName)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.NumArguments = QtWidgets.QSpinBox(Dialog)
        self.NumArguments.setMinimum(1)
        self.NumArguments.setObjectName("NumArguments")
        self.horizontalLayout.addWidget(self.NumArguments)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.addFunctionButton = QtWidgets.QPushButton(Dialog)
        self.addFunctionButton.setObjectName("addFunctionButton")
        self.verticalLayout.addWidget(self.addFunctionButton)
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Unit Test Entry"))
        self.label.setText(_translate("Dialog", "Enter Unit Tests"))
        self.label_3.setText(_translate("Dialog", "Function Name: "))
        self.label_4.setText(_translate("Dialog", "Function File name"))
        self.label_2.setText(_translate("Dialog", "Number Of Arguments:"))
        self.addFunctionButton.setText(_translate("Dialog", "Add Function"))
        self.closeButton.setText(_translate("Dialog", "Save and Close"))
