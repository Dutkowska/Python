#task: https://pl.spoj.com/problems/CALC2/
def switcher(x, a, b):
    return{
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': int(a/b),
        '%': a%b
    }[x]

calc=[0]*10
while True:
    tab = input().split()
    if tab == "": break
    sign, a, b = tab[0], int(tab[1]), int(tab[2])
    if sign == 'z': calc[a]=b
    else: print(switcher(sign, calc[a], calc[b]))