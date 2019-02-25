# task: https://pl.spoj.com/problems/KC004/
while True:
    tab = [int(x) for x in input().split()]
    a, b = tab.pop(0), tab.pop(1)
    print(tab.count(a))