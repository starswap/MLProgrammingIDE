#It appears that the conversion to python may be redundant. We might be able to just use importUI or something
#Could move much of this to UI file
import PyQt5
import sys
import UI.baseUI
import UI.EnterUnitTests
#import Objects.UnitTestObject
import Objects.ProjectObject
#from UnitTestObject import UnitTest
#def test():
#	print("hop")

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
		super(MLIDE, self).__init__(parent)
		self.setupUi(self)
		icon = PyQt5.QtGui.QIcon("./MlIcon.png")
		self.setWindowIcon(icon)		
	
		self.actionEnter_Unit_Tests.triggered.connect(self.showUnitTestEntry)
		self.actionOpen_Project.triggered.connect(self.createCurrentProjectByOpening)
	
	def createCurrentProjectByOpening(self):
		self.currentProject = Objects.ProjectObject.Project(PyQt5.QtWidgets.QFileDialog.getOpenFileName()[0],True,self)
		
	def showUnitTestEntry(self):
		self.enterUnitTests = UnitTestPopup()
		self.enterUnitTests.show()
def main():
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	form = MLIDE()
	form.show()
	app.exec_()
main()
