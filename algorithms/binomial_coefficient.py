def factorial(a):
    if a==0: return 1
    else: return a*factorial(a-1)
n=int(input("n: "))
k=int(input("k: "))
if n<k:
    print("Wrong numbers.")
else:
    bin_coe=factorial(n)/(factorial(k)*factorial(n-k))
    print(bin_coe)