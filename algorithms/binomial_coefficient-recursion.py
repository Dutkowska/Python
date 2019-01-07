def bin_coe(n, k):
    if k==0 or k==n: return 1
    elif n<k: return "Wrong numbers"
    else: return bin_coe(n-1, k-1)+bin_coe(n-1, k)
n=int(input("n: "))
k=int(input("k: "))
print(bin_coe(n, k))