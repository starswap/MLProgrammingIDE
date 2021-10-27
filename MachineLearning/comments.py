#These methods will be shipped in the final solution along with the weights 
import numpy as np
ASSOCIATED_COMMENTS_LIST = ["Calculates the dot product of two vectors","Depth First Search Graph Traversal","Quicksort algorithm (Lomuto Scheme)","Bubble Sort algorithm","Binary Search algorithm"]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!'£$%^&*()[]-=+_;:@~#,<\n.>/?\\|\" {}`\t" #Each is a one hot token
N_TOKENS = len(ALPHABET)+2
HIDDEN_LAYER_NODES = 50

#Activation functions and their derivatives
def softmax(z):
  """Softmax function - acts on vectors to normalise total sum to be out of 1, to create probabilities"""
  t = np.exp(z)
  return t/np.sum(t)

def tanh(matrix):
  """Hyperbolic tangent"""
  matrix = matrix.astype(np.float64)
  return (np.exp(matrix) - np.exp(-matrix))/(np.exp(matrix)+np.exp(-matrix))


def tanh_prime(matrix):
  """Derivative of hyperbolic tan function"""
  return 1-np.square(tanh(matrix))


def stringToMatrixForPrediction(codeBlock):
    """Represents a string of Python code as a one-hot matrix so that it can be passed into the algorithm classifier subroutine."""
    codeBlock = codeBlock.replace("    ","\t")
    blockMatrix = np.ones((N_TOKENS,1)) #Will store a set of one-hot vectors, one for each character in the current block of code, stacked horizontally. All 1s will be the start token
    for char in codeBlock: #each character in current block
        featureMatrix = np.zeros((N_TOKENS,1)) #Create one hot vector for this character, starting with all cold
        try:
            featureMatrix[ALPHABET.index(char)] = 1 #Make the correct one hot
        except ValueError: #Unknown char so use the unk token
            featureMatrix[N_TOKENS-1] = 1

        blockMatrix = np.hstack((blockMatrix,featureMatrix)) #Stack next to other vectors to build matrix of one-hot for the line
        
    return blockMatrix #return code block's onehot representation to caller

def getAlgorithmClassificationComment(inputCode,g_1=tanh,g_1_prime=tanh_prime):
      """Identifies the algorithm whose code is represented by the one hot vector in the inputCode variable, using RNN with trained weights W_a,W_y,b_a,b_y"""

      codeLength = inputCode.shape[1] #Length of algorithm code we want a prediction for

      z_1 = [np.zeros((HIDDEN_LAYER_NODES,1)) for i in range(codeLength)]  #logits on l1 before application of g_1 at each timestep 
      a = [np.zeros((HIDDEN_LAYER_NODES,1)) for i in range(codeLength)] #Activations after application of g_1 at each timestep

      for charIndex in range(0,codeLength-1): 
        #FORWARD PROPAGATION
        x_t = np.reshape(inputCode[:,charIndex],(N_TOKENS,1)) # Current character in the string (one hot), representing the input to this time step (dims 10000* 1)

        z_t_1 = np.matmul(W_a,np.vstack((a[charIndex-1],x_t))) + b_a # Logits for this layer before application of g_1 (dims 100*1)
        z_1[charIndex] = z_t_1 

        a[charIndex] = g_1(z_t_1) #Activations after application of g_1 at this timestep (dims 100*1), will be passed into next timestep. Overall in the input process we consolidate (encode) the input data in such a way that we will be able to make a good prediction afterwards
    
      z_t_2 = np.matmul(W_y,a[charIndex]) + b_y #logits after hidden layer before application of g_2===softmax
      y_hat = softmax(z_t_2) #Normalise probability estimates to be out of 1

      print(y_hat)
      if (y_hat[np.argmax(z_t_2)] < 0.30): #Not confident enough to make a prediction (only 30%)
          return "Unrecognised algorithm"
      else:
        return ASSOCIATED_COMMENTS_LIST[np.argmax(z_t_2)] # Confident enough so return result to caller ready to be put into the code.

W_a = np.load("trainedW_aComment.npy")
W_y = np.load("trainedW_yComment.npy")
b_y = np.load("trainedb_yComment.npy")
b_a = np.load("trainedb_aComment.npy")

