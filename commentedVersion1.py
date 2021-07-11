from PyQt5 import QtCore, QtGui, QtWidgets #Import graphics library
class Ui_MainWindow(object):
    """The main window class is used by the Qt graphics library to create the main window of the program"""
    def setupUi(self, MainWindow): 
        """Creates the user interface elements"""
        #Set window title and size
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 675)
        
	#The central widget is the main part of the UI which is displayed in the middle of the program. This is the main window in this case
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Create the list of files menu and scale it to be the right shape
        self.listOfFilesMenu = QtWidgets.QListWidget(self.centralwidget)
        self.listOfFilesMenu.setGeometry(QtCore.QRect(0, 30, 141, 541))
        
        #Set the size policy and stretches of the elements in the scene. This is necessary make sure objects take up the corerct amount of space.
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.listOfFilesMenu.sizePolicy().hasHeightForWidth())
        self.listOfFilesMenu.setSizePolicy(sizePolicy)
        self.listOfFilesMenu.setObjectName("listOfFilesMenu")
        
        #Create the run button as a green push button of the correct size and place it in the right place
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(0, 0, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setStyleSheet("background-color:rgb(115, 210, 22);")
        self.runButton.setObjectName("runButton")
        
        #Create the run command box as a plain text box and set its size and position
        self.runCommandBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.runCommandBox.setGeometry(QtCore.QRect(150, 0, 291, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.runCommandBox.sizePolicy().hasHeightForWidth())
        self.runCommandBox.setSizePolicy(sizePolicy)
        self.runCommandBox.setObjectName("runCommandBox")
        
        #Create the code box as a text box (allows rich text formatting) and set the size and position
        self.codeBox = QtWidgets.QTextEdit(self.centralwidget)
        self.codeBox.setGeometry(QtCore.QRect(160, 30, 411, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.codeBox.sizePolicy().hasHeightForWidth())
        self.codeBox.setSizePolicy(sizePolicy)
        self.codeBox.setObjectName("codeBox")
        
        #Create the area on which the line numbers will be drawn (by a QPainter object) as a QWidget and set the shape and location. The choice of a QPainter method is recommended by Qt here:https://doc.qt.io/qt-5/qtwidgets-widgets-codeeditor-example.html
        self.lineNumberArea = QtWidgets.QWidget(self.centralwidget)
        self.lineNumberArea.setGeometry(QtCore.QRect(140, 30, 21, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.lineNumberArea.sizePolicy().hasHeightForWidth())
        self.lineNumberArea.setSizePolicy(sizePolicy)
        self.lineNumberArea.setStyleSheet("background-color:rgb(211, 215, 207)")
        self.lineNumberArea.setObjectName("lineNumberArea")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        #Set up the menu bar to be displayed at the top of the screen and the options within it.
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 22))
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
        self.actionShow_Tutorial = QtWidgets.QAction(MainWindow)
        self.actionShow_Tutorial.setObjectName("actionShow_Tutorial")
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
        self.actionExecute = QtWidgets.QAction(MainWindow)
        self.actionExecute.setObjectName("actionExecute")
        self.actionEnter_Unit_Tests = QtWidgets.QAction(MainWindow)
        self.actionEnter_Unit_Tests.setObjectName("actionEnter_Unit_Tests")
        self.actionDisplay_Test_Results = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Test_Results.setObjectName("actionDisplay_Test_Results")
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
        self.menuRun.addAction(self.actionExecute)
        self.menuUnit_Tests.addAction(self.actionEnter_Unit_Tests)
        self.menuUnit_Tests.addAction(self.actionDisplay_Test_Results)
        self.menuHelp.addAction(self.actionShow_Tutorial)
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
        
        #Use the translator object to translate the text to display on each of the menu options into the target language (which doesn't change them as English is the target language)
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.runButton.setText(_translate("MainWindow", "Run Program"))
        self.runCommandBox.setPlainText(_translate("MainWindow", "e.g. python3 myFile.py"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuUnit_Tests.setTitle(_translate("MainWindow", "Unit Tests"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionShow_Tutorial.setText(_translate("MainWindow", "Show Tutorial"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionAdd_File_to_Project.setText(_translate("MainWindow", "Add File to Project"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionFind_Replace.setText(_translate("MainWindow", "Find/Replace"))
        self.actionFormat_Code.setText(_translate("MainWindow", "Format Code"))
        self.actionExecute.setText(_translate("MainWindow", "Execute"))
        self.actionEnter_Unit_Tests.setText(_translate("MainWindow", "Enter Unit Tests"))
        self.actionDisplay_Test_Results.setText(_translate("MainWindow", "Display Test Results"))
