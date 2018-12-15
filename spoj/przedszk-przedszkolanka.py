def nwd(a,b):
    minn=min(a,b)
    d=1
    for j in range(1,minn+1):
        if(a%j==0 and b%j==0):
            d=j
    return d

t=int(input())
for i in range(t):
    inpu=[int(h) for h in input().split()]
    x=inpu[0]
    y=inpu[1]
    w=(x*y)/nwd(x,y)
    print(w)