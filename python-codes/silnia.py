from functools import reduce

n=int(input("Podaj liczbe: "))

"""def silnia_rek(n):
    if n>1:
        return n*silnia_rek(n-1)
    if n in (0,1):
        return 1;

def silnia_iter(n):
    suma=1
    if n==0:
        print(1)
    else:
        for i in range(1, n+1):
            suma=suma*i
    print(suma)

print(silnia_rek(n))
print(silnia_iter(n))"""

def silnia(x,y):
    return(x*y)
lis=[]
for i in range(1,n+1):
    lis.append(i)
print(lis)
print(reduce(silnia, lis))


