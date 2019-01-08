def factorial_recursion(n):
    if n==0: return 1
    else: return n*factorial_recursion(n-1)