t=int(input())
for i in range(t):
    n=int(input())
    tab=[int(x,n+1) for x in input().split()] #n - base
    print(sum(tab))