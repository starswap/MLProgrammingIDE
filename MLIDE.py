#It appears that the conversion to python may be redundant. We might be able to just use importUI or something
#Could move much of this to UI file
import PyQt5
import sys
import UI.baseUI
import UI.EnterUnitTests
#import Objects.UnitTestObject
import Objects.ProjectObject
from pathlib import Path
import CodeFeatures
from Objects.HexagonObject import Hexagon

#Implemented with help from https://stackoverflow.com/questions/54081118/pop-up-window-or-multiple-windows-with-pyqt5-qtdesigner/54081597
class UnitTestPopup(PyQt5.QtWidgets.QDialog):
	def __init__(self):
	        super().__init__()
	        self.ui = UI.EnterUnitTests.Ui_Dialog()
	        self.ui.setupUi(self)
	        self.ui.addFunctionButton.clicked.connect(self.addFunction)
	        self.unitTests = [] #Will go to project obj probs.
	        self.ui.tables = []
	        self.ui.functionNames = []
	        self.ui.closeButton.clicked.connect(self.close)

	def addFunction(self):#Will go in the new UnitTest constructor
		newFunctionName = PyQt5.QtWidgets.QLabel(self)
		newFunctionName.setText(self.ui.FunctionName.text()+"():")
		font = PyQt5.QtGui.QFont()
		font.setFamily("Tlwg Mono")
		font.setPointSize(11)
		newFunctionName.setFont(font)
		self.ui.Functions.addWidget(newFunctionName)
		self.ui.functionNames.append(newFunctionName)
		
		newFunctionTable = PyQt5.QtWidgets.QTableWidget(self)
		newFunctionTable.setRowCount(1)
		newFunctionTable.setColumnCount(self.ui.NumArguments.value()+1)
		ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		newFunctionTable.setHorizontalHeaderLabels([ALPH[i] for i in range(self.ui.NumArguments.value())]+["Output"])
		self.ui.Functions.addWidget(newFunctionTable)
		self.ui.tables.append(newFunctionTable)
		
		newTestButton = PyQt5.QtWidgets.QPushButton(self)
		newTestButton.associatedTable = newFunctionTable
		newTestButton.clicked.connect(lambda : newTestButton.associatedTable.setRowCount(newTestButton.associatedTable.rowCount()+1))
		newTestButton.setText("Add test")
		self.ui.Functions.addWidget(newTestButton)

	def closeEvent(self, event):
		for j in range(len(self.ui.tables)):
			table = self.ui.tables[j]
			print(self.ui.functionNames[j].text())
			for i in range(table.rowCount()):
				for k in range(table.columnCount()):
					try:
						print(table.item(i,k).text())
					except AttributeError:
						print("Blank cell")
		print("You closed the popup")
		event.accept()

#Implemented with help from https://pythonbasics.org/qt-designer-python/
class MLIDE(PyQt5.QtWidgets.QMainWindow, UI.baseUI.Ui_MainWindow):
	def __init__(self, parent=None):
		#Move to UI file probs
		super(MLIDE, self).__init__(parent)
		self.setupUi(self)
		icon = PyQt5.QtGui.QIcon("./MlIcon.png")
		self.setWindowIcon(icon)		
	
		self.actionEnter_Unit_Tests.triggered.connect(self.showUnitTestEntry)
		self.actionOpen_Project.triggered.connect(self.createCurrentProjectByOpening)
		self.actionNew_Project.triggered.connect(self.createCurrentProjectByNew)
		self.actionClose_IDE.triggered.connect(self.close)
		self.activeFileTextbox.textChanged.connect(self.onChangeText)
		self.runCommandBox.textChanged.connect(self.onChangeText)
										
		self.highlighter = CodeFeatures.PythonSyntaxHighlighter(self.activeFileTextbox)
		self.justDeactivated = False
	
	def createCurrentProjectByOpening(self):
		self.currentProject = Objects.ProjectObject.Project(PyQt5.QtWidgets.QFileDialog.getOpenFileName(directory=str(Path.home()))[0],True,self)
		self.setUpActions()
		
	def createCurrentProjectByNew(self):
		result = PyQt5.QtWidgets.QInputDialog.getText(self, "New Project","Please enter the name of the new project:")
		if result[1] == True:
			self.currentProject = Objects.ProjectObject.Project(result[0],False,self)
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
		self.enterUnitTests = UnitTestPopup()
		self.enterUnitTests.show()
		
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
def main():
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	form = MLIDE()
	form.show()
	app.exec_()
main()
