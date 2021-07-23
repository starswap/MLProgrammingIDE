# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UnitTestResults.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(797, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout.addWidget(self.TitleLabel)
        self.ResultsLayout = QtWidgets.QVBoxLayout()
        self.ResultsLayout.setObjectName("ResultsLayout")
        self.verticalLayout.addLayout(self.ResultsLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Unit Test Results"))
        self.TitleLabel.setText(_translate("Dialog", "Unit Test Results"))
