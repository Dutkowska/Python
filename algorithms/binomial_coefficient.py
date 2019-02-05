def factorial(a):
    return 1 if a==0 else a*factorial(a-1)
def bin_coe(n, k):
    print("Wrong numbers.") if n<k else print(factorial(n)/(factorial(k)*factorial(n-k)))
n, k =int(input("n: ")), int(input("k: "))
bin_coe(n, k)