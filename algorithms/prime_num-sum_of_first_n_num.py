#write sum of first n prime numbers:
def prime(x):
    if x<2: return False
    else:
        for i in range(2, int(x/2)):
            if x%i==0:
                return False
    return True
def primesum(n):
    MAX, suma, count=1000, 0, 0
    for i in range(1, MAX):
        if prime(i) and count<n:
            suma+=i
            count+=1
    return suma
primesum(3) #2+3+5