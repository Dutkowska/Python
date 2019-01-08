def factorial_it(n):
    if n==0: return 1;
    else:
        b=1
        while(n>0):
            b*=n
            n-=1
        return b