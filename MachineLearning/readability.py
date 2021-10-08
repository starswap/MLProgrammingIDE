import numpy as np
import re
def forwardProp(X): 
    """Performs 1 forward propagation through the network to get a readability rating for given X (input features - each column is one training example so vectorised), Ws (list of weights), bs (list of biases)"""
    As = [X] #Activations at each layer, with layer 0 having the input features as its activations
    Zs = [] #Z values (input to the activation function === matrix product of Ws[current layer] and a[layer before] + bs[current layer])
    
    for i in range(len(Ws)-1): #For every layer in the network except the last one, which is dealt with separately as it has a different activation,
        Zs.append(np.matmul(Ws[i],As[i]) + bs[i]) #Compute the next Z value by multiplying the corresponding weights with the previous layer's activations and adding the biases
        As.append(sigmoid(Zs[-1])) #Compute this layer's activation by applying the tanh activation function

    #Forward prop the final layer
    Z_final = np.matmul(Ws[-1],As[-1]) + bs[-1] #Compute Z as usual 
    Zs.append(Z_final) #Save the final Z value
    As.append(Z_final) #No final activation function as we just want to do regression.
    return Zs,As #Return the Z and Activation values, which will be needed for backprop 

def sigmoid(matrix):
    """Sigmoid activation function"""
    return 1/(1+np.exp(-matrix))

def getCodeReadabilityScore(featureMatrix):
    """Runs forward propagation on the network with the provided weights and input features and returns the final layer activations, the scores for each code sample"""
    Zs, As = forwardProp(featureMatrix)
    return As[-1][0,0]*sigmaY+muY #===y_hat

def extractCodeReadabilityFeatures(codeSnippet):
	"""Takes a code snippet and converts it to a matrix of statistical features describing it, which will be used to score it on readability."""
	
	#These are used to determine whether a word seen in the code snippet is an identifier or a language keyword
	LANGUAGE_KEYWORDS = ["for","if","def","lambda","while","await","else","elif","import","pass","break","except","in","raise","class","finally","is","return","and","continue","try","as","from","assert","del","global","not","with","async","or","yield","self","False","True","AttributeError","None"] #Source https://www.programiz.com/python-programming/keyword-list 
	
	#MAINTENANCE: To change the designated tab style (tabs/spaces) for this part of the solution, swap the commented line
	TAB_CHAR = "    "
 #   TAB_CHAR = "\t" 
	
	#Initialise accumulator variables counting each feature which will later be averaged.
	numberOfLines = 0    
	totalLineLength = 0
	totalEmptyLines = 0
	maxIndentDepth = 0
	totalDigits = 0
	totalSpaces = 0
	prevIndent = 0
	blockLength = 0
	totalBlockLength = 0 
	totalBlocks = 0 
	totalIdentifiers = 0
	totalIdentifierLength = 0
	totalCamelPascal = 0
	totalUnder = 0
	totalUpperCase = 0 
	idCounts = {} #This dictionary counts occurrences of each identifier in the code snippet so we can later calculate things like the number of occurrences of the most frequent identifier

	for line in codeSnippet.split("\n"): #Go over every line in the snippet
		numberOfLines += 1 #Count lines
		totalLineLength += len(line) #This variable will later be divided by numberOfLines to get averageLineLength
		if line == "": #Count empty lines
			totalEmptyLines += 1
			continue #Skip further processing on empty lines

		if line.count(TAB_CHAR) > maxIndentDepth: #One of the features is the maximum indentation depth in tabs (or multiples of 4 spaces)
			maxIndentDepth = line.count(TAB_CHAR)
		
		totalDigits += sum([line.count(a) for a in "1234567890"]) #Count all digits in the line
		totalSpaces += line.count(" ") #Count all spaces in the line

		if line.count(TAB_CHAR) != prevIndent: #prevIndent stores the indent level of the previous line, so that we know if indentation has changed (if yes we are on a new block of code)
			totalBlockLength += blockLength #We will later divide this by total blocks to get average block length
			blockLength = 0
			totalBlocks += 1
		prevIndent = line.count(TAB_CHAR) #this line's indent is saved for next time
		blockLength += 1 

		#We take the part of the current line up to any comment (# or """) and split it on punctuation, yielding only "words". These are either identifiers or keywords
		for item in re.split("\W+",line.split("#")[0].split("\"\"\"")[0]): #https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
			if item == "": #There were two symbols in a row, yielding a blank match which we ignore
				continue
			if not(item in LANGUAGE_KEYWORDS): #Not a language keyword therefore...
				#item is an identifier name
				totalIdentifiers += 1 #Count identifiers
				totalIdentifierLength += len(item) #Will be used to get average identifier length
				
				#Count different variable naming conventions
				if "_" in item: #underscore_based
					totalUnder += 1
				if re.search("[A-Z]",item) and re.search("[a-z]",item): #camelCase/PascalCase
					totalCamelPascal += 1
				elif re.search("[A-Z]",item): #UPPER CASE
					totalUpperCase += 1
				
				#Increment the number of times we have seen this identifier in the code so we can later find the maximum occurrences of a single identifier
				if item in idCounts:
					idCounts[item] = idCounts[item] + 1 
				else:
					idCounts[item] = 1
	
	totalSharpComments = codeSnippet.count("#")

	#Avoid divide by 0 errors
	if totalIdentifiers == 0:
		totalIdentifiers = 1
	if totalBlocks == 0:
		totalBlocks = 1

	#Compute averages
	averageLineLength = totalLineLength/numberOfLines
	averageIdentifierLength = totalIdentifierLength/totalIdentifiers
	averageIdPerLine = totalIdentifiers/numberOfLines
	averageSharpCommentsPerLine = totalSharpComments/numberOfLines
	averageEmptyLinesPerLine = totalEmptyLines/numberOfLines
	averageCamelPascalPerLine = totalCamelPascal/numberOfLines
	averageUnderPerLine = totalUnder/numberOfLines
	averageCapsPerLine = totalUpperCase/numberOfLines
	averageDigitsPerLine = totalDigits/numberOfLines
	averageSpacesPerLine = totalSpaces/numberOfLines
	averageBlockLength = totalBlockLength/totalBlocks

	#Get maximum occurrence of any identifier
	if len(idCounts) > 0: #If we have at least one identifier, sort the identifiers and then get the last (maximum as ascending) one
		maximumOccurOfID = idCounts[sorted(idCounts, key=idCounts.get)[-1]] #Source: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
	else:
		maximumOccurOfID = 0 #There were no identifiers. We deal with this case separately because otherwise we get an index error on the [-1] above
	
	#Count remaining things to count and average over number of lines so we don't penalise long code
	#   List of regular expressions to match e.g. comparison operators, bitwise operators, assignment,  arithmetic
	THINGS_TO_LOOK_FOR = ["<|>|==|<=|>=","\^|\~|\&|\|","[^=]=[^=]","\+|\-|\/|\*","\,","\.","for","if|elif|else","def","lambda","while","pass","break","except","in","raise","class","finally","is","return","and","continue","try","as","from","assert","del","global","not","with","async","or","yield","\@","print"]
	##THINGS_TO_LOOK_FOR = ["<|>|==|<=|>=","\^|\~|\&|\|","[^=]=[^=]","\+|\-|\/|\*","\,","\.","for","if|elif|else","def","lambda","while","pass","break|continue","try|except|finally","raise","class","assert","global","with"]
	#THINGS_TO_LOOK_FOR = ["<|>|==|<=|>=","[^=]=[^=]","\+|\-|\/|\*","\,","\.","for","if|elif|else","def"]#"lambda","while"] #,"pass","break","except","in","raise","class","finally","is","return","and","continue","try","as","from","assert","del","global","not","with","async","or","yield","\@","print"]

	#Initialise the matrix of features we will store everything in
	N_FEATURES = 13 + len(THINGS_TO_LOOK_FOR)
	xFeatures = np.zeros((N_FEATURES,1))

	for i,item in enumerate(THINGS_TO_LOOK_FOR): #Search for each thing and fill up the features matrix
		xFeatures[i][0] = len(re.findall(item, codeSnippet))/numberOfLines #One feature is the amount of times each of the THINGS_TO_LOOK_FOR appears in the code, on average per line 
	
	#Save remaining features
	xFeatures[i+1] = averageLineLength
	xFeatures[i+2] = averageIdentifierLength
	xFeatures[i+3] = averageIdPerLine
	xFeatures[i+4] = averageSharpCommentsPerLine
	xFeatures[i+5] = averageEmptyLinesPerLine
	xFeatures[i+6] = averageCamelPascalPerLine
	xFeatures[i+7] = averageUnderPerLine
	xFeatures[i+8] = averageCapsPerLine
	xFeatures[i+9] = averageDigitsPerLine
	xFeatures[i+10] = averageSpacesPerLine
	xFeatures[i+11] = maximumOccurOfID
	xFeatures[i+12] = averageBlockLength
	xFeatures[i+13] = maxIndentDepth
	
	return xFeatures #Just the xFeatures are computed here and returned to caller. In data preparation for training, the caller will add the y label to train on, but in the live IDE the y label will be predicted by the readability features model.

Ws = np.load("ReadabilityWs.npy",allow_pickle=True)
bs = np.load("ReadabilityBs.npy",allow_pickle=True)
sigmaY = 1.0727918602806856
muY = 6.348055239417589
