#task: https://pl.spoj.com/problems/DOUGHNUT/
t=int(input())
for i in range(t):
    tab = [int(x) for x in input().split()]
    print('yes') if(tab[0]*tab[2] <= tab[1]) else print('no')