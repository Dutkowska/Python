def fibonacci(n):
    return 1 if (n==1 or n==2) else fibonacci(n-1)+fibonacci(n-2)
fibonacci(5) #1,1,2,3,5 (2+3=5)