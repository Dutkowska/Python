#task: https://pl.spoj.com/problems/JWSPLIN/
#check if 3 point are colinear
def colinear(x1, y1, x2, y2, x3, y3):
    AB=0 if x2-x1==0 else (y2-y1)/(x2-x1)
    BC=0 if x3-x2==0 else (y3-y2)/(x3-x2)
    print("TAK") if AB == BC else print("NIE")

t=int(input())
for i in range(t):
    tab=[int(x) for x in input().split()]
    colinear(tab[0], tab[1], tab[2], tab[3], tab[4], tab[5])