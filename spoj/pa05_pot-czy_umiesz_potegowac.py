#task: https://pl.spoj.com/problems/PA05_POT/
def pot(a, b):
    return 1 if(b == 0) else (a*pot(a, b-1))
d = int(input())
for i in range(d):
    tab = [int(x) for x in input().split()]
    x,y = tab[0], tab[1]
    print(pot(x%10, 4+y%4)%10)