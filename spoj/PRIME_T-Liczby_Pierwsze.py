def switcher(x):
    return{
        0: "NIE",
        1: "TAK",
    }[x] #default: .get(x, "NIE")

n=int(input())
for i in range(n):
    l = int(input())
    p = 1 #is primary
    if(l == 1): p=0
    for j in range(2,l):
        if(l%j==0): p=0
    print(switcher(p))
    p=1