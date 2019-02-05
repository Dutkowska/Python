"""is a number whose square "ends" in the same digits as the number itself.
n=n*n mod(10^k), k-length of n"""
def auto_numb(n):
    a=10;
    while(n>a): a*=10
    return True if((n*n)%a==n) else False
auto_numb(25) #25*25=...25