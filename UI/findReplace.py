import PyQt5
import PyQt5.uic
import re
class findReplace(PyQt5.QtWidgets.QWidget):
	"""Handles the IDE's find-replace feature, providing the GUI and the functionality behind this."""
	def __init__(self,assocWindow):#Takes the main window as an argument so it can access parts of the main window UI (namely the active file textbox)
		super().__init__() #Initialise the superclass so that the UI is rendered
		PyQt5.uic.loadUi("findReplace.ui", self) #Grab the UI from the XML file that stores it
		
		#Set attributes
		self.visible = False #Currently hidden
		self.associatedWindow = assocWindow #Save so we can access elsewhere in the object
		
		#Set up actions when you click the buttons
		self.closeButton.clicked.connect(self.associatedWindow.toggleFindReplace) #When the close button is clicked we should toggle the box's appearance i.e. hide it. This subroutine found in main MLIDE class
		self.findNextButton.clicked.connect(self.find) 
		self.replaceButton.clicked.connect(self.replace)
		
		self.MATCH_HIGHLIGHT_COLOUR = "#e8f716" # (Maintenance) This is the colour that matches are highlighted in.
		self.highlightCol = PyQt5.QtGui.QColor()
		self.highlightCol.setNamedColor(self.MATCH_HIGHLIGHT_COLOUR)
		self.previousFind = ""
		
	def find(self):
		if self.previousFind != self.findBox.toPlainText():
			self.gen = self.findInternals()
			next(self.gen)
		else:
			try:
				next(self.gen)
			except StopIteration:
				self.gen = self.findInternals()
				next(self.gen)
		self.previousFind = self.findBox.toPlainText()
	
	def findInternals(self):
		"""References:
			https://programtalk.com/python-examples/PyQt5.QtWidgets.QTextEdit.ExtraSelection/
			https://stackoverflow.com/questions/21122928/selecting-a-piece-of-text-using-qtextcursor
		"""
		selections = []
		results = []
		toFind = self.findBox.toPlainText()
		if not(self.regex.isChecked()):
			toFind = re.escape(toFind)
			print("a")
		print(toFind)
		for result in re.finditer(toFind,self.associatedWindow.activeFileTextbox.toPlainText(),flags=re.MULTILINE):
			selection = PyQt5.QtWidgets.QTextEdit.ExtraSelection()
			selection.format.setBackground(self.highlightCol)
			cur = self.associatedWindow.activeFileTextbox.textCursor()
			cur.setPosition(result.span(0)[0], PyQt5.QtGui.QTextCursor.MoveAnchor)
			cur.setPosition(result.span(0)[1], PyQt5.QtGui.QTextCursor.KeepAnchor)
			selection.cursor = cur
			selections.append(selection)
			results.append(result)
		self.associatedWindow.activeFileTextbox.setExtraSelections(selections)
		
		for result in results:
			cur = self.associatedWindow.activeFileTextbox.textCursor()
			cur.setPosition(result.span(0)[0], PyQt5.QtGui.QTextCursor.MoveAnchor)
			cur.setPosition(result.span(0)[1], PyQt5.QtGui.QTextCursor.KeepAnchor)
			self.associatedWindow.activeFileTextbox.setTextCursor(cur)
			yield
			
	def replace(self):
		if self.associatedWindow.activeFileTextbox.textCursor().hasSelection():
			self.previousFind = ""
			self.associatedWindow.activeFileTextbox.textCursor().insertText(self.replaceBox.toPlainText())
			
