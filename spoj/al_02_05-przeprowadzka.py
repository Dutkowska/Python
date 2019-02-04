#task: https://pl.spoj.com/problems/AL_02_05/
t = int(input())
for i in range(t):
    tab = [int(x) for x in input().split()]
    num, mx = tab[0], tab[1]
    boxes, weight = 0, 0
    tab2 = list(map(int, input().split()))
    while len(tab2) != 0:
        for i in tab2:
            if i + weight <= mx:
            #if previous + new one are still lightest than mx
                weight += i
                tab2.remove(i)
        weight = 0
        boxes += 1
    print(boxes - 1)