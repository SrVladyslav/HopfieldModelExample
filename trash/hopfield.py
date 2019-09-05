#created by Sr_Vladyslav
import numpy as np

#Hopfield network:
#OFFLine
#remember that:
#W = T^t * T - I
#Wi = W0 + W1 + ... + Wi
#Also we need some function
#f(x) -> if x < 0 so = -1 , 
#	  -> if x >= 0 so = 1

#Defining identity matrix (I) using numpy
def createI(x):
	return (np.identity(x))


#Defining W matrix formula
def solveW(T):
	#Lets create our matrices 
	T = np.matrix(T)
	print(f"T=",T)
	#T transpose matrix
	T1 = np.matrix(T.transpose())
	print(f"T1=", T1)
	#Identity matrix  
	I = np.matrix(createI(len(T)))
	print(f"I=", I)
	#Let`s use our formula to find W 
	W = T1 * T - I
	print(f"W", T1 * T - I)
	#And return the solution
	return W
#defining the searching algorythm
def solve(E):
	#E * W must be equals to some of our learned items, in case of difference we'll iterate again
	#in this particular case it will be perfect solution with 1 iteration only
	S = E * W
	#Matrix to Array 
	Sa = np.squeeze(np.asarray(S))
	#Now we apply the function f(x)
	for x in range(0, len(Sa)):
		if Sa[x] < 0:
			Sa[x] = -1.0
		else:
			Sa[x] = 1.0
	#Turning the array into the matrix again
	S = np.matrix(Sa)
	#Our basic prediction
	if (S == E0).all():
		print("The solution is E0")
	elif (S == E1).all():
		print("The solution is E1")
	else:
		print("More loops needed...")


#Test:we suppose that we have 3X3 matrix with two pictures to learn like:
#  111   010
#  010   101
#  010   101
#  	w0    w1
#  
#1) We'll create two matrix vectors of figures represented before 
#1.1) 
E0 = np.matrix([1,1,1,-1,1,-1,-1,1,-1])
print(f"E0=",E0)
#1.2) 
E1 = np.matrix([-1,1,-1,1,-1,1,1,-1,1])
print(f"E1=",E1)

#2)We solve the W0 for E0
W0 = solveW(E0)
print(f"W0=",W0)

#3)We solve the W1 for E1
W1 = solveW(E1)
print(f"W1=",W1)

#4)Now we must sum W0 and W1 to obtain the final W.
#That's our final trained Hopfield model, just ready for use to proove inputs
W = W0 + W1
print(f"W=", W)



#6)Enjoy and play 
print("======================================================================================")
print(">>This solution must be E1")
solve(np.matrix([-1,-1,-1,-1,-1,1,1,-1,1]))

print(">>This solution must be E0")
solve(np.matrix([1,-1,1,-1,-1,-1,-1,1,-1]))

print(">>This solution must be E1")
solve(np.matrix([1,-1,-1,1,-1,1,-1,-1,1]))

print(">>This solution must be E1")
#solve(np.matrix([]))