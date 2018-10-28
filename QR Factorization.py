import sys
import numpy as np
import copy

# methods

def dotVectors(vector1, vector2):
    constant = 0
    for num in range (0,len(vector1)):
        constant = constant + vector1[num]*vector2[num]
    return constant
    
def findMagnitude(vector):
    magnitude = 0
    for num in range (0,len(vector)):
        magnitude += vector[num] ** 2
        
    magnitude = magnitude ** (0.5)
    return magnitude
    
def findUnitVector(vector):
    unitVector = copy.deepcopy(vector)
    magnitude = findMagnitude(unitVector)
    for num in range (0,len(vector)):
        unitVector[num] = unitVector[num] / magnitude 
    return unitVector
     
def findQMatrix(M):
    orthgnlM = np.zeros((M.shape[0],M.shape[1]), float) 
    orthgnlM[:,0] = findUnitVector(M[:,0])
    for c in range (1, M.shape[1]): 
        orthgnlV = M[:,c] 
        for cc in range(0,c):
                    orthgnlV = orthgnlV - [x * dotVectors(orthgnlM[:,cc],M[:,c]) for x in orthgnlM[:,cc]]
        orthgnlM[:,c] = findUnitVector(orthgnlV)
    return orthgnlM
    

def findRMatrix(M):
    orthgnlM = np.zeros((M.shape[0],M.shape[1]), float)
    R = np.zeros((M.shape[1],M.shape[1]), float) 
 
    orthgnlM[:,0] = findUnitVector(M[:,0])
    
    for c in range (1, M.shape[1]): 
        orthgnlV = M[:,c] 
        for cc in range(0,c):
                    orthgnlV = orthgnlV - [x * dotVectors(orthgnlM[:,cc],M[:,c]) for x in orthgnlM[:,cc]]
        R[c,c] = findMagnitude(orthgnlV)
        orthgnlM[:,c] = findUnitVector(orthgnlV)
        
    for r in range (0, R.shape[0]):
        for c in range (0, R.shape[1]):
            if(r == 0 & c == 0):
                R[r,c] = findMagnitude(M[:,0])
            if(r < c):
                R[r,c] = dotVectors(orthgnlM[:,r],M[:,c])
    return R
     
     
     
     
     
     
R = int(input("Row : "))
C = int(input("Col : "))

m = 0
M = np.zeros((R,C), float)  

for j in range (0,C): 
        print ('Input the entries of column ' + str(j+1)) #enter each number in COLUMN followed by a space in one line
        M[:,j] = input().split() 
print()
        
print('Q: ')
print(findQMatrix(M))
print('R: ')
print(findRMatrix(M))


