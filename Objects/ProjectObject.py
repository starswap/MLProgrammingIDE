#import the necessary packages
import json
#import UnitTestObject.UnitTest as UnitTest
from datetime import datetime
from pathlib import Path
import PyQt5
import os
class Project():
	"""A project in the ml programming ide."""
	
	def __init__(self,projectNameOrFilePath,exists,mainWindow):
		"""Constructor for the project class. Will create a project object then populate its attributes by either opening an existing project or creating a new one"""
		self.associatedWindow = mainWindow #Because the pseudocode algorithms I designed for the project involve changes to the UI from the ProjectObject (to avoid excessive passsing around), we need to store a handle to the UI window in the project object.
		self.fileContents = [] #Will contain the contents of all of the files in the project
		if exists: #If the project already exists we came via an open dialogue and so we need to use the Project.open() method to populate attributes 
			self.open(projectNameOrFilePath) 
		else: #If the project does not exist, we came via a new dialogue and so we need to use newProject to populate
			self.newProject(projectNameOrFilePath)
	
	def open(self,projectFilePath):
		"""Populates the attributes of the Project object by opening an existing project"""
		_, extension = os.path.splitext(projectFilePath) #Splits the file path into the base path and the extension so we can check the extension is correct
		
		if extension != ".mlideproj": #Wrong file extension
			#Make a dialogue box to tell the user that they need to select the correct file type
			dialogue = PyQt5.QtWidgets.QMessageBox(self.associatedWindow)
			dialogue.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
			dialogue.setText("Please select a .mlideproj file")
			dialogue.show()
			return False 
		else:
			self.fileName = os.path.basename(projectFilePath) #Save the name of the project file 

			#read in the contents of the project file to unpack the attributes of the project
			f = open(projectFilePath,"r") 
			projectFileContents = json.loads(f.read())
			f.close()
			
			#Get the name, directory path and run command as stored on disk
			self.name = projectFileContents["name"]
			self.directoryPath = projectFileContents["directoryPath"]
			self.runCommand = projectFileContents["runCommand"]
			self.projectFiles = projectFileContents["projectFiles"]
			
			self.associatedWindow.setWindowTitle("ML Programming IDE - " + self.name)
			self.associatedWindow.runCommandBox.setText(self.runCommand)
			
			#Open all files in the project
			for filename in self.projectFiles:
				self.openFile(filename)
			
			#Get all of the data about unit tests in the project, iterate over each one of these and create a unit test object with the provided data. Add this to the project
			self.UnitTests = []
			try:
				for test in projectFileContents["UnitTests"]:
					self.UnitTests.append(UnitTesttest.functionName,test.inputValues,test.outputValues,test.types,test.inputConstraints,test.functionFileName)
			except KeyError:
				pass		
			print("name:" + self.name)
			print("directoryPath" + self.directoryPath)
			print("run command" + self.runCommand)
			print("projectFiles" + str(self.projectFiles))
			return True #Project opening was successful
			
	def newProject(self,projectName):
		"""Populates the attributes of the project by creating a new one"""
		if projectName == "": #If no name is provided this cannot work because we need to name the file after the project.
			projectName = "Untitled" + str(datetime.utcnow()) #So use Untitled + the time of creation in utc.
		self.name = projectName
		self.fileName = projectName + ".mlideproj"

		#Create the project folder as a subdirectory of the user's home directory, named after the project, unless the directory already exists, in which case. 
		if not(os.path.exists(os.path.join(str(Path.home()),projectName))):
			self.directoryPath = os.path.join(str(Path.home()),projectName) #Have to use os.path.join to work across platforms.
		else:
			self.directoryPath = os.path.join(str(Path.home()),projectName+str(datetime.utcnow()))
		os.mkdir(self.directoryPath)
		
		#Create project file in project directory with the data that we already have about the project
		f = open(os.path.join(self.directoryPath,self.fileName),"w") #Use of write mode means file is created if not exists
		contents = {}
		contents["name"] = projectName
		contents["directoryPath"] = self.directoryPath
		f.write(json.dumps(contents))
		f.close()
				
		#Set the window title
		self.associatedWindow.setWindowTitle("ML Programming IDE - " + self.name)
		self.associatedWindow.actionEnter_Unit_Tests.trigger() #Projects start with getting unit tests
		
	def openFile(self,filename):
		"""Open an existing file in the project into the IDE"""
		#Add the file name to the list of files menu
		item = PyQt5.QtWidgets.QListWidgetItem()
		item.setText(filename)
		item.id = self.associatedWindow.listOfFilesMenu.count()
		self.associatedWindow.listOfFilesMenu.addItem(item)

		#Get the contents of the file and put them in the ActiveFileTextbox, as well as saving them in the Project object 
		f = open(os.path.join(self.directoryPath,filename),"r")
		t = f.read()
		f.close()
		self.fileContents.append(t)
		self.activeFileIndex = len(self.fileContents) - 1 #Defines which of the open files is currently in use. 
		self.associatedWindow.activeFileTextbox.setPlainText(t)
		
	def save(self):
		"""Saves the current project to disk, by saving all files that it includes, and updating the project file"""
		f = open(os.path.join(self.directoryPath,self.fileName),"w") #Open the project file
		
		#Prepare data to write to project file
		contents = {}
		contents["name"] = self.name
		contents["directoryPath"] = self.directoryPath
		contents["projectFiles"] = self.projectFiles
		contents["runCommand"] = self.runCommand
		contents["unitTests"] = [test.saveTest() for test in self.UnitTests]
		
		#Write the data out and close the file
		f.write(json.dumps(contents))
		f.close()
		
		#For every file in the project
		for i in range(len(self.projectFiles)):
			#Open the file, write the data we have in memory out to the file, and close the file again
			f = open(os.path.join(self.directoryPath,self.projectFiles[i]),"w")
			f.write(self.fileContents[i])
			f.close()
		
		#Update the title of the window so that the user knows when the project was last saved.
		self.associatedWindow.setWindowTitle("ML Programming IDE - " + self.name + " - last saved at" + str(datetime.now()))

	def switchToFile(self,itemClicked):
		print(itemClicked.id)


