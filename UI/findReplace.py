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
		self.highlightCol = PyQt5.QtGui.QColor() #Create a QColor and apply the hex colour set in the constant above (the Qt methods taking colours require QColors)
		self.highlightCol.setNamedColor(self.MATCH_HIGHLIGHT_COLOUR)
		
		self.previousFind = "" #Stores the previous thing that we tried to find so that when we search for something next time we know whether to move to the next match of the same thing (pick up where we left off) or search for something new. This decides whether to call next() on the generator or create a new generator in the find method.
		
	def find(self):
		"""Called when the user presses the find button or presses enter in the find box. Creates a new generator object using the findInternals method, or advances the existing one to find the next match"""
		if self.previousFind != self.findBox.toPlainText(): #If the thing we are searching for now is different to the thing we searched for the last time, we can't go to the next match of the previous one; we need to make a new search.
			self.gen = self.findInternals() #Create a generator which will highlight over successive matches of the target string, and save it to a property of the object so that we can access it in later calls of this method.
			next(self.gen) #Advance to the first match found.
		else: #We are searching for the same thing as last time so we want to move to the next match
			try:
				next(self.gen) #Move the generator on one step
			except StopIteration: #There are no more matches to be found so we reset the generator and start from the top again (allowing the user to loop over matches from bottom to top)
				self.gen = self.findInternals()
				next(self.gen)
				
		self.previousFind = self.findBox.toPlainText() #Save the thing we searched for this time so that next time we can check if this has changed
	
	def findInternals(self):
		"""References:
			https://programtalk.com/python-examples/PyQt5.QtWidgets.QTextEdit.ExtraSelection/
			https://stackoverflow.com/questions/21122928/selecting-a-piece-of-text-using-qtextcursor
		A generator function which finds all matches and highlights them in the colour defined by MATCH_HIGHLIGHT_COLOUR, then successively selects matches and yields back to the calling code until the user presses find again.
		"""
		
		selections = [] #Will be a list of ExtraSelection objects - these are objects storing additional formatting to be applied to sections of a document in a QTextEdit, with the format and text to apply to
		toFind = self.findBox.toPlainText() #The string to find, extracted from the find text box in the GUI
		if not(self.regex.isChecked()): #The string is not a regex
			toFind = re.escape(toFind) #so we need to escape any regex characters so that when we treat it as a regex it still does what the user expects

		for result in re.finditer(toFind,self.associatedWindow.activeFileTextbox.toPlainText(),flags=re.MULTILINE): #Find all matches and iterate over them (re.finditer is generator-based)
			selection = PyQt5.QtWidgets.QTextEdit.ExtraSelection() #Create a new ExtraSelection detailing where the match is and the colour to highlight it
			selection.format.setBackground(self.highlightCol) #Set the colour to highlight with
			
			#Set the region we want to highlight (the range of the match)
			cur = self.associatedWindow.activeFileTextbox.textCursor() 
			cur.setPosition(result.span(0)[0], PyQt5.QtGui.QTextCursor.MoveAnchor)
			cur.setPosition(result.span(0)[1], PyQt5.QtGui.QTextCursor.KeepAnchor)
			selection.cursor = cur
			
			#Save the selection so we can apply it later, in bulk with all of the others
			selections.append(selection)
			
		self.associatedWindow.activeFileTextbox.setExtraSelections(selections) # Apply all highlights
		
		#Now we have highlighted every match, iterate over them, selecting them so the user can replace as necessary. This is the generator part.
		for result in re.finditer(toFind,self.associatedWindow.activeFileTextbox.toPlainText(),flags=re.MULTILINE):  

			#Select the match using the cursor of the activeFileTextbox so that the user actually sees the match selected
			cur = self.associatedWindow.activeFileTextbox.textCursor()
			cur.setPosition(result.span(0)[0], PyQt5.QtGui.QTextCursor.MoveAnchor)
			cur.setPosition(result.span(0)[1], PyQt5.QtGui.QTextCursor.KeepAnchor)
			self.associatedWindow.activeFileTextbox.setTextCursor(cur)
			
			yield #Pause the loop until the next time the user presses the find/next button
			
	def replace(self):
		"""Replaces the selected text in the activeFileTextbox (the current match) with the thing to replace with."""
		if self.associatedWindow.activeFileTextbox.textCursor().hasSelection(): #Only if something is selected (if not then the user hasn't pressed find first so it makes no sense to try and replace)
			self.associatedWindow.activeFileTextbox.textCursor().insertText(self.replaceBox.toPlainText()) #Insert the replacement where the match is highlighted
			self.previousFind = "" #Reset the find so that it starts again. This is because otherwise the highlights go wrong as the length of the text in the activefiletextbox changes but the highlights are done by position and so the wrong text is highlighted. By reseting the find we update the highlights based on the new text of the active file textbox.
			
