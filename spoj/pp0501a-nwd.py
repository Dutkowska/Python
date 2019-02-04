t=int(input())
for i in range(t):
    tab=[int(a) for a in input().split()]
    x, y = tab[0], tab[1]
    minn=min(x,y)
    d=1
    for j in range(1, minn+1):
        if(x%j==0 and y&j==0):
            d=j
    print(d)