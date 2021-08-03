import PyQt5
import PyQt5.uic
class findReplace(PyQt5.QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		PyQt5.uic.loadUi("findReplace.ui", self)
		self.visible = False

