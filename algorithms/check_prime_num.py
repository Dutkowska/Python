def prime(n):
    if n<2: return False
    else:
        for i in range(2, int(n/2+1)):
            if n%i == 0: return False
    return True
#print(prime(4))

#using comprehensions:
def prime_com(n):
    s = True if all(n % x != 0 for x in range(2, int(n/2 + 1))) else False
    return s
#print(prime_com(5))