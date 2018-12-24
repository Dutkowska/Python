#r - radius of 2 circles, d - distance between them
while True:
    tab=[int(x) for x in input().split()]
    r, d, pi=tab[0], tab[1], 3.141592654
    p=(r**2 - (d/2)**2)*pi
    print(round(p, 2))