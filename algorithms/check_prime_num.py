def prime(n):
    prime = True
    if n<2: 
        prime=False
    else:
        for i in range(2, int(n/2)):
            if n%i == 0:
                prime=False
                break
    if prime:
        return "it is a prime num"
    else:
        return "It isn't a prime num"