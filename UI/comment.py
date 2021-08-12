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
        Form.resize(159, 244)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dismissButton = QtWidgets.QPushButton(self.comment)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dismissButton.setFont(font)
        self.dismissButton.setStyleSheet("background-color: rgb(233, 185, 110)")
        self.dismissButton.setObjectName("dismissButton")
        self.horizontalLayout.addWidget(self.dismissButton)
        self.helpButton = QtWidgets.QToolButton(self.comment)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout.addWidget(self.helpButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.comment)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comment.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.commentText.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">To add your own syntax hints, edit the Syntax_Rules.txt file. You can also share this file with others.</span></p></body></html>"))
        self.dismissButton.setText(_translate("Form", "Dismiss Suggestion"))
        self.helpButton.setToolTip(_translate("Form", "To add your own syntax hints, edit the Syntax_Rules.txt file. You can also share this file with others"))
        self.helpButton.setText(_translate("Form", "?"))