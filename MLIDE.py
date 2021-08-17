#Could move much of this to separate files

import PyQt5
import sys
import json
import os
import copy
import math
import sys
import re
import random
import time
import datetime
from pathlib import Path
from datetime import datetime
from ast import literal_eval

from Objects.ProjectObject import Project
from Objects.UnitTestObject import UnitTest


from UI.CommentObject import Comment
import UI.baseUI
import UI.EnterUnitTests
import UI.UnitTestResults
import UI.SettingsPopup
import UI.LoadScreen
import UI.findReplace
import UI.ComplexityResultsUI
import UI.ComplexityLoading

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

		#As the user enters new functions, we store the tables of in/out etc values, function name and function filename associated with each new function, so these can later be stored in a UnitTest object. We save the gui object handles in case the user tries to delete the unit test later.
		self.ui.tables = []
		self.ui.functionNames = []
		self.ui.functionFiles = []
		self.ui.deleteButtons = []
		self.ui.horizontalLayouts = []
		self.ui.testButtons = []
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
		self.ui.functionNames.append(newFunctionName)
				
		horizontal = PyQt5.QtWidgets.QHBoxLayout(self)
		horizontal.addWidget(newFunctionName)
		delete_btn = PyQt5.QtWidgets.QPushButton(self)
		delete_btn.setText("Delete")
		delete_btn.setFixedSize(100,30)
		self.ui.deleteButtons.append(delete_btn)
		index = len(self.ui.tables)
		delete_btn.clicked.connect(lambda : self.removeFunction(index))
		horizontal.addWidget(delete_btn)
		self.ui.horizontalLayouts.append(horizontal)
		self.ui.Functions.addLayout(horizontal)
		
		#Create a label to show the file in which the function is stored
		newFunctionFile = PyQt5.QtWidgets.QLabel(self)
		newFunctionFile.setText("(in file " + self.ui.FunctionFileName.text() + ")")
		self.ui.functionFiles.append(newFunctionFile)
		self.ui.Functions.addWidget(newFunctionFile)		
		
		#Save the function name and file name for later
		self.functionFiles.append(self.ui.FunctionFileName.text())
		self.functionNames.append(self.ui.FunctionName.text())
		
		#Create a table which the user will be able to type input and output values into
		newFunctionTable = PyQt5.QtWidgets.QTableWidget(self)
		newFunctionTable.setRowCount(3) #To start with there is a row for types, a row for constraints and a row for one test. The user can add more test rows by clicking the button we are about to make.
		newFunctionTable.setColumnCount(self.ui.NumArguments.value()+1) #there is one column for each input argument to the new function plus 1 for output
		ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #We will label the arguments using capital letters from A to Z
		newFunctionTable.setHorizontalHeaderLabels(["Input" + ALPH[i] for i in range(self.ui.NumArguments.value())]+["Output"]) #Label the columns of the table as InputA, InputB, InputC etc. and then Output
		newFunctionTable.setVerticalHeaderLabels(["Types","Constraints"] + [str(i+1) for i in range(newFunctionTable.rowCount()-2)]) #Label the rows of the table as Types, Constraints, 1, 2, 3 ....
		self.ui.Functions.addWidget(newFunctionTable) #Add the table to the functions layout on screen 


		#Create a button for the user to add an additional test to this function, which will add another row to the table that we just created.
		newTestButton = PyQt5.QtWidgets.QPushButton(self)
		newTestButton.associatedTable = newFunctionTable
		newTestButton.clicked.connect(self.addTest)
		newTestButton.setText("Add test")
		self.ui.testButtons.append(newTestButton)
		self.ui.Functions.addWidget(newTestButton)
		self.ui.tables.append(newFunctionTable) #Save a reference to the table so we can iterate over its contents later once the user has finished editing it

		#reset		
		self.ui.FunctionName.setText("")
		self.ui.FunctionFileName.setText("")	
		self.ui.NumArguments.setValue(1)
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
			try:
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
						constr1 = literal_eval(table.item(1,k).text()) #Read the constraint from the table
					except: #If this occurs, there was a blank cell so just use [] as no constraint provided
						constr1 = []
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
						
				self.MainIDE.currentProject.unitTests.append(UnitTest(funcName,inputList,outputList,types,constraints, os.path.join(self.MainIDE.currentProject.directoryPath,fileName),self.MainIDE)) #Create a new UnitTest object based on all of the data that we have just collected, and add that to the currentProject
			except RuntimeError:#"wrapped C/C++ object of type QTableWidget has been deleted" - user doesn't want the test anymore
				pass
				

		self.MainIDE.currentProject.save()
		event.accept() #Now we've done the saving, allow the window to close as the user is expecting (as opposed to rejecting the event which would block the window from closing)

	def showExistingTests(self):
		"""Gets the existing tests from the current project and shows them to the user"""
		
		print("a")
		print(self.MainIDE.currentProject.unitTests)
		for test in self.MainIDE.currentProject.unitTests: #Loop over all tests that were previously created on the project; those that were saved to the project file.
			self.ui.FunctionName.setText(test.functionName) # Simulating the user typing in this stuff again is the quickest way in terms of providing code reuse.
			self.ui.FunctionFileName.setText(test.functionFileName)
			self.ui.NumArguments.setValue(test.numberOfInputs)
			self.addFunction() 
			newTable = self.ui.tables[-1]
			newTable.setRowCount(2+len(test.inputValues))
			newTable.setVerticalHeaderLabels(["Types","Constraints"] + [str(i+1) for i in range(newTable.rowCount()-2)]) #Label the rows of the table as Types, Constraints, 1, 2, 3 ....			
			#For every input and output display the type that we had saved
			for k in range(newTable.columnCount()):
				newTable.setItem(0,k,PyQt5.QtWidgets.QTableWidgetItem(test.types[k]))
				
			#For every column in the current table, set the second row to show the constraints on the user's arguments 
			for k in range(newTable.columnCount()):
				newTable.setItem(1,k,PyQt5.QtWidgets.QTableWidgetItem(str(test.inputConstraints[k]))) #Read the constraint from the table

			#Now all remaining rows after 1 and 2 simply represent tests. 
			for i in range(2,newTable.rowCount()): #For each test
				for k in range(newTable.columnCount()-1): #For every column in the current row, i.e. for every cell in the current test
						newTable.setItem(i,k,PyQt5.QtWidgets.QTableWidgetItem(test.inputValues[i-2][k])) #Set the test input to show on screen in the table
			
				#Grab the output for the current test and display it
				newTable.setItem(i,newTable.columnCount()-1,PyQt5.QtWidgets.QTableWidgetItem(test.outputValues[i-2])) #always appears in the last column of the table
		self.ui.FunctionName.setText("")
		self.ui.FunctionFileName.setText("")	
		self.ui.NumArguments.setValue(1)
		
		
	def removeFunction(self,funcToRemove):
	#	del self.functionNames[funcToRemove]	
	#	del self.functionFiles[funcToRemove]

		#Delete all ui objects in the popup for the current test
		self.ui.tables[funcToRemove].deleteLater()
		self.ui.functionNames[funcToRemove].deleteLater()
		self.ui.functionFiles[funcToRemove].deleteLater()
		self.ui.deleteButtons[funcToRemove].deleteLater()
		self.ui.horizontalLayouts[funcToRemove].deleteLater()
		self.ui.testButtons[funcToRemove].deleteLater()

#Implemented with help from https://stackoverflow.com/questions/54081118/pop-up-window-or-multiple-windows-with-pyqt5-qtdesigner/54081597
class UnitTestResultsPopup(PyQt5.QtWidgets.QDialog):
	"""Popup window which displays the results of executing the user's unit tests against their code"""
	def __init__(self,MainWindow): 
		"""Constructor - initialise UI"""
		super().__init__() #Call superclass constructor to get a dialogue box
		self.resultsUI = UI.UnitTestResults.Ui_Dialog() #Get the UI I have designed
		self.resultsUI.setupUi(self) #Set up the UI and fill it with the components it needs
		self.MainIDE = MainWindow #Save the main window of the IDE as an attribute of the popup object, which allows us to later access things like the currentProject
		
		#Set up the ctrlW shortcut for easy closing		
		ctrlW = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+W"),self)		
		ctrlW.activated.connect(self.close)	

	def show(self):
		"""Executes the UnitTests and then shows the popup with the results. Polymorphically extends the QDialog.show method"""
		EMOJI = {True:"✅",False:"❌"} #These emoticons are used for pass and fail on a test respectively.
		ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #We will label the user's function's arguments using capital letters from A to Z

		self.MainIDE.currentProject.save() #Start by saving the project so the user's code that we test is the most up to date
		self.setWindowTitle("Unit Test Results at " + str(datetime.now().strftime("%H:%M:%S"))) #https://www.programiz.com/python-programming/datetime/current-time
		
		for func in self.MainIDE.currentProject.unitTests: #for every function that we need to run tests against
			results, outputs, times = func.executeTests() #Get the results of the tests (list of bools) and the outputs of the tests

			#Create a label with a monospace font with the name of the function we are testing and add it to the dialogue box
			newFunctionName = PyQt5.QtWidgets.QLabel(self) 
			newFunctionName.setText(func.functionName+"():")
			newFunctionName.setObjectName("newFunctionName")
			newFunctionName.setStyleSheet("""		
			QLabel#newFunctionName {
				font-family: 'Consolas',Monospace;
				font-size: 11pt;
			}""")
			self.resultsUI.ResultsLayout.addWidget(newFunctionName)
		
			#Create a label to show the file in which the function is stored and add it to the dialogue box
			newFunctionFile = PyQt5.QtWidgets.QLabel(self)
			newFunctionFile.setText("(in file " + func.functionFileName + ")")
			self.resultsUI.ResultsLayout.addWidget(newFunctionFile)		
				
			#Create a table widget which will contain the results of the unit tests for one function
			newFunctionTable = PyQt5.QtWidgets.QTableWidget(self)
			newFunctionTable.setRowCount(len(func.inputValues)) #A row for each test
			newFunctionTable.setColumnCount(func.numberOfInputs+4) #there is one column for each input argument to the new function plus 1 for expected output, 1 for actual output and 1 for Pass/Fail and 1 for time
			newFunctionTable.setHorizontalHeaderLabels(["Input" + ALPH[i] for i in range(func.numberOfInputs)]+["Expected","Actual","Pass/Fail","Exe Time"]) 
			self.resultsUI.ResultsLayout.addWidget(newFunctionTable) #Display the table by adding it to the layout
			
			for testNo in range(len(func.inputValues)): # For every test that we need to execute against the function we are testing
				for argNo in range(func.numberOfInputs): #For every argument the function has 
					newFunctionTable.setItem(testNo,argNo,PyQt5.QtWidgets.QTableWidgetItem(func.inputValues[testNo][argNo])) #Set the test input to show on screen in the table
				
				newFunctionTable.setItem(testNo,func.numberOfInputs,PyQt5.QtWidgets.QTableWidgetItem(func.outputValues[testNo])) #Show the expected output value in the table
				newFunctionTable.setItem(testNo,func.numberOfInputs+1,PyQt5.QtWidgets.QTableWidgetItem(outputs[testNo])) #Show the actual output value in the table
				
				emoticon = PyQt5.QtWidgets.QTableWidgetItem(EMOJI[results[testNo]]) #Create a table widget item we can later put into the table to represent the pass/fail. We don't add it straight away as we want to style it based on whether or not the test had a positive result
				if results[testNo]: #The test passed
					emoticon.setBackground(PyQt5.QtGui.QColor("lime")) #green = positive
				else: #the test failed
					emoticon.setBackground(PyQt5.QtGui.QColor("darkred")) #red = negative
				newFunctionTable.setItem(testNo,func.numberOfInputs+2,emoticon) #Add the cell to the table so it is displayed
				newFunctionTable.setItem(testNo,func.numberOfInputs+3,PyQt5.QtWidgets.QTableWidgetItem(times[testNo])) #Add the cell to the table so it is displayed
				
		super().show() #Actually show the dialogue we've built by calling the superclass method.

##class ComplexityLoading(PyQt5.QtWidgets.QDialog):
##	"""A popup window which displays when the main complexity analysis window is loading"""
##	def __init__(self):
##		"""Constructor for the popup, which creates the graphics, initialises some variables, and sets up slots and shortcuts."""
##		super().__init__() #Call Qt QDialog constructor to get a dialogue box
##		self.ui = UI.ComplexityLoading.Ui_Dialog() #Load in the UI I have designed
##		#Set up UI and button onclicks
##		self.ui.setupUi(self)
##		self.show()


class ComplexityAnalysisPopup(PyQt5.QtWidgets.QDialog):
	"""A popup window which displays determined complexity for the functions in the user's code."""
	computed = PyQt5.QtCore.pyqtSignal()
	def __init__(self,MainIDE):
		"""Constructor for the popup, which creates the graphics, initialises some variables, and sets up slots and shortcuts."""
		super().__init__() #Call Qt QDialog constructor to get a dialogue box
		self.MainIDE = MainIDE # We store the MainIDE window associated with this popup so that later we can reference the currentProject
		
		self.ui = UI.ComplexityResultsUI.Ui_Dialog() #Load in the UI I have designed
		#Set up UI and button onclicks
		self.ui.setupUi(self)

		#Set up the ctrlW shortcut for easy closing		
		ctrlW = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+W"),self)		
		ctrlW.activated.connect(self.close)

	def disp(self,text):
		print("aa")
		self.ui.resultsTextBox.setHtml(text)

		




#Implemented with help from https://stackoverflow.com/questions/54081118/pop-up-window-or-multiple-windows-with-pyqt5-qtdesigner/54081597
class Settings(PyQt5.QtWidgets.QDialog):
	def __init__(self):
		super().__init__()
		self.ui = UI.SettingsPopup.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.closeButton.clicked.connect(self.close)
		self.settings = {}
		
		
		#Defaults:
		if sys.platform == "win32" or sys.platform == "cygwin":
			self.settings["pythonCommand"] = "py"
		else:
			self.settings["pythonCommand"] = "python3"		
		
		try:
			f = open(os.path.join(str(Path.home()),".mlidesettings"),"w+")
			self.settings = json.loads(f.read())
			f.close()
		except json.decoder.JSONDecodeError:
			pass #No settings file
			
	def closeEvent(self, event):
		self.settings["pythonCommand"] = self.ui.runCommand.text()
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
		}
		QTextEdit#lineNumberBox {
			font-family: 'Consolas',Monospace;
			font-size: 12pt;
			background-color: #ababab;
			text-align: right;
			color: white;
		}""")
							
		icon = PyQt5.QtGui.QIcon("./MlIcon.png")
		self.setWindowIcon(icon)		
	
		#Prepare popups
		self.enterUnitTests = UnitTestPopup(self)
		self.complexityAnalysisPopup = ComplexityAnalysisPopup(self)
		self.settings = Settings()
										
		self.highlighter = CodeFeatures.PythonSyntaxHighlighter(self.activeFileTextbox)
		self.justDeactivated = False
			
		self.shellInputBox.setPlaceholderText("Type input to the program here and press send. Works when program running.")
		
		self.findReplaceDialogue = UI.findReplace.findReplace(self)

		self.actionOpen_Settings.triggered.connect(self.showSettings)
		self.actionOpen_Project.triggered.connect(self.createCurrentProjectByOpening)
		self.actionNew_Project.triggered.connect(self.createCurrentProjectByNew)
		self.actionClose_IDE.triggered.connect(self.close)
		
		self.comments = []
		self.unwantedSuggestions = []
		
	def createCurrentProjectByOpening(self):
                mlideproj = PyQt5.QtWidgets.QFileDialog.getOpenFileName(directory=str(Path.home()),caption="Select an existing project (.mlideproj) to open")[0]
                try:
                        self.currentProject = Project(mlideproj,True,self)
                        self.setUpActions()
                except FileNotFoundError:
                        print("File issue")
                        pass
                
	def createCurrentProjectByNew(self):
		result = PyQt5.QtWidgets.QInputDialog.getText(self, "New Project","Please enter the name of the new project:")
		if result[1] == True:
			self.currentProject = Project(result[0],False,self)
			self.setUpActions()
			self.actionNew_File.trigger() #The user first has to create a new file
			
	def toggleFindReplace(self):
		"""Shows/hides the find/replace dialogue when the user presses ctrl-F or find/replace in the menu"""
		if self.findReplaceDialogue.visible: #if it is already showing then hide it
			self.commentsPane.takeAt(0) #Remove it from the layout it was in.
			self.findReplaceDialogue.hide() #Hide it on screen
			self.findReplaceDialogue.visible = False #save the state as not visible so that later we can use this to know whether to show or hide
			self.activeFileTextbox.setFocus() #Move the focus back to the active file textbox so the use can keep editing
			self.activeFileTextbox.setExtraSelections([]) #Remove the highlights made by the find tool
		else:#if it is hidden, show it
			self.commentsPane.insertWidget(0,self.findReplaceDialogue) #Add the find/replace GUI to the commentsPane layout at the top (position 0)
			self.findReplaceDialogue.show() #Show it
			self.findReplaceDialogue.visible = True #remember that it's visible
			self.findReplaceDialogue.findBox.setFocus() #Move the user's focus into the find box
			self.findReplaceDialogue.previousFind = "" #This value is used to know whether pressing the find button should start searching from the top of the file again or continue from the last match. We say that it should start again as the find value is compared against previousFind and it will be different to the blank string, leading to the find starting again from the top

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

		if self.activeFileTextbox.textCursor().block().length() == 0:
			print("newline")
		
		self.suggestSyntaxFeatures(self.activeFileTextbox.toPlainText())
		

	def showUnitTestEntry(self):
		self.enterUnitTests.show()
		
	def showSettings(self):
		self.settings.show()
	
	def showTestResults(self):
		self.utr = UnitTestResultsPopup(self)
		self.utr.show()
		
	def displayComplexityResults(self):
		self.complexityAnalysisPopup.show()

	def eventFilter(self, obj, event):
		"""Implemented using https://stackoverflow.com/questions/57698744/how-can-i-know-when-the-enter-key-was-pressed-on-qtextedit
		In Qt an event filter is an object which is allowed to receive events on behalf of another object before that object gets to see them. We set this class to be a filter for the active file textbox so that it can inspect keys pressed therein. We check for return/enter presses which require the calling of the OnNewline subroutine from the CodeFeatures file. 
		eventFilter is a special function name which is automatically called by Qt when events are produced 
		"""
		if event.type() == PyQt5.QtCore.QEvent.KeyPress and obj is self.activeFileTextbox: #If we got a keypressevent from the active file textbox
			if ((event.key() == PyQt5.QtCore.Qt.Key_Return) or (event.key() == PyQt5.QtCore.Qt.Key_Enter)) and self.activeFileTextbox.hasFocus(): #and the key pressed was either return (normal text enter key) or enter (on the number pad)
				CodeFeatures.onNewline(self.activeFileTextbox,self.lineNumberBox) #Call the subroutine that updates the line numbers and the indentation
				return True #The filtering was successful
				
		elif event.type() == PyQt5.QtCore.QEvent.KeyPress and obj is self.findReplaceDialogue.findBox:
			if ((event.key() == PyQt5.QtCore.Qt.Key_Return) or (event.key() == PyQt5.QtCore.Qt.Key_Enter)) and self.findReplaceDialogue.findBox.hasFocus(): 
				self.findReplaceDialogue.find()
				return True	

		return super().eventFilter(obj, event) #Otherwise we allow the event system to deal with the event itself.
			
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
		shortcut5 = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+G"),self)		
		shortcut5.activated.connect(self.actionFind_Replace.trigger)
		shortcut6 = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+H"),self)		
		shortcut6.activated.connect(self.actionFind_Replace.trigger)
		
		self.runButton.clicked.connect(self.currentProject.execute)
		self.runCommandBox.returnPressed.connect(self.currentProject.execute)
		self.inputButton.clicked.connect(self.currentProject.sendExecuteMessage)
		
		self.activeFileTextbox.verticalScrollBar().valueChanged.connect(self.lineNumberBox.verticalScrollBar().setValue) #Tell Qt that when the active file textbox scrolls, the line number textbox should scroll by the same amount so they always stay in line.
	
		#Setup right click menus:
		self.listOfFilesMenu.customContextMenuRequested.connect(self.displayRightClickMenu)
		self.activeFileTextbox.customContextMenuRequested.connect(self.displayRightClickMenu)
		self.EfficiencyHexagon.customContextMenuRequested.connect(self.displayRightClickMenu)		
		self.EleganceHexagon.customContextMenuRequested.connect(self.displayRightClickMenu)
		self.EfficacyHexagon.customContextMenuRequested.connect(self.displayRightClickMenu)		
		self.ReadabilityHexagon.customContextMenuRequested.connect(self.displayRightClickMenu)
		
		self.activeFileTextbox.cursorPositionChanged.connect(self.onMoveCursor)
		
		self.enterUnitTests.showExistingTests()
		
		self.activeFileTextbox.installEventFilter(self) #Allows this object to process events for the activeFileTextbox, meaning it can intercept certain keypresses needed to trigger subroutines.
		self.findReplaceDialogue.findBox.installEventFilter(self) #Allows this object to process events for the findReplaceDialogue, meaning it can intercept certain keypresses needed to trigger subroutines.
	
		self.actionFind_Replace.triggered.connect(self.toggleFindReplace)		
		
		self.actionCopy.triggered.connect(self.activeFileTextbox.copy)
		self.actionPaste.triggered.connect(self.activeFileTextbox.paste)
		
		self.actionFormat_Code.triggered.connect(lambda : self.activeFileTextbox.setPlainText(CodeFeatures.formatCode(self.activeFileTextbox.toPlainText())) )
		
		#Get initial score values
		self.EfficiencyHexagon.getScore()
		self.EfficacyHexagon.getScore(self.currentProject)
		self.EleganceHexagon.getScore()
		self.ReadabilityHexagon.getScore()
		
		self.actionDisplay_Complexity_Analyser_Results.triggered.connect(self.displayComplexityResults)

		self.actionEnter_Unit_Tests.triggered.connect(self.showUnitTestEntry)
		self.actionDisplay_Test_Results.triggered.connect(self.showTestResults)
		self.activeFileTextbox.textChanged.connect(self.onChangeText)
		self.runCommandBox.textChanged.connect(self.onChangeText)		

                #Source: https://realpython.com/python-pyqt-qthread/
                #Prepare the thread to run the ML components.
		self.thread = PyQt5.QtCore.QThread()
		self.updateScores = UpdateScoresAndComplexity(self)
		self.updateScores.moveToThread(self.thread)
		self.thread.started.connect(self.updateScores.update)
		self.updateScores.complexityDone.connect(self.complexityAnalysisPopup.disp)
		self.updateScores.finished.connect(self.thread.quit)
		self.updateScores.finished.connect(self.updateScores.deleteLater)
		self.thread.finished.connect(self.thread.deleteLater)
		self.thread.start()
        


	def onMoveCursor(self):
		pass #breaks undo/redo
		"""		#Highlight the current line
		formatToUse = PyQt5.QtGui.QTextBlockFormat() #Create a blank block format which will be applied to all blocks in the document to remove existing block-level format.
		start = self.activeFileTextbox.document().firstBlock()
		while start != self.activeFileTextbox.document().lastBlock(): #For all blocks in the document
			PyQt5.QtGui.QTextCursor(start).setBlockFormat(formatToUse) #Clear block level formatting
			start = start.next()
		PyQt5.QtGui.QTextCursor(start).setBlockFormat(formatToUse)			
		
		#Now create the highlight format with the correct colour and apply it to the current line's block
		formatToUse = PyQt5.QtGui.QTextBlockFormat()
		colourToUse = PyQt5.QtGui.QColor() #Create a QColor object which is a Qt-defined colour, which can accept colours in a variety of formats including hex.
		colourToUse.setNamedColor("#d9dedb")
		formatToUse.setBackground(colourToUse)
		PyQt5.QtGui.QTextCursor(self.activeFileTextbox.textCursor().block()).setBlockFormat(formatToUse)
		"""	
	def displayRightClickMenu(self,point): #(point is the point on screen that was clicked)
		"""Called when the customContextMenu requested signal is emitted by any of the widgets I have set to have a custom right click menu. Generates the correct right click menu based on the object that we right clicked on and returns that."""
		menu = PyQt5.QtWidgets.QMenu() #Create a new menu to populate with options
		sender = self.sender() #This is the widget which was right clicked on
		actions = [] #This will be a list of tuples -> text to display on right click menu and subroutine to execute when the text is clicked. We later iterate over all actions in this array and add them to the menu in one go. As it takes several lines of code to create and add an action it is more code-efficient to write it like this.
		
		if str(type(sender)) == "<class 'PyQt5.QtWidgets.QListWidget'>": #right clicked on a file in the list of files menu
			actions = [("Run file",self.currentProject.runFile),("Copy file path",lambda : setClipboardText(os.path.join(self.currentProject.directoryPath,sender.selectedItems()[0].text()))),("Switch to file",lambda : self.currentProject.switchToFile(sender.selectedItems()[0]))]
		elif sender == self.EfficiencyHexagon: #Right clicked on the efficiency hexagon
			actions = [("Access help to improve efficiency",self.EfficiencyHexagon.onRightClick)]
		elif sender == self.EleganceHexagon: #right clicked on the elegance hexagon
			actions = [("Access help to improve elegance",self.EleganceHexagon.onRightClick)]
		elif sender == self.ReadabilityHexagon: #right clicked on the readability hexagon
			actions = [("Access help to improve readability",self.ReadabilityHexagon.onRightClick)]
		elif sender == self.EfficacyHexagon: #right clicked on the efficacy hexagon
			actions = [("Access help to improve efficacy",self.EfficacyHexagon.onRightClick)]									
		elif sender == self.activeFileTextbox: #right clicked inside the active file textbox
			actions.append(("Paste",self.activeFileTextbox.paste))
			actions.append(("Display complexity analyser results",self.actionDisplay_Complexity_Analyser_Results.trigger))
			actions.append(("Display unit test results",self.actionDisplay_Test_Results.trigger))			
			if self.activeFileTextbox.textCursor().hasSelection(): #We can only do these actions if something is highlighted
				actions.append(("Copy",self.activeFileTextbox.copy))
				actions.append(("Generate code comments",ApplyCommentGeneration))
			
		for text,call in actions: #Now we are going to actually create and add all the actions to the menu
			action = PyQt5.QtWidgets.QAction(menu) #Create a new QAction which is a menu option that calls a function when trigered
			action.setText(text) #set the corresponding text for the option
			action.triggered.connect(call) #...and the subroutine to run when triggered 
			menu.addAction(action) #and add to menu

		menu.exec_(self.sender().mapToGlobal(point)) #Puts the menu on screen at the right point (mapToGlobal converts the position in the sender object to a global position so that the position at which the menu displays (arg to exec_) is where the user right clicked)

	def suggestSyntaxFeatures(self,codeToSuggestOn):
		"""Take the regex patterns defined in Syntax_Rules.txt and apply them to the user's code. In case of a match, create a comment reminding the user of what they could do to improve their code."""

		#Delete all existing suggestions and regenerate
		while len(self.comments) > 0: #We have to do it like this because when they die() they get removed from self.comments so we can't just iterate over as the array length would keep changing
			self.comments[0].die()
			
		with open("Syntax_Rules.txt","r") as f: #Contains the patterns to match and corresponding suggestions to make

			for line in f.readlines(): #Each line is one pattern-suggestion text pair.

				if line[0] == '#': #The pattern is "commented out" so skip it as it shouldn't be applied
					continue
				
				pattern = line.split(";;")[0] #regex to search for is first half
				commentText = line.split(";;")[1] #suggestion to show in case of match is second half
				
				for match in re.finditer(pattern,codeToSuggestOn):
				
					charNo = match.span()[0] #Character-level position of the match in the user's code. Will be used to calculate line number

					#If the user has previously rejected a suggestion on exactly the same block of code then don't apply it as they are obviously happy without the change
					matchedCode = match.group(0)					
					if matchedCode in self.unwantedSuggestions:
						continue
					
					#Compute the line number of the matched text from the returned char number provided by the re module
					for i,line in enumerate(codeToSuggestOn.split("\n")): #Loop over lines -> i is the line number from 0, line is the content
					
						charNo -= (len(line) +1) #Subtract the length of the line (+1 to count the \n which the split() command removed) from the character position so that....
						if charNo <= 0: #...when it gets to 0 or negative then the match must be on that line
							lineNo = i+2 #Adjust for the fact that we want the line numbers to start from 1 to match those displayed in the IDE
							break
					
					newComm = Comment("On line " + str(lineNo) + ", have you considered using " + commentText ,self.commentsPane,matchedCode) #Create a new comment with the correct message, referring to the correct part of the user's code
					newComm.ui.dismissButton.clicked.connect(self.unwantedComment) #Setup the event callback for when the user dismisses the suggestion
					newComm.deleted.connect(lambda : self.comments.remove(self.sender())) #Setup the event callback for when the comment is deleted to make sure that we remove it from self.comments such that this is always accurate
					
					self.comments.append(newComm) #Save a handle on the comment we just made for later e.g. for when we want to delete it
			
	def unwantedComment(self):
		"""Triggered when the user presses dismiss suggestion on a comment"""
		self.unwantedSuggestions.append(self.sender().comment.matchedCode) #Save the code that was matched to create that suggestion so that we don't accidentally create the same suggestion again.
		self.sender().comment.die() #Delete the comment, causing it to be removed from the screen and from the self.comments array via qt signal-slot events





class LoadScreen(PyQt5.QtWidgets.QMainWindow, UI.LoadScreen.Ui_MainWindow):
	def __init__(self, IDEWindow, parent=None):
		super(LoadScreen, self).__init__(parent)
		self.setupUi(self)
		icon = PyQt5.QtGui.QIcon("./MlIcon.png")
		self.setWindowIcon(icon)	
		self.setFixedSize(self.size())
		self.IDEWindow = IDEWindow
		
		
		self.setStyleSheet("""
		QWidget {
			font-family:calibri,Ubuntu,sans-serif;
			font-size: 11pt;
		}""")
		
		self.newProjectButton.clicked.connect(self.new)
		self.openProjectButton.clicked.connect(self.open)

		shortcut = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+O"),self)
		shortcut2 = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+N"),self)
		shortcut.activated.connect(self.openProjectButton.click)
		shortcut2.activated.connect(self.newProjectButton.click)
		
		
		#Set up the ctrlW shortcut for easy closing		
		ctrlW = PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence("Ctrl+W"),self)		
		ctrlW.activated.connect(self.close)
				
		#Add ctrl L for learn?
	def open(self):
		self.hide()
		self.IDEWindow.show()
		self.IDEWindow.actionOpen_Project.trigger()
	
	def new(self):
		self.hide()
		self.IDEWindow.show()
		self.IDEWindow.actionNew_Project.trigger()
def DisplayComplexityAnalyserResults():
	pass
	
def ApplyCommentGeneration():
	pass
def setClipboardText(text):
	global app
	app.clipboard().setText(text)

#Source: https://realpython.com/python-pyqt-qthread/
class UpdateScoresAndComplexity(PyQt5.QtCore.QObject):
	finished = PyQt5.QtCore.pyqtSignal()
	complexityDone = PyQt5.QtCore.pyqtSignal(str)


	def __init__(self,mainWindow):
		self.mainWindow = mainWindow
		super().__init__()

	def EstimateCodeComplexity(self,unitTest):
		"""Estimates the complexity of the function attached to the unitTest provided"""
		STEPS = 5 #MAINTENANCE: This is the number of different inputs for which the user's function will be tested before we try to get a result
		ATTEMPTS = 10 #MAINTENANCE: This is the number of times we will run the tests, averaging over each time.

		#MAINTENANCE: These are the functions whose values are used to determine the complexity of the code based on the time taken - which is it proportional to? You can add more complexities as long as the position in the COMPLEXITY_FUNCTIONS list of the function matches the position in the FUNCTION_STRINGS list of the name.
		COMPLEXITY_FUNCTIONS = [lambda a : 1,lambda a : math.log(a), lambda a: a, lambda a: a*math.log(a),lambda a : a**2] 
		FUNCTION_STRINGS = ["1","logn","n","nlogn","n^2","2^n"]
		
		start = random.randint(1,10) #Initialise valid minimum and maximum values
		end = random.randint(400000,410000)
		for constraint in unitTest.inputConstraints[0]:
			if constraint[0] == "Range" or constraint[0] == "Length": #Check if the user has specified a constraint on the length of a string or the range of an integer. In that case we should only try values in that range/strings of that length range. 
				start = constraint[1]
				end = constraint[2]		
		
		difference = end-start #total input space we have to make measurements
		inpStep = difference // STEPS #We take several time measurements with different n values (as in O(n))
		ns = [] #n values as in O(n^2 etc)
		times = []  #times it takes with corresponding n values

		#For each measurement we need to make, time run the subroutine and time its execution
		for i in range(start+inpStep,end,inpStep): #Try to avoid starting with a really low value as this can be highly influenced by anomalous factors like caching etc.
			ns.append(i) #Save the n value so we can later use this to compute the complexity
		
			try:
				mockInput = unitTest.generateMockInput(i) #This input will be fed to the function and its execution on this input timed
				totalTime = 0 #Stores the total time taken over all ATTEMPTS 
				for att in range(ATTEMPTS):
					output, time = unitTest.executeFunction([str(mockInput)]) #FUTURE RELEASE: Currently only 1-argument functions support complexity estimation
					if output == "ERROR":
						return "ERROR IN CODE" #When the code errors there is no way to know about the complexity
					totalTime += float(time)
				times.append(totalTime/ATTEMPTS) #Save average time at this level of input
				
			except Exception as e: #For some reason mock input could not be generated so an exception was thrown by the mock input generation function. We can present this to the user as it contains more details
				return str(e)

		minimumCost = float('inf') #the cost of the best fitting complexity routine to the user's code (the lower the cost value the closer the complexity function matches the user's code times)
		bestFunction = "" #The name of the complexity function which best fits the subroutine
		
		for funcName, function in zip(FUNCTION_STRINGS,COMPLEXITY_FUNCTIONS):
			cf_applied = list(map(function,ns)) #Apply the complexity function to all of the n values we used.
			divided = [times[i]/cf_applied[i] for i in range(len(times)) ] #The time taken to run the function should be proportional to f(n) where f() is the correct complexity function, meaning t = kf(n) so k = t/f(n). Therefore the correct complexity function will have the most similar values in this divided array
			
			#we now need to find the function which has the most constant value in the divided array. Sort the results from low to high, then taking the total of the differences between successive results.               
			results = sorted(divided)
			costOfThisFunction = 0
			for i in range(1,len(results)):
				costOfThisFunction += (results[i] - results[i-1])
			costOfThisFunction /= results[-1]
			
			#As we process through all functions which could be the complexity of this one, we need to keep track of the most realistic choice.
			if costOfThisFunction < minimumCost:
				minimumCost = costOfThisFunction
				bestFunction = funcName
		

		return bestFunction		
					
	def prepareComplexity(self):
		"""Computes, renders and shows the results of analysing the complexity of the user's subroutines, in a new popup window."""
		outputText = "<p>Complexity of ≈ <ul>" #This variable contains the text that will be shown in the main textbox of the popup
		uts = self.mainWindow.currentProject.unitTests
		for ut in uts: #Code complexity estimation is performed on a UnitTest object
		         result = self.EstimateCodeComplexity(ut) #The complexity estimation
		         outputText += "<li>&nbsp;"+ut.functionName+"():&nbsp;&nbsp;&nbsp;&nbsp;<span style='background-color:#c7c7c7;font-family: Consolas,Monospace;'>O(" +result+")</span></li>" #Creates a bullet point with the function name and complexity. nbsp = non breaking space (https://www.wikihow.com/Insert-Spaces-in-HTML)

		outputText += "</ul><br>Last computed at "+ str(datetime.now().strftime("%H:%M:%S")) +"<br />Disclaimer - complexity estimated by empirical observation and so may be inaccurate.</p>" #close remaining tags to get correctly formed HTML before showing on screen #https://www.programiz.com/python-programming/datetime/current-time
		self.complexityDone.emit(outputText)
		print("KoP")

	def update(self):
		"""Updates scores and complexity analysis estimates. This runs in a separate thread so as to prevent it from freezing the GUI"""

		self.prepareComplexity()
##                SCORE_COMPUTE_FREQUENCY = 5000 #MAINTENANCE : This is the number of milliseconds between updates of the scores. 
##		self.scoreComputeTimer = PyQt5.QtCore.QTimer() #Create a timer to trigger score updates (only updating every few seconds gives time for computations to finish without freezing computer - could be slow - and is less distracting for user) 
##		self.scoreComputeTimer.timeout.connect(self.EfficiencyHexagon.getScore)
##		self.scoreComputeTimer.timeout.connect(lambda : self.EfficacyHexagon.getScore(self.currentProject))
##		self.scoreComputeTimer.timeout.connect(self.EleganceHexagon.getScore)
##		self.scoreComputeTimer.timeout.connect(self.ReadabilityHexagon.getScore)
##		self.scoreComputeTimer.start(SCORE_COMPUTE_FREQUENCY) #Timer will fire the timeout event every SCORE_COMPUTE_FREQUENCY milliseconds
##		
		self.finished.emit()



app = PyQt5.QtWidgets.QApplication(sys.argv)
IDE_Window = MLIDE()
	
if len(sys.argv) == 2: #When the user double clicks on an mlideproj file in windows or when they put the file as the cmd line arg this occurs
	IDE_Window.show()
	IDE_Window.currentProject = Project(sys.argv[1],True,IDE_Window)
	IDE_Window.setUpActions()
else:
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
		   
