from functools import reduce

lista=(1,2,3,4)
"""def fun(x):
    return x+5"""

"""print(list(map(fun, lista)))

for i in map(fun, lista):
    print(i)

odw=(9,8,7,6)
print(list(zip(lista,odw)))

print(list(zip(lista, list(map(fun, lista)))))"""

#bierze kolejne elementy listy i wrzuca rekurencyjnie do funkcji:
"""def suma(x,y):
    return x+y
print(reduce(suma, lista))"""

"""def silnia(x,y):
    return(x*y)
lis=[]
for i in range(1,6):
    lis.append(i)
print(lis)
print(reduce(silnia, lis))"""

"""def parzyste(x):
    if x%2==0:
        return True
    else:
        return False
print(list(filter(parzyste, lista)))"""

"""class produkt:
    ilosc=0
    def ustaw_ilosc(self, ilosc):
        self.ilosc=ilosc
class pomidor(produkt):
    opis="pomidorki"

p=pomidor()
p.ustaw_ilosc(10)
print(p.ilosc)"""

"""#dziedziczenie klas
class product:
    ilosc=0
    def __init__(self):
        self.ilosc=10
    def ustaw_ilosc(self, ilosc):
        self.ilosc=ilosc

class pomidor(product):
    def __init__(self):
        product.__init__(self)
p=pomidor()
print(p.ilosc)
print("Czy pomidor podklasą produktu?")
print(issubclass(pomidor, product))"""

path = '/Users/Paula/Documents/python/plik.txt'
#plik = open(path, 'r+')
#plik.write('123 \n')
plik=open(path, 'r')
for line in plik:
    print(line)
#print(plik.read())
plik.close()
