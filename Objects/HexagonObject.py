import PyQt5
from to_precision import to_precision

class Hexagon(PyQt5.QtWidgets.QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.show()
		self.score = 9.8
		self.active = True
		self.forceInactive = False
		
	def onClick(self):
		"""Runs when the hexagon gets clicked on"""
		if self.active == True:
			self.deactivate()
		else:
			self.activate()
			
	def deactivate(self,force=False):
		"""Deactivates the hexagon so its score is no longer calculated and displayed"""
		self.active = False #Set it to inactive
		self.mainColour = self.property("hexColor") #Save the colour so that when we set the colour to grey we can get it back again later.
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
		self.setProperty("hexColor",self.mainColour) #Bring the colour back
		self.repaint() #Display the Hexagon again. This also recalculates the score.
		
	def getScore(self):
		return 9.8
	
	def mousePressEvent(self,event):
		"""Overrides QWidget method to allow us to react to mouse button presses"""
		if event.button() == PyQt5.QtCore.Qt.LeftButton: #If the button pressed was the left mouse button
			self.onClick() #Run the onClick function
			
	def paintEvent(self, canvas): #Implemented with reference to zetcode.com/gui/pyqt5/painting
		"""Overrides QWidget paintEvent method to describe how to render the Hexagon object"""
		
		if self.active == False: #If the object is inactive then we should just show the score as 0
			self.score = 0 
		else:
			self.score = self.getScore() #When it is active we need to get the score
		
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
		myPainter.drawText(W/2-17,H/2+LONG_PADDING/2+5,to_precision(self.score, 2, 'std'))
		
		#Stop painting before we return
		myPainter.end()

		
		
