t=int(input())
for i in range(t):
    tab=[int(x) for x in input().split()]
    length=tab[0]
    tab2=[]
    for j in range(2, length+1):
        tab2.append(tab[j])
    tab2.append(tab[1])
    print(*list(tab2), sep=' ')