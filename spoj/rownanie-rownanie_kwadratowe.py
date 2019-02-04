#write numbers of roots from quadratic equation ax^2+bx+c=0
while True:
    tab=[float(x) for x in input().split()]
    a, b, c=tab[0], tab[1], tab[2]
    delta=(b*b)-(4*a*c)
    if delta<0: print("0")
    elif delta==0: print("1")
    else: print("2")