#input: t - num of tests /n n - length of list and list
#output: firstly write numbers from even indexes, then from odd indexes
t=int(input())
for i in range(t):
    tab=[int(x) for x in input().split()]
    print(*(tab[2:tab[0]+1:2]+tab[1:tab[0]+1:2]), sep=' ')