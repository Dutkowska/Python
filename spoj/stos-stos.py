#task: https://pl.spoj.com/problems/STOS/
tab=[]
while True:
    x = input()
    if x == '': break
    else:
        if x == '+':
            if len(tab) < 10:
                tab.insert(0, int(input()))
                print(':)')
            else: print(':(')
        elif x == '-':
            print(tab.pop(0)) if len(tab) != 0 else print(':(')