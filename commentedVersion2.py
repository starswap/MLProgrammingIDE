from PyQt5 import QtCore, QtGui, QtWidgets #Import graphics library

class Ui_MainWindow(object):
    """The main window class is used by the Qt graphics library to create the main window of the program"""
    def setupUi(self, MainWindow):
       """Creates the user interface elements"""
        
        #Set window title and size
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 638)
        
        #The central widget is the main part of the UI which is displayed in the middle of the program. This is the main window in this case
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #NEW: Set the main window to use a grid layout. Grid layouts can automatically scale when the size of the window is changed because they maintain their aspect ratio. This solves the user's problem
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        
	#Create the area on which the line numbers will be drawn (by a QPainter object) as a QWidget and set the shape and location. The choice of a QPainter method is recommended by Qt here:https://doc.qt.io/qt-5/qtwidgets-widgets-codeeditor-example.html        
        self.lineNumberArea_2 = QtWidgets.QWidget(self.centralwidget)
     
        #Set the size policy and stretches of the elements in the scene. This is necessary make sure objects take up the corerct amount of space.
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.lineNumberArea_2.sizePolicy().hasHeightForWidth())
        
        #Set the size policy and display characteristics (background color) of the line number area, then add it to the grid layout
        self.lineNumberArea_2.setSizePolicy(sizePolicy)
        self.lineNumberArea_2.setStyleSheet("background-color:rgb(211, 215, 207)")
        self.lineNumberArea_2.setObjectName("lineNumberArea_2")
        self.gridLayout.addWidget(self.lineNumberArea_2, 1, 1, 1, 1)
        
        #Create the list of files menu and scale it to be the right shape, then add it to the grid layout
        self.listOfFilesMenu = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.listOfFilesMenu.sizePolicy().hasHeightForWidth())
        self.listOfFilesMenu.setSizePolicy(sizePolicy)
        self.listOfFilesMenu.setObjectName("listOfFilesMenu")
        self.gridLayout.addWidget(self.listOfFilesMenu, 1, 0, 2, 1)
        
        #Create the code box as a text box (allows rich text formatting) and set the size and position and add it to the grid layout. NEW: The font of the code box is set so that it is monospace which is a design requirement.        
        self.codeBox = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.codeBox.sizePolicy().hasHeightForWidth())
        self.codeBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.codeBox.setFont(font)
        self.codeBox.setStyleSheet("")
        self.codeBox.setObjectName("codeBox")
        self.gridLayout.addWidget(self.codeBox, 1, 2, 1, 1)

        #Create the run command box as a plain text box and set its size and position then add it to the layout. NEW: The font is set to be monospace and bold. 
        self.runCommandBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runCommandBox.sizePolicy().hasHeightForWidth())
        self.runCommandBox.setSizePolicy(sizePolicy)
        self.runCommandBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setBold(True)
        font.setWeight(75)
        self.runCommandBox.setFont(font)
        self.runCommandBox.setStyleSheet("")
        self.runCommandBox.setObjectName("runCommandBox")
        self.gridLayout.addWidget(self.runCommandBox, 0, 2, 1, 2)

	#NEW: Create the vertical layout object which will contain the hexagons and their labels, then add this to the main grid layout. Fill the vertical layout with labels (for efficiency, efficacy, readability, elegance) and dials which are placeholders as outlined in the report.
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.dial = QtWidgets.QDial(self.widget)
        self.dial.setGeometry(QtCore.QRect(50, 20, 50, 64))
        self.dial.setObjectName("dial")
        self.verticalLayout.addWidget(self.widget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.dial_2 = QtWidgets.QDial(self.widget_2)
        self.dial_2.setGeometry(QtCore.QRect(60, 20, 50, 64))
        self.dial_2.setObjectName("dial_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.dial_3 = QtWidgets.QDial(self.widget_3)
        self.dial_3.setGeometry(QtCore.QRect(60, 30, 50, 64))
        self.dial_3.setObjectName("dial_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.dial_4 = QtWidgets.QDial(self.widget_4)
        self.dial_4.setGeometry(QtCore.QRect(60, 20, 50, 64))
        self.dial_4.setObjectName("dial_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        
        #NEW: Set the stretch factors inside the vertical layout. This ensures that the widgets which the hexagons will be drawn on top of will be 5 times as tall as their corresponding labels, which is proportionate.
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 5)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 5)
        self.verticalLayout.setStretch(7, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 4, 3, 1)


	#NEW: Create a second vertical layout which will store comments, and fill it with a couple of placeholder comments, each of which is made up of a text browser object and a button to close the comment. Add this to the grid layout.
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 3, 1, 1)
       
  	#NEW: Create the code output window, style it to be black with white bold text, and set its dimensions and location then add it to the grid layout.
        self.outputWindow = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setBold(True)
        font.setWeight(75)
        self.outputWindow.setFont(font)
        self.outputWindow.setStyleSheet("background-color:black;color:white;")
        self.outputWindow.setReadOnly(True)
        self.outputWindow.setObjectName("outputWindow")
        self.gridLayout.addWidget(self.outputWindow, 2, 1, 1, 3)

        #Create the run button as a green push button of the correct size and place it in the right place, adding it to the layout.
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setStyleSheet("background-color:rgb(115, 210, 22);")
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 0, 0, 1, 1)
      
 	#NEW: Set the stretch factors for the rows and columns on the grid layout. These are the ratios representing how much of the available vertical and horizontal space each object should take up. These ratios are easily flexed to reflect a larger screen size. 
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 40)
        self.gridLayout.setColumnStretch(3, 20)
        self.gridLayout.setColumnStretch(4, 20)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 15)
        
      	#Set the central widget up
        MainWindow.setCentralWidget(self.centralwidget)
        
        #Set up the menu bar to be displayed at the top of the screen and the options within it.
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuUnit_Tests = QtWidgets.QMenu(self.menubar)
        self.menuUnit_Tests.setObjectName("menuUnit_Tests")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
        #Set up the  "actions" which are sub-menu options below e.g. file or help       
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionAdd_File_to_Project = QtWidgets.QAction(MainWindow)
        self.actionAdd_File_to_Project.setObjectName("actionAdd_File_to_Project")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFind_Replace = QtWidgets.QAction(MainWindow)
        self.actionFind_Replace.setObjectName("actionFind_Replace")
        self.actionFormat_Code = QtWidgets.QAction(MainWindow)
        self.actionFormat_Code.setObjectName("actionFormat_Code")
        self.actionExecute_Project = QtWidgets.QAction(MainWindow)
        self.actionExecute_Project.setObjectName("actionExecute_Project")
        self.actionDisplay_Unit_Test_Results = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Unit_Test_Results.setObjectName("actionDisplay_Unit_Test_Results")
        self.actionEnter_Unit_Tests = QtWidgets.QAction(MainWindow)
        self.actionEnter_Unit_Tests.setObjectName("actionEnter_Unit_Tests")
        self.actionDisplay_Test_Results = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Test_Results.setObjectName("actionDisplay_Test_Results")
        self.actionShow_Tutoruial = QtWidgets.QAction(MainWindow)
        self.actionShow_Tutoruial.setObjectName("actionShow_Tutoruial")
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionAdd_File_to_Project)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionFind_Replace)
        self.menuEdit.addAction(self.actionFormat_Code)
        self.menuRun.addAction(self.actionExecute_Project)
        self.menuRun.addAction(self.actionDisplay_Unit_Test_Results)
        self.menuUnit_Tests.addAction(self.actionEnter_Unit_Tests)
        self.menuUnit_Tests.addAction(self.actionDisplay_Test_Results)
        self.menuHelp.addAction(self.actionShow_Tutoruial)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuUnit_Tests.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

	#Qt expects the objects to have their text generated by a translating function, which allows it to support different languages (although this program will only have English)
        self.retranslateUi(MainWindow)

        #Sets up the necessary slots to make the program work.
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
    	#Creates a translator object to translate the text.
        _translate = QtCore.QCoreApplication.translate
        
        #Use the translator object to translate the text to display on each of the menu options into the target language (which doesn't change them as English is the target language). Note that the HTML is the default formatting for TextEdits (not for PlainTextEdits)
        MainWindow.setWindowTitle(_translate("MainWindow", "ML Programming IDE"))
        self.codeBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Code will be typed here</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.runCommandBox.setPlainText(_translate("MainWindow", "e.g. python3 myFile.py"))
        self.label.setText(_translate("MainWindow", "Efficacy"))
        self.label_2.setText(_translate("MainWindow", "Efficiency"))
        self.label_3.setText(_translate("MainWindow", "Elegance"))
        self.label_4.setText(_translate("MainWindow", "Readability"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is where the AI\'s comments will go</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Dismiss Suggestion"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Second AI suggestion etc.    </p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Dismiss Suggestion"))
        self.outputWindow.setPlainText(_translate("MainWindow", "code output is displayed \n"
"in this window\n"
""))
        self.runButton.setText(_translate("MainWindow", "Run Program"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuUnit_Tests.setTitle(_translate("MainWindow", "Unit Tests"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionAdd_File_to_Project.setText(_translate("MainWindow", "Add File to Project"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionFind_Replace.setText(_translate("MainWindow", "Find/Replace"))
        self.actionFormat_Code.setText(_translate("MainWindow", "Format Code"))
        self.actionExecute_Project.setText(_translate("MainWindow", "Execute Project"))
        self.actionDisplay_Unit_Test_Results.setText(_translate("MainWindow", "Display Unit Test Results"))
        self.actionEnter_Unit_Tests.setText(_translate("MainWindow", "Enter Unit Tests"))
        self.actionEnter_Unit_Tests.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionDisplay_Test_Results.setText(_translate("MainWindow", "Display Test Results"))
        self.actionShow_Tutoruial.setText(_translate("MainWindow", "Show Tutorial"))
