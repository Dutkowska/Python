#task: https://pl.spoj.com/problems/WSEGA/
t = int(input())
for i in range(t):
    tab = [int(x) for x in input().split()]
    x = tab.pop(0) - 1
    leg = sum(tab)
    print(x + leg)
