from functools import reduce

lista=(1,2,3,4)
def f(x):
    return x+5

odw=(6,7,8,9)

def parz(x):
    if x%2==0:
        return True
    else:
        return False
print(list(filter(parz, lista)))
