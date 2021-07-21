import json
class UnitTest():
	"""An object representing a set of Unit Tests that can be run against one individual function in the user's code. (i.e. one UnitTest object to one function), including a set of input values, types, and constraints, and a set of output values, as well as the methods required to run these against the function when the user has written it."""
	def __init__(self,funcName,inputList,outputList,types,inpConstraints,funcFileName):
		"""Constructor for the UnitTest class - take the data surrounding the unit test and store it inside the class' scope. This data comes from the UnitTestPopup part of the UI, typed in by the user."""
		
		#Put the provided data into the permanent storage of the class (as opposed to local variables in the constructor)
		self.numberOfInputs = len(inputList[0]) #The input list is a list of lists where each inner list is a set of inputs to the function. This was going to be a list of tuples, but it is easier to use lists as Python support heterogeneity within these types. It would be inefficient to create a list and then convert to tuple and we might want to modify tests later.
		self.functionFileName = funcFileName
		self.functionName = funcName
		self.inputValues = inputList
		self.outputValues = outputList
		self.types = types
		self.inputConstraints = inpConstraints
	
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

"""

Methods:

    UnitTest.executeTests()

    UnitTest.addTest()

    (constructor)

    UnitTest.saveTest()

    UnitTest.GenerateMockInput()


Attributes:

    UnitTest.functionToTest [string]

    UnitTest.inputValues [array of tuples]

    UnitTest.outputValues [array of output values]

    UnitTest.types [tuple of values representing the input and output data types for the function to be unit tested]

    UnitTest.InputConstraints [tuple of tuples where each inner tuple is a constraint on one input of the function.] 

    UnitTest.numberOfInputs [integer]

    UnitTest.functionFileName [string]"""
