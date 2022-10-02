# Developer:
# Kareem Mohamed Wardany
# ----------------------------------------

class GlobalAlignment:
	def __init__(self,gap,match,mismatch):
		self.gap = gap
		self.match = match
		self.mismatch = mismatch

	def MatchMismatch(self,x,y): #return value of match or mismatch
		if x != y:
			return self.mismatch
		else:
			return self.match
def ReturnBlosum62Value(c1, c2):
    #blosum 62 values for proteins
    blosum62 = {
        ('W', 'F'): 1, ('L', 'R'): -2, ('S', 'P'): -1, ('V', 'T'): 0,
        ('Q', 'Q'): 5, ('N', 'A'): -2, ('Z', 'Y'): -2, ('W', 'R'): -3,
        ('Q', 'A'): -1, ('S', 'D'): 0, ('H', 'H'): 8, ('S', 'H'): -1,
        ('H', 'D'): -1, ('L', 'N'): -3, ('W', 'A'): -3, ('Y', 'M'): -1,
        ('G', 'R'): -2, ('Y', 'I'): -1, ('Y', 'E'): -2, ('B', 'Y'): -3,
        ('Y', 'A'): -2, ('V', 'D'): -3, ('B', 'S'): 0, ('Y', 'Y'): 7,
        ('G', 'N'): 0, ('E', 'C'): -4, ('Y', 'Q'): -1, ('Z', 'Z'): 4,
        ('V', 'A'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('V', 'E'): -2,
        ('T', 'N'): 0, ('P', 'P'): 7, ('V', 'I'): 3, ('V', 'S'): -2,
        ('Z', 'P'): -1, ('V', 'M'): 1, ('T', 'F'): -2, ('V', 'Q'): -2,
        ('K', 'K'): 5, ('P', 'D'): -1, ('I', 'H'): -3, ('I', 'D'): -3,
        ('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
        ('P', 'H'): -2, ('F', 'Q'): -3, ('Z', 'G'): -2, ('X', 'L'): -1,
        ('T', 'M'): -1, ('Z', 'C'): -3, ('X', 'H'): -1, ('D', 'R'): -2,
        ('B', 'W'): -4, ('X', 'D'): -1, ('Z', 'K'): 1, ('F', 'A'): -2,
        ('Z', 'W'): -3, ('F', 'E'): -3, ('D', 'N'): 1, ('B', 'K'): 0,
        ('X', 'X'): -1, ('F', 'I'): 0, ('B', 'G'): -1, ('X', 'T'): 0,
        ('F', 'M'): 0, ('B', 'C'): -3, ('Z', 'I'): -3, ('Z', 'V'): -2,
        ('S', 'S'): 4, ('L', 'Q'): -2, ('W', 'E'): -3, ('Q', 'R'): 1,
        ('N', 'N'): 6, ('W', 'M'): -1, ('Q', 'C'): -3, ('W', 'I'): -3,
        ('S', 'C'): -1, ('L', 'A'): -1, ('S', 'G'): 0, ('L', 'E'): -3,
        ('W', 'Q'): -2, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 0,
        ('N', 'R'): 0, ('H', 'C'): -3, ('Y', 'N'): -2, ('G', 'Q'): -2,
        ('Y', 'F'): 3, ('C', 'A'): 0, ('V', 'L'): 1, ('G', 'E'): -2,
        ('G', 'A'): 0, ('K', 'R'): 2, ('E', 'D'): 2, ('Y', 'R'): -2,
        ('M', 'Q'): 0, ('T', 'I'): -1, ('C', 'D'): -3, ('V', 'F'): -1,
        ('T', 'A'): 0, ('T', 'P'): -1, ('B', 'P'): -2, ('T', 'E'): -1,
        ('V', 'N'): -3, ('P', 'G'): -2, ('M', 'A'): -1, ('K', 'H'): -1,
        ('V', 'R'): -3, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -2,
        ('V', 'V'): 4, ('M', 'I'): 1, ('T', 'Q'): -1, ('I', 'G'): -4,
        ('P', 'K'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('I', 'C'): -1,
        ('Z', 'D'): 1, ('F', 'R'): -3, ('X', 'K'): -1, ('Q', 'D'): 0,
        ('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -2, ('Z', 'H'): 0,
        ('B', 'L'): -4, ('B', 'H'): 0, ('F', 'F'): 6, ('X', 'W'): -2,
        ('B', 'D'): 4, ('D', 'A'): -2, ('S', 'L'): -2, ('X', 'S'): 0,
        ('F', 'N'): -3, ('S', 'R'): -1, ('W', 'D'): -4, ('V', 'Y'): -1,
        ('W', 'L'): -2, ('H', 'R'): 0, ('W', 'H'): -2, ('H', 'N'): 1,
        ('W', 'T'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('W', 'P'): -4,
        ('L', 'D'): -4, ('B', 'I'): -3, ('L', 'H'): -3, ('S', 'N'): 1,
        ('B', 'T'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('E', 'Q'): 2,
        ('Y', 'G'): -3, ('Z', 'S'): 0, ('Y', 'C'): -2, ('G', 'D'): -1,
        ('B', 'V'): -3, ('E', 'A'): -1, ('Y', 'W'): 2, ('E', 'E'): 5,
        ('Y', 'S'): -2, ('C', 'N'): -3, ('V', 'C'): -1, ('T', 'H'): -2,
        ('P', 'R'): -2, ('V', 'G'): -3, ('T', 'L'): -1, ('V', 'K'): -2,
        ('K', 'Q'): 1, ('R', 'A'): -1, ('I', 'R'): -3, ('T', 'D'): -1,
        ('P', 'F'): -4, ('I', 'N'): -3, ('K', 'I'): -3, ('M', 'D'): -3,
        ('V', 'W'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('P', 'N'): -2,
        ('K', 'A'): -1, ('M', 'L'): 2, ('K', 'E'): 1, ('Z', 'E'): 4,
        ('X', 'N'): -1, ('Z', 'A'): -1, ('Z', 'M'): -1, ('X', 'F'): -1,
        ('K', 'C'): -3, ('B', 'Q'): 0, ('X', 'B'): -1, ('B', 'M'): -3,
        ('F', 'C'): -2, ('Z', 'Q'): 3, ('X', 'Z'): -1, ('F', 'G'): -3,
        ('B', 'E'): 1, ('X', 'V'): -1, ('F', 'K'): -3, ('B', 'A'): -2,
        ('X', 'R'): -1, ('D', 'D'): 6, ('W', 'G'): -2, ('Z', 'F'): -3,
        ('S', 'Q'): 0, ('W', 'C'): -2, ('W', 'K'): -3, ('H', 'Q'): 0,
        ('L', 'C'): -1, ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4,
        ('W', 'S'): -3, ('S', 'E'): 0, ('H', 'E'): 0, ('S', 'I'): -2,
        ('H', 'A'): -2, ('S', 'M'): -1, ('Y', 'L'): -1, ('Y', 'H'): 2,
        ('Y', 'D'): -3, ('E', 'R'): 0, ('X', 'P'): -2, ('G', 'G'): 6,
        ('G', 'C'): -3, ('E', 'N'): 0, ('Y', 'T'): -2, ('Y', 'P'): -3,
        ('T', 'K'): -1, ('A', 'A'): 4, ('P', 'Q'): -1, ('T', 'C'): -1,
        ('V', 'H'): -3, ('T', 'G'): -2, ('I', 'Q'): -3, ('Z', 'T'): -1,
        ('C', 'R'): -3, ('V', 'P'): -2, ('P', 'E'): -1, ('M', 'C'): -1,
        ('K', 'N'): 0, ('I', 'I'): 4, ('P', 'A'): -1, ('M', 'G'): -3,
        ('T', 'S'): 1, ('I', 'E'): -3, ('P', 'M'): -2, ('M', 'K'): -1,
        ('I', 'A'): -1, ('P', 'I'): -3, ('R', 'R'): 5, ('X', 'M'): -1,
        ('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 1, ('X', 'E'): -1,
        ('Z', 'N'): 0, ('X', 'A'): 0, ('B', 'R'): -1, ('B', 'N'): 3,
        ('F', 'D'): -3, ('X', 'Y'): -1, ('Z', 'R'): 0, ('F', 'H'): -1,
        ('B', 'F'): -3, ('F', 'L'): 0, ('X', 'Q'): -1, ('B', 'B'): 4
    }
    return blosum62[(c1, c2)]

def zeroMatrix(sizeX, sizeY, matrix):

    # Zero-ing the matrix
	for i in range(len(sizeX)+1):
		matrix2 = []
		for j in range(len(sizeY)+1):
			matrix2.append(0)
		matrix.append(matrix2)

def getMatrix(size1,size2,gap):

    matrix = []
    zeroMatrix(size1, size2, matrix)

    # Adding Gap values in first row and column
    for j in range(1,len(size2)+1):
        matrix[0][j] = j*gap
    for i in range(1,len(size1)+1):
        matrix[i][0] = i*gap
    return matrix

def traceback(size1,size2):

    matrix = []
    zeroMatrix(size1, size2, matrix)

	# First row and column with "left" or "up" & "-" for [0][0]
    for j in range(1,len(size2)+1):
        matrix[0][j] = '🠔'
    for i in range(1,len(size1)+1):
        matrix[i][0] = '🠕'
    matrix[0][0] = '-'
    return matrix


def globalAlign(x,y,globalAlignment):
	
    # Align sequences globally
	matrix = getMatrix(x,y,globalAlignment.gap)
	traceBack = traceback(x,y)
    # Adding match and mismatch values to diagonal and gap to up and left
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			left = matrix[i][j-1] + globalAlignment.gap
			up = matrix[i-1][j] + globalAlignment.gap
			diag = matrix[i-1][j-1] + globalAlignment.MatchMismatch(x[i-1],y[j-1])
			matrix[i][j] = max(left,up,diag) # Take the max values from them and add it to the matrix[i][j]
            
            # For the traceback matrix
			if matrix[i][j] == left:
				traceBack[i][j] = '🠔'
			elif matrix[i][j] == up:
				traceBack[i][j] = '🠕'
			else:
				traceBack[i][j] = '⬉'
	return matrix,traceBack
def proteinGlobalAlign(x,y,globalAlignment):
	
    # Align proteins sequences globally using our functions
    matrix = getMatrix(x,y,globalAlignment.gap)
    traceBack = traceback(x,y)

    
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            left = matrix[i][j-1] + globalAlignment.gap
            up = matrix[i-1][j] + globalAlignment.gap
            # Exception handling for the opposite values in blosum 62
            try:
                diag = matrix[i-1][j-1] + ReturnBlosum62Value(x[i-1],y[j-1])
            except:
                diag = matrix[i-1][j-1] + ReturnBlosum62Value(y[j-1],x[i-1])
            matrix[i][j] = max(left,up,diag)
            
            # For the traceback matrix
            if matrix[i][j] == left:
                traceBack[i][j] = '🠔'
            elif matrix[i][j] == up:
                traceBack[i][j] = '🠕'
            else:
                traceBack[i][j] = '⬉'
    return matrix,traceBack

def getAlignedSequences(x,y,matrix,traceBack):
	
    # Bottom-up traceback
	xseq = []
	yseq = []
	i = len(x)
	j = len(y)
	while(i > 0 or j > 0):
		if traceBack[i][j] == '⬉':
			# Match
			xseq.append(x[i-1])
			yseq.append(y[j-1])
			i = i-1
			j = j-1
		elif traceBack[i][j] == '🠔':
			# Left
			xseq.append('-')
			yseq.append(y[j-1])
			j = j-1
		elif traceBack[i][j] == '🠕':
			# Up
			xseq.append(x[i-1])
			yseq.append('-')
			i = i-1
		elif traceBack[i][j] == 'done':
			# Reaching [0][0]
			break
	return xseq,yseq

def printMatrix(matrix): # Matrix printing

	for z in range(len(matrix)):
		print(matrix[z])
	print()



# MAIN FUNCTION

# Entering 1 for DNA Seqquencing & 2 for Protein Sequencing
print("1-DNA Seqquencing \n2-Protein Sequencing")
choice = input("Choice:")

if choice == "1": # DNA Seqquencing

    x = input("First Sequence:").upper()
    y = input("Second Sequence:").upper()

    print('Sequences are:')
    print(x)
    print(y)
    print(" ")
    globalAlignment = GlobalAlignment(-1,1,-2) #Gap, Match and Mismatch values
    matrix,traceBack = globalAlign(x,y,globalAlignment)

    xseq,yseq = getAlignedSequences(x,y,matrix,traceBack)

    print('Aligned Sequences are:')
    #*seq[::-1] is used to print the whole sequence in one line
    print(*xseq[::-1])
    print(*yseq[::-1])

    print('Global Alignment Matrix:')
    printMatrix(matrix)

    print('Trace Back Matrix:')
    printMatrix(traceBack)

elif choice == "2": # Protein Sequencing
    x = input("First Protein Sequence:").upper()
    y = input("Second Protein Sequence:").upper()

    print('Protein Sequences are:')
    print(x)
    print(y)
    print(" ")
    globalAlignment = GlobalAlignment(-1,1,-2) #Gap, Match and Mismatch values
    matrix,traceBack = proteinGlobalAlign(x,y,globalAlignment)

    xseq,yseq = getAlignedSequences(x,y,matrix,traceBack)

    print('Aligned Sequences are:')
    #*seq[::-1] is used to print the whole sequence in one line
    print(*xseq[::-1])
    print(*yseq[::-1])

    print('Global Alignment Matrix:')
    printMatrix(matrix)

    print('Trace Back Matrix:')
    printMatrix(traceBack)

else:
    print("Invalid Choice!")