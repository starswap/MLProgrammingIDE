import PyQt5
from to_precision import to_precision
import random

class Hexagon(PyQt5.QtWidgets.QWidget):
	def __init__(self,parent,resourceURLs=[""],startScore=0):
		"""Constructor - create a new Hexagon object and initialise its parameters"""
		super().__init__(parent) #Run the superclass constructor to create a QWidget with the required space, which we can then draw on
		self.show() #Make it visible
		self.score = startScore #Initialise score
		self.resourceURLs = resourceURLs #These will be suggested to the user as resources that could help them improve their score on this hexagon
		self.active = True
		self.forceInactive = False
		self.setContextMenuPolicy(PyQt5.QtCore.Qt.CustomContextMenu) #When you right click you get custom hexagon options, not normal right click options
		

	def onClick(self):
		"""Runs when the hexagon gets clicked on"""
		if self.active == True:
			self.deactivate()
		else:
			self.activate()
			
	def deactivate(self,force=False):
		"""Deactivates the hexagon so its score is no longer calculated and displayed"""
		self.oldScore = self.score
		self.active = False #Set it to inactive
		self.setProperty("hexColor","#979c98") #Set the colour to grey
		self.repaint() #Update the displayed hexagon on screen.
		self.forceInactive = force #The force flag can be set to prevent the hexagon from being reactivated until the force flag is sent with the reactivate call. This allows us to hold the hexagons inactive when there is no code in the active file textbox for example, so that even if the user clicks on them they don't come back
		
	def activate(self,force=False):
		"""Reactivates a Hexagon so its score is calculated and displayed"""
		if self.forceInactive: #If the hexagon was force deactivated...
			if not(force): #...and we didn't force reactivate it
				return #do nothing
			else:
				self.forceInactive = False # It was force inactive but now we unforce that before activating it again so that next time it gets deactivated it doesn't think it's forcing when it isn't
		self.active = True #Reactivate
		self.score = self.oldScore
		self.setProperty("hexColor",self.property("mainColor")) #Bring the colour back
		self.repaint() #Display the Hexagon again. This also recalculates the score.
		
	def getScore(self):
		self.repaint()
	
	def mousePressEvent(self,event):
		"""Overrides QWidget method to allow us to react to mouse button presses"""
		if event.button() == PyQt5.QtCore.Qt.LeftButton: #If the button pressed was the left mouse button
			self.onClick() #Run the onClick function
			
	def paintEvent(self, canvas): #Implemented with reference to zetcode.com/gui/pyqt5/painting
		"""Overrides QWidget paintEvent method to describe how to render the Hexagon object"""

		if self.active == False: #If the object is inactive then we should just show the score as 0
			self.score = 0 
		
		#(validation) In case the returned score was negative or greater than 10.
		if self.score < 0:
			self.score = 0
		elif self.score > 10:
			self.score = 10
		
		#Get the dimensions we have to draw on
		W = canvas.rect().width()
		H = canvas.rect().height()
		
		#Compute the amount of y(longitudinal) padding we want
		LONG_PADDING = 0.1*H
		X = (H-(2*LONG_PADDING))/4 #Now compute the Hexagon's dimension. This value is half the side length, half the apothem length and half the centre to vertex length for the hexagons drawn here (which does mean they aren't regular technically)
		LAT_PADDING = (W - 4*X)/2 #Compute the x(width) padding we need to put it in the middle of the available space

		#create and start a painter object which will draw the hexagon
		myPainter = PyQt5.QtGui.QPainter()
		myPainter.begin(self)
		
		#give the painter the write brush (fill) and pen (outline) colours
		col = PyQt5.QtGui.QColor()
		col.setNamedColor(self.property("hexColor"))
		myPainter.setBrush(PyQt5.QtGui.QBrush(col))
		myPainter.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor(0,0,0),3))
		myPainter.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor(255,255,255),3))
		
		#Drawe the hexagon based on the dimensions calculated
		myPainter.drawConvexPolygon(PyQt5.QtGui.QPolygon([
			PyQt5.QtCore.QPoint((LAT_PADDING+X),(LONG_PADDING)),
			PyQt5.QtCore.QPoint((LAT_PADDING+3*X),(LONG_PADDING)),
			PyQt5.QtCore.QPoint((LAT_PADDING+4*X),(LONG_PADDING+2*X)),
			PyQt5.QtCore.QPoint((LAT_PADDING+3*X),(LONG_PADDING+4*X)),
			PyQt5.QtCore.QPoint((LAT_PADDING+X),(LONG_PADDING+4*X)),
			PyQt5.QtCore.QPoint((LAT_PADDING),(LONG_PADDING+2*X)),
		]))
		
		#Set the correct font size for writing the score
		myFont = myPainter.font()
		myFont.setPointSize(18)
		myPainter.setFont(myFont)
		
		#Write the score on the hexagon (the -17 adjusts for the fact the coords are top-left based and we want it central)
		rounded = to_precision(self.score, 2, 'std')
		if rounded[-1] == ".":
			rounded = rounded[:-1]
		myPainter.drawText(W/2-17,H/2+LONG_PADDING/2+5,rounded)
		
		#Stop painting before we return
		myPainter.end()
	
	def onRightClick(self):
		"""Triggered when the user clicks the 'Access help to improve...' option in the right click menu."""
		PyQt5.QtGui.QDesktopServices.openUrl(PyQt5.QtCore.QUrl(random.choice(self.resourceURLs))) #Opens a random resource from the ones the hexagon has set as appropriate in the user's default browser

class EfficiencyHexagon(Hexagon):
	def __init__(self,parent):
		super().__init__(parent, resourceURLs=["https://www.bigocheatsheet.com/"]) #FUTURE RELEASE: We could have the hexagons generate these resources by themselves using additional learning algorithms
		
	def getScore(self,complexityStrings):
                """Given the complexities of all of the user's functions, computes a rough score for these based on the premise that O(1) is really good and O(2^n) is very bad. Of course not all problems can be solved in all complexities but we neglect to consider that here as that would be quite difficult to implement"""
                POSSIBLE_COMPLEXITIES = ["1","logn","n","nlogn","n^2","2^n"] #MAINTENANCE: If more complexities are added to the program, their strings should be added here, and their strings and functions in EstimateCodeComplexity. 
                totalComplexityScore = 0
                totalSubroutines = 0
                
                for result in complexityStrings: #For every complexity string e.g. "logn" from one of the user's functions,
                        if result in POSSIBLE_COMPLEXITIES: #If we recognise it as a valid complexity
                                totalComplexityScore = totalComplexityScore + (len(POSSIBLE_COMPLEXITIES)-1-POSSIBLE_COMPLEXITIES.index(result)) #The function scores 5 for O(1), 4 for O(logn) etc. down to 0 for O(2^n)
                                totalSubroutines += 1          #We count the total number of subroutines we have scored so that we can average over them
                if totalSubroutines > 0: #VALIDATION: If no subroutines to estimate the complexity of can't give a score as the following code would involve dividing by 0
                        avg = totalComplexityScore/totalSubroutines #Get average subroutine complexity score
                        self.score = 10*avg/(len(POSSIBLE_COMPLEXITIES)-1) #Was out of 5 so make out of ten
                        super().getScore() #Call the superclass method we are extending so the calculated score is displayed (the superclass method contains the code common to all Hexagons which display in the same way)

class EfficacyHexagon(Hexagon):
	def __init__(self,parent):
		super().__init__(parent,resourceURLs=["https://www.dropbox.com/s/cqsxfws52gulkyx/drawing.pdf","https://en.wikipedia.org/wiki/Software_bug","https://www.dummies.com/programming/python/the-8-most-common-python-programming-errors/"])
		
	def getScore(self,currentProject):
		""""Executes the user's unit tests against the current project and uses them to get a score out of 10 for the project's current level of efficacy."""
		currentProject.save() #Running the unit tests reads the project's data off of the disk so we need to save it in order to run the tests.
		totalTests = 0 
		totalSuccesses = 0
		
		for ut in currentProject.unitTests: #For each function the user wants us to tests
			results, outputs, times = ut.executeTests() #Run all testsa against it and get the results
			for result in results: #For each result (either True for pass or False for fail)
				totalSuccesses = (totalSuccesses + 1) if result else totalSuccesses #Either this was a success so chalk it up or ignore it
				totalTests += 1
			
		if len(currentProject.unitTests) == 0: #Avoid division by 0 error and just say that the score is 0 if there are no unit tests
			self.score = 0
		else:
			self.score = 10*totalSuccesses/totalTests #The score is like a percentage but out of 10 of correct scores.
		super().getScore() #Call the superclass method we are extending so the calculated score is displayed (the superclass method contains the code common to all Hexagons which display in the same way)
		
class ReadabilityHexagon(Hexagon):
	def __init__(self,parent):
		super().__init__(parent,resourceURLs=["https://code.tutsplus.com/tutorials/top-15-best-practices-for-writing-super-readable-code--net-8118","https://dzone.com/articles/10-tips-how-to-improve-the-readability-of-your-sof","https://stackoverflow.com/questions/550861/improving-code-readability"])
		
	def getScore(self):
		super().getScore()
		
class EleganceHexagon(Hexagon):
	def __init__(self,parent):
		super().__init__(parent,["https://levelup.gitconnected.com/write-elegant-python-code-with-these-10-tricks-43ae7b1aa481","EleganceTips.html","https://dev.solita.fi/2016/06/02/what-is-elegant-code.html"])
		
	def getScore(self):
		super().getScore()


