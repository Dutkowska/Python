from math import *
from sympy import *
import numpy as np
def newton_method(f, df, x0, eps, eps2):
    #f(x)=0, |f(x)|<eps, eps2 - max iterations
    xn=x0
    for i in range(eps2):
        fn=f(xn)
        if abs(fn)<eps:
            print("Iterations: ", i, "; solution:")
            return xn
        Dfn=Df(xn)
        if Dfn == 0: print("No solutions")
        xn=xn-fn/Dfn

fx=input("Enter a polynomian f, such as f(x)=0: ")
f=lambda x: eval(fx)
df=lambda x: np.diff(f)
x0=int(input("Enter a start point: "))
print(newton_method(f,df,x0,0.0001,10))