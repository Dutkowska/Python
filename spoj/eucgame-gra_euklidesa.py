t=int(input())
for i in range(t):
    tab=[int(x) for x in input().split()]
    a, b=tab[0], tab[1]
    while(a<b or b<a):
        if(a<b): b-=a
        else: a-=b
    print(a+b)