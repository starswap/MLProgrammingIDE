import PyQt5
import PyQt5.uic
class findReplace(PyQt5.QtWidgets.QWidget):
	def __init__(self,assocWindow):
		super().__init__()
		PyQt5.uic.loadUi("findReplace.ui", self)
		self.visible = False
		self.associatedWindow = assocWindow
		self.closeButton.clicked.connect(self.associatedWindow.toggleFindReplace)
					
	def findReplace(self):
		for result in re.finditer(self.findBox,self.associatedWindow.activeFileTextbox.toPlainText(),flags=re.MULTILINE)
		
