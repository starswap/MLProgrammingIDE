#It appears that the conversion to python may be redundant. We might be able to just use importUI or something
#Could move much of this to UI file

import PyQt5
import sys
import json
import os
import copy
from pathlib import Path

from Objects.ProjectObject import Project
from Objects.UnitTestObject import UnitTest

import UI.baseUI
import UI.EnterUnitTests
import UI.SettingsPopup
import UI.LoadScreen

import CodeFeatures

#Implemented with help from https://stackoverflow.com/questions/54081118/pop-up-window-or-multiple-windows-with-pyqt5-qtdesigner/54081597
class UnitTestPopup(PyQt5.QtWidgets.QDialog):
	"""A popup window which allows the user to enter unit tests and have them stored in the current project."""
	def __init__(self,MainIDE):
		"""Constructor for the popup, which creates the graphics, initialises some variables, and sets up slots and shortcuts."""
		super().__init__() #Call Qt QDialog constructor to get a dialogue box
		self.MainIDE = MainIDE # We store the MainIDE window associated with this popup so that later we can reference the currentProject
		
		self.ui = UI.EnterUnitTests.Ui_Dialog() #Load in the UI I have designed

		#Set up UI and button onclicks
		self.ui.setupUi(self)		
		self.ui.closeButton.clicked.connect(self.close)
		self.ui.addFunctionButton.clicked.connect(self.addFunction)

		#As the user enters new functions, we store the tables of in/out etc values, function name and function filename associated with each new function, so these can later be stored in a UnitTest object.
		self.ui.tables = []
		self.functionNames = []
		self.functionFiles = []
		
		#Set up the ctrlW shortcut for easy closing		
		ctrlW = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+W"),self)		
		ctrlW.activated.connect(self.close)
		
	def addFunction(self):
		"""Triggered by the user clicking the Add Function button inside the Unit Test Popup box. Takes the data about the function (name, filename, number of inputs etc) provided by the user and uses this to create a table they can fill in with unit tests, a label with the name and filename of the function, and a button for adding more tests to the new function. The input data for function name etc. is saved inside this object's state, to later be put into a UnitTest object"""
		
		#Create a label to show the function's name, set the font to be a monospace font, size 11pt.
		newFunctionName = PyQt5.QtWidgets.QLabel(self)
		newFunctionName.setText(self.ui.FunctionName.text()+"():")
		newFunctionName.setObjectName("newFunctionName")
		newFunctionName.setStyleSheet("""		
		QLabel#newFunctionName {
			font-family: 'Consolas',Monospace;
			font-size: 11pt;
		}""")
		self.ui.Functions.addWidget(newFunctionName)
		
		#Create a label to show the file in which the function is stored
		newFunctionFile = PyQt5.QtWidgets.QLabel(self)
		newFunctionFile.setText("(in file " + self.ui.FunctionFileName.text() + ")")
		self.ui.Functions.addWidget(newFunctionFile)		
		
		#Save the function name and file name for later
		self.functionFiles.append(self.ui.FunctionFileName.text())
		self.functionNames.append(newFunctionName.text())
		
		#Create a table which the user will be able to type input and output values into
		newFunctionTable = PyQt5.QtWidgets.QTableWidget(self)
		newFunctionTable.setRowCount(3) #To start with there is a row for types, a row for constraints and a row for one test. The user can add more test rows by clicking the button we are about to make.
		newFunctionTable.setColumnCount(self.ui.NumArguments.value()+1) #there is one column for each input argument to the new function plus 1 for output
		ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #We will label the arguments using capital letters from A to Z
		newFunctionTable.setHorizontalHeaderLabels(["Input" + ALPH[i] for i in range(self.ui.NumArguments.value())]+["Output"]) #Label the columns of the table as InputA, InputB, InputC etc. and then Output
		newFunctionTable.setVerticalHeaderLabels(["Types","Constraints"] + [str(i+1) for i in range(newFunctionTable.rowCount()-2)]) #Label the rows of the table as Types, Constraints, 1, 2, 3 ....
		self.ui.Functions.addWidget(newFunctionTable) #Add the table to the functions layout on screen 
		self.ui.tables.append(newFunctionTable) #Save a reference to the table so we can iterate over its contents later once the user has finished editing it
		
		#Create a button for the user to add an additional test to this function, which will add another row to the table that we just created.
		newTestButton = PyQt5.QtWidgets.QPushButton(self)
		newTestButton.associatedTable = newFunctionTable
		newTestButton.clicked.connect(self.addTest)
		newTestButton.setText("Add test")
		self.ui.Functions.addWidget(newTestButton)
	
	def addTest(self):
		"""Adds an additional row to the table associated with the New Test button whose clicking led to this method being called (see newTestButton.clicked.connect)"""
		sender = self.sender() #The button object that was clicked, causing this signal to be sent
		sender.associatedTable.setRowCount(sender.associatedTable.rowCount()+1) #Add an additional row to the table by increasing the row count by 1.
		sender.associatedTable.setVerticalHeaderLabels(["Types","Constraints"] + [str(i+1) for i in range(sender.associatedTable.rowCount()-2)]) # Relabel the rows of the table so that the new row also has a label.

	def closeEvent(self, event):
		"""Triggered when the user closes the dialogue box by clicking the 'Save and Close' button, clicking the x button in the corner, or pressing ctrl-W. Saves the unit tests that the user has just entered into a UnitTest object which is attached to the current project"""
		
		self.MainIDE.currentProject.unitTests = [] #Reset the unit tests to be empty as we will refill them based on everything the user has put into this window.
	
		#For every table that we created, i.e. for every function the user has made a unit test for, ...	
		for j in range(len(self.ui.tables)):
			table = self.ui.tables[j] #Get the current table
			funcName = self.functionNames[j] #Get the name of the current function
			inputList = [] # Prepare a list of inputs to the function
			outputList = [] #Prepare a list of outputs from the function
			types = [] #Prepare a list of types of the function inputs.
			constraints = [] #Prepare a list of constraints on the function inputs
			fileName = self.functionFiles[j] #Get the filename for the file in which the current function is stored
			
			#For every column in the current table, use the first row to get the types of the user's arguments
			for k in range(table.columnCount()):
				try:
					type1 = table.item(0,k).text() #Read the type from the table
				except AttributeError: #If this occurs, there was a blank cell so we just use "", as no type was provided
					type1 = ""
				types.append(type1) #Save the type that we just got and then get the next one.
				
			#For every column in the current table, use the second row to get the constraints on the user's arguments 
			for k in range(table.columnCount()):
				try:
					constr1 = table.item(1,k).text() #Read the constraint from the table
				except AttributeError: #If this occurs, there was a blank cell so just use "" as no constraint provided
					constr1 = ""
				constraints.append(constr1) #Save the current constraint and then we can get the next one
				
			#Now all remaining rows after 1 and 2 simply represent tests. 
			for i in range(2,table.rowCount()): #For each test

				thisInput = [] #Prepare a list to store one test's worth of input 
				for k in range(table.columnCount()-1): #For every column in the current row, i.e. for every cell in the current test
					try:
						thisInput.append(table.item(i,k).text()) #Get the test input
					except AttributeError: #Blank cell...
						thisInput.append("") #... so use ""
				inputList.append(thisInput) #Add all the inputs we just collected to the overall list of input lists 

				#Grab the output for the current test
				try:
					outputList.append(table.item(i,table.columnCount()-1).text()) #always appears in the last column of the table
				except AttributeError: #Blank cell so use ""
					outputList.append("")
					
			self.MainIDE.currentProject.unitTests.append(UnitTest(funcName,inputList,outputList,types,constraints,fileName)) #Create a new UnitTest object based on all of the data that we have just collected, and add that to the currentProject

		self.MainIDE.currentProject.save()
		event.accept() #Now we've done the saving, allow the window to close as the user is expecting (as opposed to rejecting the event which would block the window from closing)

	def showExistingTests(self):
		"""Gets the existing tests from the current project and shows them to the user"""
		
		for test in self.MainIDE.currentProject.unitTests: #Loop over all tests that were previously created on the project; those that were saved to the project file.
			self.ui.functionName.setText(test.funcName)
			self.ui.FunctionFileName.setText(test.funcFileName)
			self.addFunction() ????
			newTable = self.ui.tables[-1]
			newTable.setRowCount(2+len(test.inputValues))
			#For every input and output display the type that we had saved
			for k in range(newTable.columnCount()):
				table.item(0,k).setText(test.types[k])
				
			#For every column in the current table, set the second row to show the constraints on the user's arguments 
			for k in range(table.columnCount()):
				table.item(1,k).setText(test.inputConstraints) #Read the constraint from the table

			#Now all remaining rows after 1 and 2 simply represent tests. 
			for i in range(2,table.rowCount()): #For each test
				for k in range(table.columnCount()-1): #For every column in the current row, i.e. for every cell in the current test
						table.item(i,k).setText(test.inputValues[i][k]) #Set the test input to show on screen in the table
			
				#Grab the output for the current test and display it
				table.item(i,table.columnCount()-1).setText(test.outputValues[i]) #always appears in the last column of the table
	

class Settings(PyQt5.QtWidgets.QDialog):
	def __init__(self):
		super().__init__()
		self.ui = UI.SettingsPopup.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.closeButton.clicked.connect(self.close)
		self.settings = {}
		
		#Defaults:
		if sys.platform == "win32" or sys.platform == "cygwin":
			self.settings["runFileCommand"] = "py"
		else:
			self.settings["runFileCommand"] = "python3"		
		
		try:
			f = open(os.path.join(str(Path.home()),".mlidesettings"),"w+")
			self.settings = json.loads(f.read())
			f.close()
		except json.decoder.JSONDecodeError:
			pass #No settings file
	def closeEvent(self, event):
		self.settings["runFileCommand"] = self.ui.fileRun.text()
		f = open(os.path.join(str(Path.home()),".mlidesettings"),"w")
		f.write(json.dumps(self.settings))
		f.close()
		event.accept()



#Implemented with help from https://pythonbasics.org/qt-designer-python/
class MLIDE(PyQt5.QtWidgets.QMainWindow, UI.baseUI.Ui_MainWindow):
	def __init__(self, parent=None):
		#Move to UI file probs
		
		super(MLIDE, self).__init__(parent)
		self.setupUi(self)
		self.setStyleSheet("""
		QWidget {
			font-family:calibri,Ubuntu,sans-serif;
			font-size: 11pt;
		}
		QTextEdit#activeFileTextbox {
			font-family: 'Consolas',Monospace;
			font-size: 12pt;
		}
		QLineEdit#runCommandBox {
			font-family: 'Consolas',Monospace;
			font-size: 11pt;
			font-weight: bold;
		}
		QPlainTextEdit#shellInputBox {
			font-family: 'Consolas',Monospace;
			font-size: 11pt;
		}		
		QPlainTextEdit#outputWindow {
			font-family: 'Consolas',Monospace;
			font-size: 11pt;
		}""")
							
		icon = PyQt5.QtGui.QIcon("./MlIcon.png")
		self.setWindowIcon(icon)		
	
		self.actionEnter_Unit_Tests.triggered.connect(self.showUnitTestEntry)
		self.actionOpen_Settings.triggered.connect(self.showSettings)
		self.actionOpen_Project.triggered.connect(self.createCurrentProjectByOpening)
		self.actionNew_Project.triggered.connect(self.createCurrentProjectByNew)
		self.actionClose_IDE.triggered.connect(self.close)
		self.activeFileTextbox.textChanged.connect(self.onChangeText)
		self.runCommandBox.textChanged.connect(self.onChangeText)
										
		self.highlighter = CodeFeatures.PythonSyntaxHighlighter(self.activeFileTextbox)
		self.justDeactivated = False
	
		#Prepare popups
		self.enterUnitTests = UnitTestPopup(self)		
		self.settings = Settings()
		
		self.shellInputBox.setPlaceholderText("Type input to the program here and press send. Works when program running.")

	def createCurrentProjectByOpening(self):
		self.currentProject = Project(PyQt5.QtWidgets.QFileDialog.getOpenFileName(directory=str(Path.home()),caption="Select an existing project (.mlideproj) to open")[0],True,self)
		self.setUpActions()
		
	def createCurrentProjectByNew(self):
		result = PyQt5.QtWidgets.QInputDialog.getText(self, "New Project","Please enter the name of the new project:")
		if result[1] == True:
			self.currentProject = Project(result[0],False,self)
			self.setUpActions()

	def onChangeText(self): #in display score module
		if len(self.activeFileTextbox.toPlainText()) == 0:
			self.EfficacyHexagon.deactivate(True)
			self.EleganceHexagon.deactivate(True)
			self.EfficiencyHexagon.deactivate(True)
			self.ReadabilityHexagon.deactivate(True)
			self.justDeactivated = True
			
		elif self.justDeactivated == True:
			self.justDeactivated = False
			self.EfficacyHexagon.activate(True)
			self.EleganceHexagon.activate(True)
			self.EfficiencyHexagon.activate(True)
			self.ReadabilityHexagon.activate(True)		
		
		if hasattr(self, "currentProject"):
			self.currentProject.saveToProject()

	def showUnitTestEntry(self):
		self.enterUnitTests.show()
		
	def showSettings(self):
		self.settings.show()
		
	def setUpActions(self):
		self.listOfFilesMenu.itemClicked.connect(self.currentProject.switchToFile)
		self.actionSave_Project.triggered.connect(self.currentProject.save)
		self.actionNew_File.triggered.connect(lambda : self.currentProject.newFile(PyQt5.QtWidgets.QInputDialog.getText(self, "New File","Please enter the name of the new file:")[0]))
		self.actionAdd_File_to_Project.triggered.connect(lambda : self.currentProject.addFile(PyQt5.QtWidgets.QFileDialog.getOpenFileName(directory=str(Path.home()))[0]))			
		self.actionExecute_Project.triggered.connect(self.currentProject.execute)
	
		shortcut = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+Return"),self)
		shortcut2 = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+Enter"),self)
		shortcut.activated.connect(self.currentProject.sendExecuteMessage)
		shortcut2.activated.connect(self.currentProject.sendExecuteMessage)
		shortcut3 = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+R"),self)
		shortcut3.activated.connect(self.runCommandBox.setFocus)
		shortcut4 = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+I"),self)		
		shortcut4.activated.connect(self.shellInputBox.setFocus)
		self.runButton.clicked.connect(self.currentProject.execute)
		self.runCommandBox.returnPressed.connect(self.currentProject.execute)
		self.inputButton.clicked.connect(self.currentProject.sendExecuteMessage)
	
		#Setup right click menus:
		self.listOfFilesMenu.customContextMenuRequested.connect(self.displayRightClickMenu)
		
		self.enterUnitTests.showExistingTests()??????????????
	
	def displayRightClickMenu(self,point):
		menu = PyQt5.QtWidgets.QMenu()
		sender = self.sender()
		if str(type(sender)) == "<class 'PyQt5.QtWidgets.QListWidget'>":
			actions = [("Run file",self.currentProject.runFile),("Copy file path",lambda : setClipboardText(os.path.join(self.currentProject.directoryPath,sender.selectedItems()[0].text())))]

		for text,call in actions:
			action = PyQt5.QtWidgets.QAction(menu)
			action.setText(text)
			action.triggered.connect(call)
			menu.addAction(action)

		menu.exec_(self.sender().mapToGlobal(point))			
	
class LoadScreen(PyQt5.QtWidgets.QMainWindow, UI.LoadScreen.Ui_MainWindow):
	def __init__(self, IDEWindow, parent=None):
		super(LoadScreen, self).__init__(parent)
		self.setupUi(self)
		icon = PyQt5.QtGui.QIcon("./MlIcon.png")
		self.setWindowIcon(icon)	
		self.setFixedSize(self.size())
		self.IDEWindow = IDEWindow
		
		self.newProjectButton.clicked.connect(self.new)
		self.openProjectButton.clicked.connect(self.open)
	
	def open(self):
		self.hide()
		self.IDEWindow.show()
		self.IDEWindow.actionOpen_Project.trigger()
	
	def new(self):
		self.hide()
		self.IDEWindow.show()
		self.IDEWindow.actionNew_Project.trigger()
	
def setClipboardText(text):
	global app
	app.clipboard().setText(text)

app = PyQt5.QtWidgets.QApplication(sys.argv)
IDE_Window = MLIDE()
Load_Screen = LoadScreen(IDE_Window)
Load_Screen.show()
app.exec_()

"""		
		font = PyQt5.QtGui.QFont("Monospace");
		font.setStyleHint(PyQt5.QtGui.QFont.TypeWriter);
		font.setPointSize(12)
		self.activeFileTextbox.setFont(font)
		font2 = PyQt5.QtGui.QFont("Monospace");
		font2.setStyleHint(PyQt5.QtGui.QFont.TypeWriter);
		font2.setPointSize(11)
		font2.setWeight(PyQt5.QtGui.QFont.Bold)
		self.runCommandBox.setFont(font2)
		font3 = PyQt5.QtGui.QFont("Monospace");		
		font3.setStyleHint(PyQt5.QtGui.QFont.TypeWriter);
		font3.setPointSize(11)
		self.shellInputBox.setFont(font3)
		self.outputWindow.setFont(font3)
		
"""
		   
