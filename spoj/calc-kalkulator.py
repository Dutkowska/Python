def switcher(x):
    return{
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b,
        '%': a%b
    }[x]

tab=[]
while True:
    tab=input().split()
    sign=tab[0]
    a, b=int(tab[1]), int(tab[2])
    print(switcher(sign))
    if tab=="":
        break