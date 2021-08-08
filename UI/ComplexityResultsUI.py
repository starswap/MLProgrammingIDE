# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComplexityResults.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(804, 298)
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
        self.resultsTextBox = QtWidgets.QTextEdit(Dialog)
        self.resultsTextBox.setReadOnly(True)
        self.resultsTextBox.setObjectName("resultsTextBox")
        self.verticalLayout.addWidget(self.resultsTextBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Complexity Analysis Results"))
        self.TitleLabel.setText(_translate("Dialog", "Complexity Analysis Results"))
