tab=[float(x) for x in input().split()]
a, b, c = tab[0], tab[1], tab[2]
if a!=0: print(round((c-b)/a, 2))
elif a==b-c: print("NWR")
elif a==0 and b-c!=0.0: print("BR")