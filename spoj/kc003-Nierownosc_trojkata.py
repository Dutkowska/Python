def Triangle(a,b,c):
    return 1 if a>0 and b>0 and c>0 and a+b>c and a+c>b else 0

while True:
    tab=[float(x) for x in input().split()]
    print(Triangle(tab[0], tab[1], tab[2]))