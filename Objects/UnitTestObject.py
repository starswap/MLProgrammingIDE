class UnitTest():
	def __init__(self,FuncName,InputList,OutputList,Types,InpConstraints,numberOfInputs=length(InputList) by default,funcFileName):
		self.functionFileName = funcFileName
		self.numberOfInputs = numberOfInputs
		self.functionToTest = funcName
		self.inputValues = InputList
		self.outputValues = OutputList
		self.inputConstraints = InpConstraints
		paramString = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		
		UnitTestWindow.add(funcName+"(" + paramString[:2*numberOfInputs-1] + "):")
		newFuncTable = window.table(rows=2,columns=numberOfInputs+1))
		for i = 0 to numberOfInputs - 2 :
			newFuncTable[0][i] = alphabet[i]
		newFuncTable[0][i] = "Out"
		for i = 0 to numberOfInputs - 1:
    			newFuncTable[1][i] = window.textbox(id=funcName+str(i))
    			
		UnitTestWindow.add(newFuncTable)
		UnitTestWindow.add(window.button(onclick=this.addTest())



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

    UnitTest.functionFileName [string]
