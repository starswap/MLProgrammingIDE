#It appears that the conversion to python may be redundant. We might be able to just use setupUi
#Could move much of this to UI file
import PyQt5
import sys
import version1
import EnterUnitTests
import UnitTestEntryFunction

#def test():
#	print("hop")

#Implemented with help from https://stackoverflow.com/questions/54081118/pop-up-window-or-multiple-windows-with-pyqt5-qtdesigner/54081597
class UnitTestPopup(PyQt5.QtWidgets.QDialog):
	def __init__(self):
	        super().__init__()
	        self.ui = EnterUnitTests.Ui_Dialog()
	        self.ui.setupUi(self)
	        self.ui.addFunctionButton.clicked.connect(self.addFunction)
	        self.unitTests = [] #Will go to project obj probs.

	def addFunction(self):#Will go in the new UnitTest constructor
		newFunctionName = PyQt5.QtWidgets.QLabel(self)
		newFunctionName.setText(self.ui.FunctionName.text()+"():")
		font = PyQt5.QtGui.QFont()
		font.setFamily("Tlwg Mono")
		font.setPointSize(11)
		newFunctionName.setFont(font)
		self.ui.Functions.addWidget(newFunctionName)
		
		newFunctionTable = PyQt5.QtWidgets.QTableWidget(self)
		newFunctionTable.setColumnCount(3)
		newFunctionTable.setRowCount(3)
		self.ui.Functions.addWidget(newFunctionTable)
		




#Implemented with help from https://pythonbasics.org/qt-designer-python/
class MLIDE(PyQt5.QtWidgets.QMainWindow, version1.Ui_MainWindow):
	def __init__(self, parent=None):
		super(MLIDE, self).__init__(parent)
		self.setupUi(self)
		self.actionEnter_Unit_Tests.triggered.connect(self.showUnitTestEntry)
	def showUnitTestEntry(self):
		self.enterUnitTests = UnitTestPopup()
		self.enterUnitTests.show()
def main():
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	form = MLIDE()
	form.show()
	app.exec_()
main()
