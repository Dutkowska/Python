#give me a solution of continuous function f(x)=0, from interval [a,b]
def bisection_method(f, a, b, n):
    if (f(a)*f(b)>=0): print("Wrong datas.")
    else:
        an, bn = a, b
        for i in range(n):
            cn=(an+bn)/2
            fcn=f(cn)
            if f(cn)==0:
                print("Solution: ")
                return cn
            elif f(an)*f(cn)<0:
                an=an
                bn=cn
            elif f(bn)*f(cn)<0:
                an=cn
                bn=bn
            else:
                print("No solution from this method.")
    return (an+bn)/2

        
fx=input("Enter a continuous function f: ")
f=lambda x: eval(fx)
a=int(input("Enter the beginning of an interval [a,b]: "))
b=int(input("and the end of its: "))
n=int(input("Number of iterations: "))

print(bisection_method(f, a, b, n))