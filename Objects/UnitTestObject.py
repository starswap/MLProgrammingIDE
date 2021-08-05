import json
import jinja2
import subprocess
import os
import time
import random
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
		times = [] #list of floats - execution times
		for i,oneTest in enumerate(self.inputValues): #For every test to run
			filledInTemplate = jinja2.Template(TEMPLATE).render(filePath=self.functionFileName,functionToTest=self.functionName,arguments=oneTest) #Fill in the template code so that the function executed is the user's one
		
			#Write the filled in template out to a file which we can then run to execute it
			g = open("unitTestTemp.py","w")
			g.write(filledInTemplate)
			g.close()
			
			#Run the file and get the output
			try:
				tick = time.time() #start time
				returnedVal = subprocess.check_output([self.associatedWindow.settings.settings["pythonCommand"],"unitTestTemp.py"]).decode("UTF-8") #https://stackoverflow.com/questions/18739239/python-how-to-get-stdout-after-running-os-system
				tock = time.time() #end time
				times.append("{time:.4f}".format(time=(tock-tick))) #delta T
				
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
				times.append("0")			
			
			#delete the temp file
			os.remove("unitTestTemp.py")
			
		return results, outputs, times
	
	def generateMockInput(self,sizeConstraint):
		""" Uses the type and constraint information stored about user functions by the unit test object in order to generate realistic input to the function, of a given length, which can be used to examine the complexity of the function. The sizeConstraint argument gives an idea of how big the input should be and represents the n value in big o notation. The way it is used depends on the type of input required."""
		#FUTURE RELEASE: Currently we only support complexity analysis on the first input of a function. 
		print(self.inputConstraints)
		if self.types[0] == "Int" or self.types[0] == "Float": 
			mini = -10000 #Initialise valid minimum and maximum values
			maxi = 10000
			for constraint in self.inputConstraints[0]: #FUTURE RELEASE: Add more constraint types e.g. amount of dp for float
				if constraint[0] == "Range": #The user has provided a range of acceptable values.
					mini = constraint[1]
					maxi = constraint[2]
			if (sizeConstraint >= mini) and (sizeConstraint <= maxi): #We can just use the size constraint as it is a number in the valid range
				return sizeConstraint
			else:
				raise ValueError("Size constraint not within bounds for int/float size") #the sizeConstraint is outside the valid range so cannot be used

		elif self.types[0] == "String":
			alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" #Initialise the alphabet
			for constraint in self.inputConstraints[0]: #Go through all constraints
				if constraint[0] == "Length": #User has provided a length range
					if not(sizeConstraint >= constraint[1] and sizeConstraint <= constraint[2]): #The length that we were given is invalid
						raise ValueError("Size constraint not within valid bounds for string length")
				elif constraint[0] == "Alphabet": #User has provided a set of valid characters
					alphabet = constraint[1]
				else: #FUTURE RELEASE - add more input constraint types
					raise TypeError("Input constraint format unrecognised")
			res = ""
			for i in range(sizeConstraint): #Make a string containing letters of alphabet with length sizeConstraint 
				res += random.choice(alphabet)
			return res

		elif self.types[0][:4] == "List": #List of sometype
			for constraint in self.inputConstraints[0]:
				if constraint[0] == "Length": #Min/Max length constraint provided
					if sizeConstraint < constraint[1] or sizeConstraint > constraint[2]:
						raise ValueError("Size constraint not within valid bounds for list length")
			res = []
			elementType = self.types[0][4:] #Type of the elements of the list
			for i in range(sizeConstraint): #Make a list length sizeConstraint of elements of the right type. FUTURE RELEASE -> Allow the user to specify constraints on the values in the array e.g. by recursively applying the constraint rules. This would widen the scope of the mock input's validity as right now it just uses values from some arbitrary range.
				if elementType == "Int":
					res.append(random.randint(-1000000,1000000))
				elif elementType == "Float":
					res.append(random.random()*1000000 - 500000)	
				elif elementType == "Bool":
					res.append(bool(random.randint(0,1)))
				elif elementType == "Char":
					res.append(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
				else:
					raise TypeError("Only List of Int, Float, Bool or Char supported")
			return res
		elif self.types[0] == "":
			return None
		else:
			raise TypeError("Complexity Analysis only for Int, Float, String, List of Int/Float/Bool/Char arguments") #FUTURE RELEASE: Support more types on complexity analysis

