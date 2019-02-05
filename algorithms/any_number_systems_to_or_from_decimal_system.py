'''chose your number system and then convert number from/to this system to/from decimal system
example: 8, s (from 8-base), 345 -> 229 .... 2, d (to 2-base), 21 -> 10101;'''
def num_sys(n, fr, to):
    suma, i = 0, 1
    while(n>0):
        k = n%to
        suma+=k*i
        i*=fr
        n = n//to
    return suma
def check_num(n, system):
    while(n>0):
        k = n%10
        if k >= system: return False
        else: n = n//10;
        return True
def chose(way, n, system):
    if way == "d": print("From decimal to your number system: ", num_sys(n, 10, system))
    elif way == "s": print("From your number system to decimal system: ", num_sys(n, system, 10))
    else: print("Wrong letter. ")
        
system=int(input("Choose number system by base (from 2 to 9): "))
way=input("Choose: 10-base system to your_system-base system (d) or your_system-base system to 10-base system (s): ")
n=int(input("Enter your number: "))
if(check_num(n, system)==True): chose(way, n, system)
else: print("Wrong number")