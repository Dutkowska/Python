# task: https://pl.spoj.com/problems/BICAKE/polski/
from math import *
while True:
    n = int(input())
    if n == 1: print("0")
    else:
        m = (n - 1) * 2.0
        m = -m
        delta = 1.0 - 4.0 * m
        x_1 = (-1.0 + sqrt(delta)) / 2.0
        x_2 = (-1.0 - sqrt(delta)) / 2.0
        if (x_1 > 0): print(ceil(x_1))
        elif (x_2 > 0): print(ceil(x_2))