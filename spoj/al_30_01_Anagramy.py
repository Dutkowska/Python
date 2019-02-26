# task: https://pl.spoj.com/problems/AL_30_01/
f = lambda text, source: all([c in source for c in text])
res = 0
tab = [x for x in input().split()]
source, num = tab[0], int(tab[1])
for i in range(num):
    text = input()
    if f(text, source): res += 1
print(res)