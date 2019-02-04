def bin_coe(n, k):
    if k==0 or k==n: return 1
    elif n<k: return False
    else: return bin_coe(n-1, k-1)+bin_coe(n-1, k)
t=int(input())
for i in range(t):
    tab=[int(x) for x in input().split()]
    n, k = tab[0], tab[1]
    print(bin_coe(n,k))