def nwd(a,b):
    minn, d  = min(a,b), 1
    for j in range(1,minn+1):
        if(a%j==0 and b%j==0): d=j
    return d

t = int(input())
for i in range(t):
    tab = [int(h) for h in input().split()]
    x, y = tab[0], tab[1]
    print((x*y)/nwd(x,y))