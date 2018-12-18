def rol(tabb):
    newtab=tabb[1:]
    newtab.append(tabb[0])
    return newtab
    #or append pop 0
t=int(input())
for i in range(t):
    tab=input().split()
    tab2=rol(tab[1:])
    print(*list(tab2), sep=' ')