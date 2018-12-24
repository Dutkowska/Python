#t - number of tests; 
#find numbers ai < n such that: ai divided by x, not divided by y
t=int(input())
for i in range(t):
    tab=[int(x) for x in input().split()]
    n, x, y = tab[0], tab[1], tab[2]
    tabnew=[]
    for j in range(x, n):
        if j%x==0 and j%y!=0: tabnew.append(j)
    print(*tabnew, sep=' ')