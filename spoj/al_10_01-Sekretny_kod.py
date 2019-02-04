#task: https://pl.spoj.com/problems/AL_10_01/
t=int(input())
for i in range(t):
    tab=[x for x in input().split()]
    ender = 1
    num = tab[1].count('?')
    if num == 0: print('1') #none ?
    elif num == 1 and tab[0] == 1: print('10') # if: 1 ?
    elif tab[1][0]=='?':
        ender*=9
        ender*=10**(num-1)
        print(ender)
    else:
        ender*=10**(num)
        print(ender)