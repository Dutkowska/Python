def pot(a, b):
    if(b==0):
        return 1
    else:
        return (a*pot(a, b-1))
d=int(input())
for i in range(d):
    tab=[int(x) for x in input().split()]
    x,y=tab[0], tab[1]
    w=pot(x%10, 4+y%4)
    print(w%10)