t=int(input())
for i in range(t):
    tab=[int(x) for x in list(input())]
    suma=tab[0]*1 + tab[1]*3 + tab[2]*7 + tab[3]*9 + tab[4]*1 +tab[5]*3 + tab[6]*7 + tab[7]*9 + tab[8]*1 + tab[9]*3 + tab[10]*1;
    if suma>0:
        if(suma%10 ==0): print('D')
        else: print('N')
    else: print('N')