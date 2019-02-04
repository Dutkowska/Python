t = int(input())
for i in range(t):
    tab = [int(x) for x in input().split()]
    v, w = tab[0], tab[1]
    print(2*v*w/(v+w))