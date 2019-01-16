#check if num is a sum of two numbers, reverse of each other:
reverse=lambda a: int(str(a)[::-1])
def reversesum(x):
    for i in range(1, x//2 +1):
        if i+reverse(i)==x:
            print(i,reverse(i))
            return True
    return False

print(reversesum(22))