#fermats factorization, help find prime numbers dividing n:
#with using p=x^2-y^2=(x+y)(x-y), p-odd number
#a=x+y; b=x-y
from math import *
def fermats(p):
    while(p%2==0):
        p/=2
        print(2)
    x=ceil(sqrt(p))
    y2=x*x-p
    y=floor(sqrt(y2))
    while(x+y<p):
        if(y2==y*y):
            a=x+y
            b=x-y
            if(b==1): break
            fermats(a)
            fermats(b)
        x+=1
        y2=x*x-p
        y=floor(sqrt(y2))
    print(p)
    
fermats(78)