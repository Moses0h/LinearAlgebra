import sys
import numpy as np

J = int(input("Row : "))
K = int(input("Col : "))

m = 0
M = np.zeros((J,K), float)  #creates a zero matrix 
D = np.zeros((J,K), float)

for j in range (0,J): #starts a counter from 0 to J
        print ('Input the entries of equation ' + str(j+1)) #tell the user to input specific entries each entry
        M[j,:] = input().split() #go to matrix M into row j and all the columns, which the use will input
        
print (M)

for j in range (m,J):
        for k in range (0,K-1):          
                if M[j,k] == 1:
                        for a in range(j+1,J):
                                M[a,:] = -M[a,k]*M[j,:] + M[a,:] #fill in
                        for a in range (0,j):
                                M[a,:] = -M[a,k]*M[j,:] + M[a,:] #fill in   
                        m += 1
                        break
                elif M[j,k] != 1 and M[j,k] != 0:
                        M[j,:] = M[j,:]/M[j,k]
                        for a in range (j+1,J):
                                M[a,:] = -M[a,k]*M[j,:] + M[a,:] #fill in
                        for a in range (0,j):
                                M[a,:] = -M[a,k]*M[j,:] + M[a,:] #fill in
                        m += 1
                        break
                        
                        
                         
                
print (M[:,:])