#task: https://pl.spoj.com/problems/GLUTTON/
from math import *
doba=60*60*24
t=int(input())
for i in range(t):
    suma=0
    tab=[int(x) for x in input().split()]
    n, m=tab[0], tab[1]
    for j in range(n):
        sec=int(input())
        suma+=floor(doba/sec);
    if suma!=0:
        print(ceil(suma/m))
    else:
        print(0)