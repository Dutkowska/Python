x=int(input())
for i in range(x, x-100, -1):
    if i%3 == 0 and i%5 == 0: print('SPOKOKOKO')
    elif i%3 == 0: print('KOKO')
    elif i%5 == 0: print('SPOKO')
    else: print(i)