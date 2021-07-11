#import the necessary packages
import json
import UnitTestObject.UnitTest as UnitTest
from datetime import datetime
from pathlib import Path
import PyQt5

class Project():
	"""A project in the ml programming ide."""
	
	def __init__(self,projectNameOrFilePath,exists,mainWindow):
		"""Constructor for the project class. Will create a project object then populate its attributes by either opening an existing project or creating a new one"""
		self.associatedWindow = mainWindow #Because the pseudocode algorithms I designed for the project involve changes to the UI from the ProjectObject (to avoid excessive passsing around), we need to store a handle to the UI window in the project object.
		self.fileContents = [] #Will contain the contents of all of the files in the project
		if exists: #If the project already exists we came via an open dialogue and so we need to use the Project.open() method to populate attributes 
			if self.open(projectNameOrFilePath) == "False": #Try to open the existing project unless the project is not a project file, in which case False is returned. 
				#Show a dialogue to tell the user that they chose the wrong type of file.
				rejectionDialogue = PyQt5.QtWidgets.QDialog("You must select a project file with extension mlideproj") 
				rejectionDialogue.show() 		
		else: #If the project does not exist, we came via a new dialogue and so we need to use newProject to populate
			self.newProject(projectNameOrFilePath)
	
	def open(self,projectFilePath):
		"""Populates the attributes of the Project object by opening an existing project"""
		_, extension = os.path.splitext(projectFilePath) #Splits the file path into the base path and the extension so we can check the extension is correct
		if extension != "mlideproj":
			return False #Not a project file
		else:
			self.fileName = os.path.basename(projectFilePath) #Save the name of the project file 

			#read in the contents of the project file to unpack the attributes of the project
			f = open(projectFilePath,"r") 
			projectfileContents = json.loads(f.read())
			f.close()
			
			#Get the name, directory path and run command as stored on disk
			self.name = projectFileContents["name"]
			self.directoryPath = projectFileContents["directoryPath"]
			self.runCommand = projectFilecontents["runCommand"]
			
			self.associatedWindow.setWindowTitle("ML Programming IDE - " + this.name)
			
			#Open all files in the project
			for filename in self.projectFiles
				self.OpenFile(filename)
			
			#Get all of the data about unit tests in the project, iterate over each one of these and create a unit test object with the provided data. Add this to the project
			self.UnitTests = []
			for test in projectFileContents["UnitTests"]:
				self.UnitTests.append(UnitTesttest.functionName,test.inputValues,test.outputValues,test.types,test.inputConstraints,test.functionFileName))
				
			return True #Project opening was successful
			
	def newProject(self,projectName):
		"""Populates the attributes of the project by creating a new one"""
		if projectName == "": #If no name is provided this cannot work because we need to name the file after the project.
			projectName = "Untitled" + str(datetime.utcnow()) #So use Untitled + the time of creation in utc.
		self.name = projectName
		self.fileName = projectName + ".mlideproj"

		#Create the project folder as a subdirectory of the user's home directory, named after the project, unless the directory already exists, in which case. 
		if not(os.path.exists(os.path.join(str(Path.home(),projectName))):
			self.directoryPath = os.path.join(str(Path.home(),projectName)) #Have to use os.path.join to work across platforms.
		else:
			self.directoryPath = os.path.join(str(Path.home(),projectName+str(datetime.utcnow())))
		os.mkdir(self.directoryPath)
		
		#Create project file in project directory
		f = open(os.path.join(self.directoryPath,self.fileName),"r")
		f.close() #Create a file by opening and closing
		
		#Set the window title
		self.associatedWindow.setWindowTitle("ML Programming IDE - " + this.name)
		self.associatedWindow.actionEnter_Unit_Tests.trigger() #Projects start with getting unit tests
		
	def openFile(filename):
		"""Open an existing file in the project into the IDE"""
		#Add the file name to the list of files menu
		item = PyQt5.QtGui.QListWidgetItem()
		item.setText(filename)
		self.associatedWindow.listOfFilesMenu.addItem(item)
		
		#Get the contents of the file and put them in the ActiveFileTextbox, as well as saving them in the Project object 
		f = open(filename,"r")
		t = f.read()
		f.close()
		self.fileContents.append(t)
		self.activeFileIndex = len(self.fileContents) - 1 #Defines which of the open files is currently in use. 
		self.associatedWindow.activeFileTextbox.setPlainText(t)


