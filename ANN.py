import numpy, random, os
a = 1 
bias = 1 
weights = [random.random(),random.random(),random.random()]
def Perceptron(input1, input2, output) :
   outputP = input1*weights[0]+input2*weights[1]+biais*weights[2]
   if outputP > 0 : 
      outputP = 1
   else :
      outputP = 0
   error = output – outputP
   weights[0] += error * input1 * a
   weights[1] += error * input2 * a
   weights[2] += error * biais * a

   for i in range(50) :
   Perceptron(1,1,1) 
   Perceptron(1,0,1) 
   Perceptron(0,1,1) 
   Perceptron(0,0,0) 

x = int(input())
y = int(input())
outputP = x*weights[0] + y*weights[1] + biais*weights[2]
if outputP > 0 : 
   outputP = 1
else :
   outputP = 0
print(x, "or", y, "is : ", outputP)
outputP = 1/(1+numpy.exp(-outputP)) 
