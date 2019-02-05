# (n k) = n! / k!(n-1)! symbol Newtona
def factorial(a):
    return 1 if (a==0) else a*factorial(a-1)
def bin_coe(n, k):
    if n<k: print("Wrong numbers")
    else: return factorial(n)/(factorial(k)*factorial(n-k))

#print(bin_coe(4,2))
