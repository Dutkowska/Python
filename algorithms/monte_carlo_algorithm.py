import random
import math
pc=0 #number of points in the circle
psq=int(input()) #number of points in the square


for i in range(psq):
    x=random.random()
    y=random.random()
    if(x*x+y*y<=1): #check if pts are inside the circle, r=1
        pc+=1
        
pi=4*pc/psq        
print("result: ", pi)
print("diff: ", abs(math.pi-pi))