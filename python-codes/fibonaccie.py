def fib_iter(n):
    a=1
    b=1
    l=[]
    l.append(a)
    l.append(b)
    for i in range(2,n):
        c=a+b
        l.append(c)
        a=b
        b=c
    print(c)
    n="kolejne elementy ciągu: "
    print("%s" % ("kolejne elementy ciągu: "))
    print(*l, sep=',')

fib_iter(5)

def fib_rek(n):
    fib=[0,1]
    new=0
    for i in range(n-1):
        new=fib[-1]+fib[-2]
        fib.append(new)
        #print(fib)
    print(fib)

fib_rek(5)
