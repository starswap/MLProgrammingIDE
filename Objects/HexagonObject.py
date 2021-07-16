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
		if self.active == True:
			self.deactivate()
		else:
			self.activate()
			
	def deactivate(self,force=False):
		self.active = False
		self.mainColour = self.property("hexColor")
		self.setProperty("hexColor","#979c98")
		self.repaint()
		self.forceInactive = force
		
	def activate(self,force=False):
		if self.forceInactive:
			if not(force):
				return
		self.active = True
		self.setProperty("hexColor",self.mainColour)
		self.repaint()
		
	def getScore(self):
		return 9.8
	
	def mousePressEvent(self,event):
		if event.button() == PyQt5.QtCore.Qt.LeftButton:
			self.onClick()
			
	def paintEvent(self, canvas): #Implemented with reference to zetcode.com/gui/pyqt5/painting
		
		if self.active == False:
			self.score = 0 
		else:
			self.score = self.getScore()
			
		if self.score < 0:
			self.score = 0
		elif self.score > 10:
			self.score = 10
		
		W = canvas.rect().width()
		H = canvas.rect().height()
		LONG_PADDING = 0.1*H
		X = (H-(2*LONG_PADDING))/4		
		print(X)
		LAT_PADDING = (W - 4*X)/2

		myPainter = PyQt5.QtGui.QPainter()
		myPainter.begin(self)
		col = PyQt5.QtGui.QColor()
		col.setNamedColor(self.property("hexColor"))
		myPainter.setBrush(PyQt5.QtGui.QBrush(col))
		myPainter.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor(0,0,0),3))
		myPainter.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor(255,255,255),3))
		myPainter.drawConvexPolygon(PyQt5.QtGui.QPolygon([
			PyQt5.QtCore.QPoint((LAT_PADDING+X),(LONG_PADDING)),
			PyQt5.QtCore.QPoint((LAT_PADDING+3*X),(LONG_PADDING)),
			PyQt5.QtCore.QPoint((LAT_PADDING+4*X),(LONG_PADDING+2*X)),
			PyQt5.QtCore.QPoint((LAT_PADDING+3*X),(LONG_PADDING+4*X)),
			PyQt5.QtCore.QPoint((LAT_PADDING+X),(LONG_PADDING+4*X)),
			PyQt5.QtCore.QPoint((LAT_PADDING),(LONG_PADDING+2*X)),
		]))
		
		myFont = myPainter.font()
		myFont.setPointSize(18)
		myPainter.setFont(myFont)
		myPainter.drawText(W/2-17,H/2+LONG_PADDING/2+5,to_precision(self.score, 2, 'std'))
		
		myPainter.end()

		
		
