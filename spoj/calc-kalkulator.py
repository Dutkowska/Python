def switcher(x):
    return{
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b,
        '%': a%b
    }[x]

while True:
    tab=input().split()
    if tab=="": break
    sign, a, b = tab[0], int(tab[1]), int(tab[2])
    print(switcher(sign))