import numpy as np #Linear algebra library

def processCodeToMatrix(codeContents):
	"""Takes a string of user code and processes it according to the features the estimation level model uses."""
	
	THINGS_TO_LOOK_FOR = ["for","if","def","lambda","while","await","else","elif","import","pass","break","except","in","raise","class","finally","is","return","and","continue","try","as","from","assert","del","global","not","with","async","or","yield","@","print"]#The number of times each of these appears in code on an article's page will be used as a feature. I will add more as necessary. 
	N_FEATURES = len(THINGS_TO_LOOK_FOR) + 5 
      
	datasetMatrix = np.zeros((N_FEATURES,1)) #Initialise the matrix which will contain the data we collect

	for i,item in enumerate(THINGS_TO_LOOK_FOR):
	    datasetMatrix[i][0] = codeContents.count(item)/len(codeContents.split("\n")) #One feature is the amount of times each of the THINGS_TO_LOOK_FOR appears in the code, on average per line 

	datasetMatrix[i+1][0]= len(codeContents.split("\n")) #Number of lines
	datasetMatrix[i+2][0] = len(codeContents) #Total length
	
	totalCommentLength = 0
	totalComments = 0
	maxIndentDepth = 0 
	for line in codeContents.split("\n"): #Go through all lines in the code
	    if len(line) == 0: #Skip blank lines
		    continue
	    if line[0] == "#": #all g4g articles have comments on their own lines so we can just check if a hash appears at the start of the line.
		    totalComments += 1
		    totalCommentLength += len(line)
	    if line[0] == "\xa0" and line.count("\xa0") > maxIndentDepth: #Get indentation depth (\xa0 is a non breaking space character, used to indent code by G4G)
		    maxIndentDepth = line.count("\xa0")

	#save calculated features to matrix
	datasetMatrix[i+3] = maxIndentDepth
	datasetMatrix[i+4] = totalCommentLength
	datasetMatrix[i+5] = totalComments

	MU = np.matrix([[0.05082507],[0.02822244],[0.03304276],[0.00191462],[0.00281161],[0.],[0.00937306],[0.00116156],[0.04998702],[0.00768705],[0.00186048],[0.00538154],[0.43338024],[0.00221055],[0.01573597],[0.00114189],[0.09830038],[0.01814295],[0.03698907],[0.00020747],[0.00688233],[0.07782559],[0.02803602],[0.00043255],[0.01624842],[0.00271568],[0.01243397],[0.01541601],[0.],[0.19692068],[0.00274482],[0.00381828],[0.14567307],[74.62557078],[1792.64383562],[12.2739726],[434.63013699],[14.24200913]])
	SIGMA = np.matrix([[0.07054681],[0.05446474],[0.04842599],[0.01293988],[0.01049264],[1.],[0.02710312],[0.00695543],[0.06562021],[0.02777971],[0.01265887],[0.02178715],[0.26618716],[0.00999644],[0.04285446],[0.01002316],[0.12348276],[0.03604208],[0.05152651],[0.00170739],[0.02043596],[0.10019193],[0.0436205],[0.00461246],[0.0711935],[0.01665319],[0.03046686],[0.03822321],[1.],[0.15501729],[0.02100033],[0.01774738],[0.12924724],[63.51310571],[1604.57555551],[12.32133718],[442.45008511],[15.1859364]])

	#Normalise in the same way the training data was normalised.
	datasetMatrix -= MU
	datasetMatrix /= SIGMA    
	return datasetMatrix

def tanh(matrix):
	"""The hyperbolic tangent activation function. Used as the default activation for all layers except the last one here"""
	return (np.exp(matrix) - np.exp(-matrix))/(np.exp(matrix)+np.exp(-matrix))

def tanh_prime(matrix):
	"""Derivative of the hyperbolic tangent activation function with respect to the input matrix"""
	return 1-np.square(tanh(matrix))

def softmax(matrix):
	"""Computes the soft maximum vector-valued activation function on each column of a matrix. Used as the final layer activation since we are doing multiclass classification"""
	temp = np.exp(matrix) #Compute elementwise e^n where e is Euler's number ~ 2.718
	return temp/np.sum(temp,axis=0) #Normalise the result so that the columns sum to 1, by dividing through by columnwise sum

def forwardProp(X,Ws,bs): 
	"""Performs 1 forward propagation through the network to get a predicted class (code level) for X (input features - each column is one training example so vectorised), Ws (list of weights), bs (list of biases)"""
	As = [X] #Activations at each layer, with layer 0 having the input features as its activations
	Zs = [] #Z values (input to the activation function === matrix product of Ws[current layer] and a[layer before] + bs[current layer])
    
	for i in range(len(Ws)-1): #For every layer in the network except the last one, which is dealt with separately as it has a different activation,
	    Zs.append(np.matmul(Ws[i],As[i]) + bs[i]) #Compute the next Z value by multiplying the corresponding weights with the previous layer's activations and adding the biases
	    As.append(tanh(Zs[-1])) #Compute this layer's activation by applying the tanh activation function

	#Forward prop the final layer
	Z_final = np.matmul(Ws[-1],As[-1]) + bs[-1] #Compute Z as usual 
	Zs.append(Z_final) #Save the final Z value
	As.append(softmax(Z_final)) #Compute the softmax activation over the final logits and save as the final activations.
	return Zs,As #Return the Z and Activation values, which will be needed for backprop 

def classifyCodeLevel(featureMatrix):
	"""Runs forward propagation on the network with the provided weights and input features and returns the final layer activations which is a matrix of probabilities for each possible classification"""
	Zs, As = forwardProp(featureMatrix,Ws,bs)
	return As[-1] #===y_hat

Ws = np.load("G4GWs.npy",allow_pickle=True)
bs = np.load("G4GBs.npy",allow_pickle=True)
