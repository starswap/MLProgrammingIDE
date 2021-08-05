from PyQt5 import QtCore, QtGui, QtWidgets #Import necessary modules


class Ui_Form(object): #A Ui_Form object is a custom widget that we can bring into a program 
    def setupUi(self, Form):
    	"""Create the base UI of the comment"""
    	
        Form.setObjectName("Comment") 
        
        #Set correct size and stretch characteristics
        Form.resize(159, 243) 
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        
        #Create the vertical layout which will contain the comment textedit and the dismiss button, laid out vertically, and style it correctly
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #This QFrame is simply used to put a black border around the content of the comment
        self.comment = QtWidgets.QFrame(Form)
        self.comment.setStyleSheet("QFrame#comment {border: 1px solid black;}")
        self.comment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.comment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.comment.setObjectName("comment")
        
        #Another vertical layout inside the frame is needed
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.comment)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        #Create commentText textedit and style main font (this will be overwritten for code blocks)
        self.commentText = QtWidgets.QTextEdit(self.comment)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.commentText.setFont(font)
        self.commentText.setReadOnly(True)
        self.commentText.setObjectName("commentText")
        self.verticalLayout_2.addWidget(self.commentText)
        
        #Create and style the button needed to close the comment and add it to the layout
        self.dismissButton = QtWidgets.QPushButton(self.comment)
        self.dismissButton.setStyleSheet("background-color: rgb(233, 185, 110)")
        self.dismissButton.setObjectName("dismissButton")
        self.verticalLayout_2.addWidget(self.dismissButton)
        self.verticalLayout.addWidget(self.comment)

        self.retranslateUi(Form) #Put text on the dismiss button
        QtCore.QMetaObject.connectSlotsByName(Form) #Set up slots (events in Qt)

    def retranslateUi(self, Form):
    	"""Fills the English text in on the dismiss button"""
    	
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dismissButton.setText(_translate("Form", "Dismiss Suggestion")) #Write Dismiss Suggestion on the button
