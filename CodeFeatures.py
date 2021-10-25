import PyQt5
import re
import math
import MachineLearning.autocomplete
class PythonSyntaxHighlighter(PyQt5.QtGui.QSyntaxHighlighter):
	"""Performs syntax highlighting on the text typed in the active file textbox. Subclass of QSyntaxsHighlighter, which performs all the styling using the predefined method setFormat(start,length,format). We override highlightBlock which is called automatically by Qt, to add our own styling rules"""
	def __init__(self,associatedTextEdit):
		"""Constructor - set up highlighter and define colour constants"""
		#Run superclass constructor
		super().__init__(associatedTextEdit.document())
		
		#(maintenance) To change the syntax highlight colours, change these constants
		self.COMMENT = "#999999"
		self.KEYWORD = "#ff9900"
		self.BOOL = "#0000ff"
		self.DEF_FUNC = "#cc4125"
		self.STRING = "#20124d"
		self.USER_FUNC = "#274e13"
		self.BACKGROUND_COLOR = "#FFFFFF"
		self.DEFAULT_TEXT_COLOR = "#000000"

		#Define the things we will highlight as language keywords, bools and default functions
		self.LANGUAGE_KEYWORDS = ["for","if","def","lambda","while","await","else","elif","import","pass","break","except","in","raise","class","finally","is","return","and","continue","try","as","from","assert","del","global","not","with","async","or","yield"]  # Source https://www.programiz.com/python-programming/keyword-list 
		self.DEFAULT_FUNCTIONS = ["abs\(","delattr\(","hash\(","memoryview\(","set\(","all\(","dict\(","help\(","min\(","setattr\(","any\(","dir\(","hex\(","next\(","slice\(","ascii\(","divmod\(","id\(","object\(","sorted\(","bin\(","enumerate\(","input\(","oct\(","staticmethod\(","bool\(","eval\(","int\(","open\(","str\(","breakpoint\(","exec\(","isinstance\(","ord\(","sum\(","bytearray\(","filter\(","issubclass\(","pow\(","super\(","bytes\(","float\(","iter\(","print\(","tuple\(","callable\(","format\(","len\(","property\(","type\(","chr\(","frozenset\(","list\(","range\(","vars\(","classmethod\(","getattr\(","locals\(","repr\(","zip\(","compile\(","globals\(","map\(","reversed\(","__import__\(","complex\(","hasattr\(","max\(","round"] #https://docs.python.org/3/library/functions.html
		self.BOOL_HIGHLIGHTS = ["False","True","None"]
		
		#Set the background colour and default text color as specified by the constants above
		associatedTextEdit.setStyleSheet("background-color: "+self.BACKGROUND_COLOR + "; color: " + self.DEFAULT_TEXT_COLOR + ";")	
		
	def highlightBlock(self,lineToHighlight):
		"""Called by Qt - performs the actual highlighting."""
		

		formatToUse = PyQt5.QtGui.QTextCharFormat() #Create a QTextCharFormat object, which is an object specifying settings (e.g. color, boldness etc) of text, which we can apply to the textedit text.
		colourToUse = PyQt5.QtGui.QColor() #Create a QColor object which is a Qt-defined colour, which can accept colours in a variety of formats including hex.
		formatToUse.setFontWeight(PyQt5.QtGui.QFont.Bold) #Set the highlight format to be bold until we say otherwise.

	#Highlight language keywords
		colourToUse.setNamedColor(self.KEYWORD) #Prepare the colour
		formatToUse.setForeground(colourToUse)
		for keyword in self.LANGUAGE_KEYWORDS: #For each possbile keyword that could appear
			for occur in re.finditer("(^|[\\t ])+("+keyword+")([: ]|$)",lineToHighlight,flags=re.MULTILINE): #For every time it appears (the regex here says at least 1 tab or space or the line beginning then the keyword)
				self.setFormat(occur.start(1),len(keyword)+1,formatToUse)#Format the keyword

	#Highlight all functions in the user defined colour. We will afterwards go through and rehighlight any default functions in their colour.
		colourToUse.setNamedColor(self.USER_FUNC) #Prepare the colour
		formatToUse.setForeground(colourToUse)			
		for occur in re.finditer("(^|[\\t ])+?([^ ]+)\(",lineToHighlight,flags=re.MULTILINE): #the regex here says at least one tab or space or the line beginning then at least one character which isn't a space (which is the identifier name) then a bracket to signify that it must be function.
			self.setFormat(occur.span(2)[0],occur.span(2)[1]-occur.span(2)[0],formatToUse) #style the identifier
	
	#Highlight all predefined functions
		colourToUse.setNamedColor(self.DEF_FUNC)
		formatToUse.setForeground(colourToUse)						
		for func in self.DEFAULT_FUNCTIONS:
			for occur in re.finditer("(^|[\\t ])+("+func+")",lineToHighlight,flags=re.MULTILINE): #This regex says at least one start of line, tab or space character, then the function.
				self.setFormat(occur.start(2),len(func)-2,formatToUse)
				colourToUse.setNamedColor(self.DEF_FUNC)
	
	#Highlight the boolean values
		colourToUse.setNamedColor(self.BOOL)		
		formatToUse.setForeground(colourToUse)						
		for boo in self.BOOL_HIGHLIGHTS:
			for occur in re.finditer("(^|[\\t ])+("+boo+")",lineToHighlight,flags=re.MULTILINE): #this regex is the same as the above one
				self.setFormat(occur.start(2),len(boo),formatToUse)

	#Highlight strings
		#Prepare the color format
		colourToUse.setNamedColor(self.STRING)
		formatToUse.setForeground(colourToUse)
		#Look for single quotes that start a string
		quotes = [q.start() for q in re.finditer("(?<!\\\)'",lineToHighlight)] #Because finditer returns a generator you have to convert to list. See https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
		#If there are an odd number of quotes in the line the string is as yet unfinished so we need to highlight all the way to the end of the line. This can be done by assumning there was a quote after the end of the line.
		if len(quotes) % 2 == 1:
			quotes.append(len(lineToHighlight))
		for i in range(0,len(quotes),2): #For every other quote in the string
			self.setFormat(quotes[i],quotes[i+1]-quotes[i]+1,formatToUse) #Highlight from this quote to the next one			
		#Repeat for strings demarcated by double quotes
		doubleQ = [q.start() for q in re.finditer("(?<!(\\\))(?<!(\"\"))\"",lineToHighlight)] #The regular expression used here and above uses negative lookbehind. This specifies a character (here a backslash) which cannot appear before the match. If it does the match is discarded. A second lookbehind discards any matches preceded by two more quotes because these are triple quotes, dealt with later. The main pattern aside from the lookbehinds simply looks for a ". When using this regex inside a Python string, some additional backslashes are added to escape the backslash which escapes the backslashes and then also to escape the quotes. The net result of this is that the syntax highlighting doesn't get messed up if you put an escaped quote inside a string,  
		if len(doubleQ) % 2 == 1:
			doubleQ.append(len(lineToHighlight))
		for i in range(0,len(doubleQ),2):
			self.setFormat(doubleQ[i],doubleQ[i+1]-doubleQ[i]+1,formatToUse)		
	
	#Highlight sharp comments
		formatToUse.setFontWeight(PyQt5.QtGui.QFont.Normal)		
		colourToUse.setNamedColor(self.COMMENT)
		formatToUse.setForeground(colourToUse)
		if lineToHighlight.find("#") != -1:
			self.setFormat(lineToHighlight.find("#"),len(lineToHighlight)-lineToHighlight.find("#"),formatToUse) #We don't need regexes here as you can only have one sharp comment per line so Python's find subroutine will suffice.
	
	#Highight triple quote docstrings
		self.setCurrentBlockState(self.previousBlockState()) #The QSyntaxHighlighter parent class provides a "currentBlockState" attribute which can be set to any integer. This is so that you can track multiline highlights such as with these docstrings. When it is set to -1, no special state is set, and when it is set to 1 I have chosen to take that to mean we are currently doing a triple quote comment.
		tripleQComment = [0]+[q.start() for q in re.finditer('"""',lineToHighlight)] #find all triple quotes. Set the start of the string to be a quote so that if the previous line had a triple quote on it then we highlight from the beginning of this line to the first triple quote on this line.
		for i in range(1,len(tripleQComment)):  #for every triple quote (we have to iterate starting at the 1th element because we use i-1 in the loop)
			if self.currentBlockState() == 1: #if we are inside a comment, we just hit the end of it as we just hit a triple quote
				self.setFormat(tripleQComment[i-1],tripleQComment[i]-tripleQComment[i-1]+3,formatToUse)	#so now we can highlight it as we know where it ends
				self.setCurrentBlockState(-1) #We are no longer inside a triple quote comment
			else: #We are not inside a triple quote comment but we just hit a triple quote so ....
				self.setCurrentBlockState(1) #... now we are
		#At the end, if we are one """ short, the comment must continue onto the next line. Therefore we should highlight all of the rest of this line. When the next line is highlighted we will deal with the need to continue highlighting at the start of that one.		
		if self.currentBlockState() == 1:
			self.setFormat(tripleQComment[-1],len(lineToHighlight)-tripleQComment[-1]+3,formatToUse)	

def onNewline(activeFileBox,lineNumbersBox):
	"""Runs every time the user presses the return or enter key inside the active file textbox. Does two things:
		1. Indents the new line so that the indentation matches the previous line, reduced if there was a return on the previous line and increased if there was a colon
		2. Checks if we need to add more line numbers to the line number box and if so adds them
	"""
	
	if activeFileBox.document().lineCount() == lineNumbersBox.document().lineCount(): #If, before adding the new line the user requested by pressing enter, we have the same number of lines in the active file textbox as line numbers in the line number box, when we add a new line we will need a new line number...
		lineNumbersBox.append(str(lineNumbersBox.document().lineCount()+1)) #... so put the next line number into the line number box

	prevLine = activeFileBox.textCursor().block().text() #The line before the newline. We will check to see how many tabs this contains and if it contains any modifiers (: or return) which would change the number of tabs in the next line.
	
	whereNewLineOccurred = activeFileBox.textCursor().positionInBlock() #Find out at which point in the line the user's cursor was when they pressed etner.
	if whereNewLineOccurred != 0: #By default the above method returns the position after the one we are interested in (the end of the line before) as this is where the cursor is. The exception is when enter is pressed at the beginning of an existing line, in which case 0 is returned as expected. 
		whereNewLineOccurred -= 1 #Correct for this defect.
	
	if len(prevLine) > 0 and prevLine[whereNewLineOccurred] == ":": #If the last line ends in a colon
		newTabs = 1 #We need to put one extra indent on the next line
	elif "\treturn " in prevLine: #If the last line is a return statement we drop out of a function call
		newTabs = -1 #and so there should be one fewer tab on the next line
	else: #If neither of these are present then we don't need to modify it
		newTabs = 0

	#Count the number of tabs at the front of the previous line and add this to the amount we wanted to modify by
	for char in prevLine: 
		if char == "\t":
			newTabs += 1
		else:
			break #The first time a character we check is not a tab, we break out of the loop so that we only check for tabs at the front of the line and not elsewhere in the line

	oldCurPos = activeFileBox.textCursor().position() #We need to save the position of the cursor as...
	activeFileBox.setPlainText(activeFileBox.toPlainText()[:oldCurPos] + "\n"+ ("\t"*newTabs) +activeFileBox.toPlainText()[oldCurPos:]) #... when we update the contents of the active file textbox by replacing the existing text with a new text containing the added tabs, we lose the position of the cursor, which just moves to the top of the file.
	
	newCur = activeFileBox.textCursor() #Take the textCursor
	newCur.setPosition(oldCurPos+1+newTabs) #Set its position to be where it was before we messed about with the contents of the textbox, adjusted for the added tabs, 
	activeFileBox.setTextCursor(newCur) #And re-apply it to the textbox.
	
def formatCode(code):
	"""Takes a string of python code and adds tab characters where it thinks they will be needed in order to ensure that the code is correctly indented. Note that this can only ever be a guess as it depends on the logic of the program that the user has designed"""
	lines = code.split("\n") #We will successively compute on each line of the code so first split to lines
	currentIndent = 0 #This value stores the correct indent we think the current line should have
	outputText = "" #This string is the result of the formatting which will be built up throughout the function call and then returned at the end.
	lastIf = 0 #Stores the indentation level of the most recent if command.
	lastTry = 0 #stores the indentation level of the most recent try command
	
	for line in lines:
		#Count how many tabs are already present at the beginning of the current line
		existingTabs = 0 
		for char in line: 
			if char == "\t":
				existingTabs += 1
			else:
				break

		if ("elif " in line) or ("else:" in line): #If this line is an elif or an else, we should automatically demote it to the same indentation as the previous if which it matches with
			currentIndent = lastIf
		elif ("except " in line) or ("finally:" in line) or ("except:" in line): #Make sure excepts and finallys match trys in indent
			currentIndent = lastTry
		
		if existingTabs > currentIndent: #More tabs than expected
			line = line[(existingTabs-currentIndent):] #So reduce by the delta
		elif existingTabs < currentIndent: #Fewer tabs than expected
			line = "\t"*(currentIndent-existingTabs) + line #So increase by the delta
			
		outputText += line + "\n" #Save the new version of the current line in the accumulator variable we will return
		
		if len(line) > 0 and line[-1] == ":": #the line endswith a colon so the right indent increases by one in Python for the NEXT line
			if "if " in line: #If we have an if command, save the current indentation level so we can later jump back to match this on a corresponding elif or else.
				lastIf = currentIndent
			elif ("try:") in line: #If we have a try command, save the indent so except and finally can later be matched up
				lastTry = currentIndent
			
			currentIndent += 1 
		elif "\treturn " in line: #A return was detected so we should drop the required indent by one for the next line
			currentIndent -= 1
		
	return outputText #The result of this function (the returned outputText value) is then put into the active file textbox to replace the existing unformatted code


#Implemented with help from https://doc.qt.io/qt-5/qtwidgets-tools-customcompleter-example.html (C++)
class codeEditor(PyQt5.QtWidgets.QTextEdit):
	"""Subclasses QTextEdit to provide code editor functionality for use in my IDE. Notably, tab autocomplete is handled correctly"""
	def __init__(self,parent):
		"""Constructor for the codeEditor class"""
		super().__init__(parent) #Superclass constructor to initialise a QTextEdit widget
		self.show() #Make it visible
		
		self.prepareCompleter() #Setup the code autocompleter
		self.completerActive = True #By default completions are in use
		self.currentTabs = 0

		
	def prepareCompleter(self):
		"""Initialises the code autocompletion functionality by creating a Qcompleter object and styling it correctly"""
		self.completer = PyQt5.QtWidgets.QCompleter(self)
		self.completer.setWidget(self) #Tells the QCompleter it is providing completions on the codeEditor widget (activeFileTextbox)
		self.completer.setCompletionMode(PyQt5.QtWidgets.QCompleter.PopupCompletion) #Tell is to show completion options as a popup next to the text typed by the user

		#Colour it purple and make the font size and style the same as the rest of the text in the activeFileTextbox
		self.completer.popup().setStyleSheet("""
		QListView {
			background-color:WHITE;
			border-radius: 4px;
			color: black;
			border-color: black;
			font-size: 11pt;
			font-family:calibri,Ubuntu,sans-serif;
		}
""")
		self.completer.activated.connect(self.fillInCompletion) #When the user selects a completion, we should call this method
		self.completerActive = True
		
	def displayAutocompleteSuggestions(self):#Needed as otherwise spams completions. #Include as version
		"""Gets the autocomplete suggestions from the machine learning algorithm that produces them and displays them in the completer"""
		if self.completerActive: #Only if the completer is active should we display suggestions
			currentLineText = self.textCursor().block().text() #Get text of current line where cursor is positioned

			#Get suggestions and set model with the completions and the current text put together
			self.currentTabs = currentLineText.count("\t")
			self.completer.setModel(PyQt5.QtCore.QStringListModel([currentLineText.replace("\t","") + sug for sug in MachineLearning.autocomplete.suggestAutocomplete(currentLineText.replace("\t",""))]))
			self.completer.popup().setCurrentIndex(self.completer.completionModel().index(0, 0)) #Start selecting at top
			self.completer.popup().setFocusPolicy(PyQt5.QtCore.Qt.NoFocus)
                        
			#Get where the cursor is and make the completer display in the correct place
			#Implemented with help from https://doc.qt.io/qt-5/qtwidgets-tools-customcompleter-example.html (C++)
			rectangle = self.cursorRect()
			rectangle.setWidth(self.completer.popup().sizeHintForColumn(0)+ 50 + self.completer.popup().verticalScrollBar().sizeHint().width())
			self.completer.complete(rectangle)

	def fillInCompletion(self,textToComplete):
		"""When the user selects a completion, we will fill it in so that the code in the IDE changes to that"""

		#Remove the existing data before replacing it with the completed data
		cursor = self.textCursor();
		cursor.select(PyQt5.QtGui.QTextCursor.LineUnderCursor)
		cursor.removeSelectedText()
		cursor.insertText("\t"*self.currentTabs+ textToComplete)
		self.setTextCursor(cursor)
		
	def keyPressEvent(self,event):#Implemented with help from https://doc.qt.io/qt-5/qtwidgets-tools-customcompleter-example.html (C++)
		"""Called by Qt when a key is pressed on a codeEditor object"""
		
		if (self.completer.popup().isVisible()): #a completion is available
			if event.key() == PyQt5.QtCore.Qt.Key_Tab: #Let the Qcompleter object deal with tab presses
				event.ignore()
				return
			if event.key() == PyQt5.QtCore.Qt.Key_Enter or event.key() == PyQt5.QtCore.Qt.Key_Return: #Let the Qcompleter object deal with return/enter presses...
					#...but make sure to deactivate the completer so that we don't get multiple completions on the same line
					self.completer.popup().hide()
					self.completerActive = False
					event.ignore()
					return  
			if event.key() == PyQt5.QtCore.Qt.Key_Escape: #Let the Qcompleter object deal with escape presses
				event.ignore()
				return

			else: #another unrecognised key was pressed
				super().keyPressEvent(event) #we can leave the handling of this to the QTextEdit class.
				
		else: #no completions are shown
			if event.key() == PyQt5.QtCore.Qt.Key_Enter or event.key() == PyQt5.QtCore.Qt.Key_Return: #enter/return pressed
				#reactivate the completer for the new line
				self.completerActive = True
				#update line numbers box and indentation
				onNewline(self,self.lineNumberBox)
				self.displayAutocompleteSuggestions()
				event.accept() #the event has been processed so no-one else needs to process it

	
			else: #another unrecognised key was pressed
				super().keyPressEvent(event) #we can leave the handling of this to the QTextEdit class.
				
