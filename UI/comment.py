# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comment.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(159, 243)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comment = QtWidgets.QFrame(Form)
        self.comment.setStyleSheet("QFrame#comment {border: 1px solid black;}")
        self.comment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.comment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.comment.setObjectName("comment")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.comment)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.commentText = QtWidgets.QTextEdit(self.comment)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.commentText.setFont(font)
        self.commentText.setReadOnly(True)
        self.commentText.setObjectName("commentText")
        self.verticalLayout_2.addWidget(self.commentText)
        self.dismissButton = QtWidgets.QPushButton(self.comment)
        self.dismissButton.setStyleSheet("background-color: rgb(233, 185, 110)")
        self.dismissButton.setObjectName("dismissButton")
        self.verticalLayout_2.addWidget(self.dismissButton)
        self.verticalLayout.addWidget(self.comment)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dismissButton.setText(_translate("Form", "Dismiss Suggestion"))
