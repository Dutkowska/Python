def factorial_recursion(n):
    return 1 if n==0 else n*factorial_recursion(n-1)
print(factorial_recursion(5))