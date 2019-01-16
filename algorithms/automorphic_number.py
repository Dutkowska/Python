"""is a number whose square "ends" in the same digits as the number itself.
n=n*n mod(10^k), k-length of n"""
def auto_numb(n):
    a=10;
    while(n>a): a*=10
    if((n*n)%a==n): return True
    else: return False
auto_numb(25) #25*25=...25