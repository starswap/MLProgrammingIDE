from PyQt5 import QtCore, QtGui, QtWidgets #Import graphics library
class Ui_Dialog(object):
    """The main window class is used by the Qt graphics library to create the main window of the program"""
    def setupUi(self, Dialog):
        """Creates the user interface elements"""
        
        #Create a Qt Dialog which is used as a pop up box and give it a name and size
        Dialog.setObjectName("Dialog")
        Dialog.resize(528, 526)
        
        #Create a vertical layout within which all parts of the dialogue box will be stacked. This layout widget ensures that the elements will dynamically resize if the dialogue is enlarged 
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #Create a scroll area which is a set of widgets that can have a scroll bar applied to them if they take up more space than the scroll are allows
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 508, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        #Create another vertical layout which we will put the widgets of the dialogue inside, then append this to the scroll area
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        #Label the dialogue box with a title and style it underlined and size 18 in the default font.
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        
        #Create a vertical layout which will contain a unit test interface for each function the user defines. This will consist of the function signature and a table for constraints, argument types and test values 
        self.Functions = QtWidgets.QVBoxLayout()
        self.Functions.setObjectName("Functions")
        self.verticalLayout_2.addLayout(self.Functions)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        
        #Fill the scroll area with its contents
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        
        #Create a textbox (QLineEdit) for the user to type the name of a function they want to make unit tests for and then add this to the dialogue box
        self.FunctionName = QtWidgets.QLineEdit(Dialog)
        self.FunctionName.setObjectName("FunctionName")
        self.verticalLayout.addWidget(self.FunctionName)
        
        #Create a horizontal layout to contain a QSpinBox for the number of arguments that the function has, and a label for this box. Scale these adn add them to the layout.
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
        
        #Create a button to add a new function based on the form data the user has typed in so that they can add unit tests for it. 
        self.addFunctionButton = QtWidgets.QPushButton(Dialog)
        self.addFunctionButton.setObjectName("addFunctionButton")
        self.verticalLayout.addWidget(self.addFunctionButton)
        
        #Create a close button so the user can save the unit tests and close the dialogue
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

	#Add the text to the dialogue in the user's language
        self.retranslateUi(Dialog)
        
        #Sets up the necessary slots to make the program work.
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
       """Translates the program's text to the language of the user, using mappings defined in Qt. This a default feature of qt which I have kept despite only making my program for English-speaking users at the moment"""
       	#Creates a translator object to translate the text.
        _translate = QtCore.QCoreApplication.translate
        
        #Translate text and set text in the program to the translated result
        Dialog.setWindowTitle(_translate("Dialog", "Unit Test Entry"))
        self.label.setText(_translate("Dialog", "Enter Unit Tests"))
        self.FunctionName.setText(_translate("Dialog", "FunctionName"))
        self.label_2.setText(_translate("Dialog", "Number Of Arguments:"))
        self.addFunctionButton.setText(_translate("Dialog", "Add Function"))
        self.closeButton.setText(_translate("Dialog", "Save and Close"))
