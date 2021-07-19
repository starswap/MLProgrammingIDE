#import the necessary packages
import json
#import UnitTestObject.UnitTest as UnitTest
from datetime import datetime
from pathlib import Path
import PyQt5
import os
import shutil

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
		self.messages = []
	
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
		self.projectFiles = []
		self.runCommand = ""
		self.associatedWindow.runCommandBox.setText(self.runCommand)
		self.unitTests = []
					
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
		contents["projectFiles"] = self.projectFiles
		f.write(json.dumps(contents))
		f.close()
				
		#Set the window title
		self.associatedWindow.setWindowTitle("ML Programming IDE - " + self.name)
		self.associatedWindow.actionEnter_Unit_Tests.trigger() #Projects start with getting unit tests
		
		self.save()
		
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
		contents["unitTests"] = [test.saveTest() for test in self.unitTests]
		
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
		self.associatedWindow.setWindowTitle("ML Programming IDE - " + self.name + " - last saved at" + str(datetime.now().strftime("%H:%M:%S"))) #https://www.programiz.com/python-programming/datetime/current-time

	def switchToFile(self,itemClicked):
		"""Switches the currently active file"""
		self.activeFileIndex = itemClicked.id #Set the active file index to be the index of the file we clicked on in the list of files menu
		self.associatedWindow.activeFileTextbox.setPlainText(self.fileContents[itemClicked.id]) #Set the contents of the active file textbox to be the contents of the file that we switched to

	def newFile(self,filename):
		"""Creates a new file and adds it to the current project"""
		#If we don't have a filename then use untitled and the timestamp of creation
		if filename == "":
			filename = "Untitled" + str(datetime.utcnow())
		self.projectFiles.append(filename) #Add the name to the list of files in the project

		#Create the file by opening for writing and closing again
		f = open(os.path.join(self.directoryPath,filename),"w")
		f.close()
		
		#Open the file into the IDE so the user can start editng it
		self.openFile(filename)
		self.save()
	
	def saveToProject(self):
		"""Runs every time the content of the active file textbox changes. Saves the content to the fileContents attribute of the Project object"""
		self.fileContents[self.activeFileIndex] = self.associatedWindow.activeFileTextbox.toPlainText()
		self.runCommand = self.associatedWindow.runCommandBox.text()
	

	def addFile(self,filepath):#https://stackoverflow.com/questions/123198/how-can-a-file-be-copied, https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
		"""Takes a file from somewhere on the user's computer and adds it to the current project"""
		newName = Path(filepath).name #Separate the path from the filename. This allows us to keep the same filename when copying it into the project's directory
		if newName in os.listdir(self.directoryPath): #If a file with this name already exists in the project directory
			newName += str(datetime.utcnow()) #Make unique by adding timestamp

		shutil.copy(filepath,os.path.join(self.directoryPath,newName)) #Copy the file into the project directory
		self.projectFiles.append(newName) #Add the new file to the project files
		self.openFile(newName) #Open the file into the IDE

	#Execution interface
	def execute(self):
		"""Run the project's runCommand as a subprocess inside the IDE, attached to the current project object (this allows it to be accessed later)"""
		
		#Reset the text of the output and input windows
		self.associatedWindow.outputWindow.setPlainText("") 
		self.associatedWindow.shellInputBox.setPlainText("")
		
		#Create the subprocess and run the command
		self.activeProcess = PyQt5.QtCore.QProcess()
		self.activeProcess.start(self.runCommand.split(" ")[0],self.runCommand.split(" ")[1:])
		
		#Set up Qt Signals (essentially events)
		self.activeProcess.finished.connect(self.cleanupExecution) # When the process finishes, the cleanupExecution method will be run
		self.activeProcess.readyRead.connect(self.readDataFromSubprocess) # When the process has put some data to stdout, the readDataFromSubprocess method will be run to get that data and put it in the output window	
		self.activeProcess.readyReadStandardError.connect(self.readErrorFromSubprocess) # When the process has put some data to stderr, the readErrorFromSubprocess method will be run to get that data and put it in the output window. 

	def sendExecuteMessage(self):
		"""Send the input the user has placed in the input box to the running subprocess. This method is triggered when the Send Input button is clicked"""
		
		if hasattr(self,"activeProcess"): #Only try to send data if the process is already running otherwise we might get a broken pipe error
			messageText = self.associatedWindow.shellInputBox.toPlainText() #this is the input to send to the program
			messageContentsToScreen = self.associatedWindow.shellInputBox.toPlainText() #this is the input that will be shown in the output box so the user knows where the program was when the input was made. We use two separate variables as....
			if self.associatedWindow.appendNewline.isChecked(): #...if we need to append a new line to the end of the input the user has typed ...
				#...the messageText gets the actual platform specific line ending while the messageContentsToScreen gets the text \n so the user knows we mean a newline.
				messageText += os.linesep
				messageContentsToScreen += "\\n"
			
			self.activeProcess.writeData(PyQt5.QtCore.QByteArray(messageText.encode("utf-8"))) #Encode the input as UTF8 bytes before sending it on stdin to the process
			self.associatedWindow.outputWindow.setPlainText(self.associatedWindow.outputWindow.toPlainText() + "\n[INPUT: " + messageContentsToScreen +"]\n") #Update the output window to show that input was sent to the process
			self.associatedWindow.shellInputBox.setPlainText("") #Clear the input window ready for the next bit of input
			
	def cleanupExecution(self):
		"""Runs when the subprocess of the user's run command has finished executing to delete the subprocess and write end of execution to the output window"""
		self.activeProcess.close()
		delattr(self,"activeProcess")
		self.associatedWindow.outputWindow.setPlainText(self.associatedWindow.outputWindow.toPlainText() + "\n----END OF EXECUTION----")
		
	def readDataFromSubprocess(self):
		"""Reads data from the subprocess' STDIN to put into the output box, whenever the subprocess has pushed data onto STDOUT"""
		self.activeProcess.setReadChannel(PyQt5.QtCore.QProcess.StandardOutput) #Tell qt that when we use bytesAvailable() or readLine() we want to refer to STDIN and not STDERR
		while self.activeProcess.bytesAvailable() != 0: #While we haven't read all of the data from the process' stdout
			self.associatedWindow.outputWindow.setPlainText(self.associatedWindow.outputWindow.toPlainText() + str(self.activeProcess.readLine(),"utf-8"))  #Read an additional line from stdout as bytes, decode it as UTF-8 and then append this to the output window
	
	def readErrorFromSubprocess(self):
		"""Reads data from the subprocess' STDERR to put into the output box, whenever the subprocess has pushed data onto STDERR"""	
		self.activeProcess.setReadChannel(PyQt5.QtCore.QProcess.StandardError) #Tell qt that when we use bytesAvailable() or readLine() we want to refer to STDERR and not STDOUT
		while self.activeProcess.bytesAvailable() != 0: #While we haven't read all of the data from the process' stderr
			self.associatedWindow.outputWindow.setPlainText(self.associatedWindow.outputWindow.toPlainText() + str(self.activeProcess.readLine(),"utf-8")) #Read an additional line from stderr as bytes, decode it as UTF-8 and then append this to the output window
		

