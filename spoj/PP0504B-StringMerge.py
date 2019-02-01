#https://pl.spoj.com/problems/PP0504B/
# i recreated this task: input - aaa bbbb -> aba
def string_merge(a,b):
    c=[j for j in range(min(len(a), len(b)))]
    for i in range(min(len(a), len(b))):
        if min(len(a), len(b))==len(a): c[i]=a[i] if i%2==0 else b[i]
        else: c[i]=b[i] if i%2==0 else a[i]
    return c
#print(''.join(string_merge('aaaaaa', 'bbbbbbbbb')))
t=int(input())
for k in range(t):
    tab=[x for x in input().split()]
    a, b = tab[0], tab[1]
    print(''.join(string_merge(a, b)))