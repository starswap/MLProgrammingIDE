import json
import jinja2
import subprocess
import os
class UnitTest():
	"""An object representing a set of Unit Tests that can be run against one individual function in the user's code. (i.e. one UnitTest object to one function), including a set of input values, types, and constraints, and a set of output values, as well as the methods required to run these against the function when the user has written it."""
	def __init__(self,funcName,inputList,outputList,types,inpConstraints,funcFileName,window):
		"""Constructor for the UnitTest class - take the data surrounding the unit test and store it inside the class' scope. This data comes from the UnitTestPopup part of the UI, typed in by the user."""
		
		#Put the provided data into the permanent storage of the class (as opposed to local variables in the constructor)
		self.numberOfInputs = len(inputList[0]) #The input list is a list of lists where each inner list is a set of inputs to the function. This was going to be a list of tuples, but it is easier to use lists as Python support heterogeneity within these types. It would be inefficient to create a list and then convert to tuple and we might want to modify tests later.
		self.functionFileName = funcFileName
		self.functionName = funcName
		self.inputValues = inputList
		self.outputValues = outputList
		self.types = types
		self.inputConstraints = inpConstraints
		self.associatedWindow = window	

	def saveTest(self):
		"""Returns a string of JSON data which represents the full state of the UnitTest object, which can then be written out into a file to save the project"""
		stateObj = {} #Will store all data about the object
		stateObj["functionName"] = self.functionName
		stateObj["inputValues"] = self.inputValues
		stateObj["outputValues"] = self.outputValues
		stateObj["types"] = self.types
		stateObj["inputConstraints"] = self.inputConstraints
		stateObj["functionFileName"] = self.functionFileName

		return stateObj # Will later be converted to a json string

	
	def executeTests(self):
		"""Executes all defined tests in the UnitTest object against the code of the function that the user has written to see if the correct outputs are produced"""
		
		#https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
		#https://realpython.com/primer-on-jinja-templating/
		TEMPLATE = """import importlib.util
spec = importlib.util.spec_from_file_location("moduleToTest", "{{filePath}}")
codeToTest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(codeToTest)
print(codeToTest.{{functionToTest}}({% for arg in arguments %}{{arg}},{% endfor %}),end="")
""" #This is the code that will be run to test the user's code. We first import the file containing the user's code and then we run the function with the required arguments. The TEMPLATE variable is in jinja template format as the actual function name, file name and arguments will be filled in at runtime. 

		results = [] #list of bools - True if the test was successful and the output matched the expected output, False otherwise
		outputs = [] #list of string - the returned values from the function the user has written that we are testing
		
		for i,oneTest in enumerate(self.inputValues): #For every test to run
			filledInTemplate = jinja2.Template(TEMPLATE).render(filePath=self.functionFileName,functionToTest=self.functionName,arguments=oneTest) #Fill in the template code so that the function executed is the user's one
		
			#Write the filled in template out to a file which we can then run to execute it
			g = open("unitTestTemp.py","w")
			g.write(filledInTemplate)
			g.close()
			
			#Run the file and get the output
			try:
				returnedVal = subprocess.check_output([self.associatedWindow.settings.settings["pythonCommand"],"unitTestTemp.py"]).decode("UTF-8") #https://stackoverflow.com/questions/18739239/python-how-to-get-stdout-after-running-os-system
				
				#Check if the actual output matches the expected output for this test.
				if returnedVal == self.outputValues[i]:
					results.append(True)
				else:
					results.append(False)
					
				#Save the output to return later
				outputs.append(returnedVal)
			except subprocess.CalledProcessError: #There was an error in the user's code or the function was not yet defined
				outputs.append("ERROR")
				results.append(False)				
			
			#delete the temp file
			os.remove("unitTestTemp.py")
			
		return results, outputs
"""
Methods:

    UnitTest.GenerateMockInput()


Attributes:

    UnitTest.functionToTest [string]

    UnitTest.inputValues [array of tuples]

    UnitTest.outputValues [array of output values]

    UnitTest.types [tuple of values representing the input and output data types for the function to be unit tested]

    UnitTest.InputConstraints [tuple of tuples where each inner tuple is a constraint on one input of the function.] 

    UnitTest.numberOfInputs [integer]

    UnitTest.functionFileName [string]"""
    
