Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> napis = 'abcdef'
>>> print(napis[0:2])
ab
>>> liczba = 123
>>> print(liczba)
123
>>> print(napis + str(liczba))
abcdef123
>>> print(napis + liczba)
>>> print(napis + str(liczba))
abcdef123
>>> print("%s %d" % (napis, liczba))
abcdef 123
>>> lista = [1, 2, 3, 4, 5, 6]
>>> len(lista)
6
>>> lista.append(liczba)
>>> len(lista)
7
>>> print(lista)
[1, 2, 3, 4, 5, 6, 123]
>>> lista[2]
3
>>> litery = ["A", "B", "C"]
>>> len(litery)
3
>>> print("nana")
nana
>>> print("nana \n nana")
nana 
 nana
>>> print("nana\nnana")
nana
nana
>>> print("nana r'\nanana")
nana r'
anana
>>> t= ('Hello'
    'world')
>>> t
'Helloworld'
>>> wpisz = int(input("Wpisz liczbe: "))
Wpisz liczbe: 2
>>> wpisz
2
>>> l='123456'
>>> l[0]
'1'
>>> l[-1]
'6'
>>> l[1]
'2'
>>> l[:2]
'12'
>>> len(l)
6
>>> lista=l.join('2')
>>> lista
'2'
>>> l
'123456'
>>> l.split()
['123456']
>>> lit="a b c d e f"
>>> lit.split()
['a', 'b', 'c', 'd', 'e', 'f']
>>> len(lit)
11
>>> lit
'a b c d e f'
>>> tab=lit.split()
>>> len(tab)
6
>>> tab[0]
'a'
>>> tab + ['g', 'h']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> tabb = tab + ['g', 'h']
>>> len(tabb)
8
>>> tabb[2]=['c']
>>> tabb
['a', 'b', ['c'], 'd', 'e', 'f', 'g', 'h']
>>> tabb[2]=c
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    tabb[2]=c
NameError: name 'c' is not defined
>>> tabb[2]='c'
>>> tabb
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> tabb[2]='cc'
>>> tabb
['a', 'b', 'cc', 'd', 'e', 'f', 'g', 'h']
>>> len(tabb)
8
>>> tabb[2]=[]
>>> tabb
['a', 'b', [], 'd', 'e', 'f', 'g', 'h']
>>> len(tabb)
8
>>> tabb.insert(0,00)
>>> tabb
[0, 'a', 'b', [], 'd', 'e', 'f', 'g', 'h']
>>> tabb.insert(3,'c')
>>> tabb
[0, 'a', 'b', 'c', [], 'd', 'e', 'f', 'g', 'h']
>>> tabb.clear()
>>> tabb
[]
>>> len(tabb)
0
>>> d=['dzien', 'dobry']
>>> range(5)
range(0, 5)
>>> for i in d:
	print(i, len(i))

	
dzien 5
dobry 5
>>> range(5)
range(0, 5)
>>> for j in range(len(d)):
	print(j, d[j])

	
0 dzien
1 dobry
>>> for j in range(len(d)):
	print(j, d[j], len(d[j]))

	
0 dzien 5
1 dobry 5
>>> for j in range(1, len(d)):
	print(j, d[j])

	
1 dobry
>>> tabb
[]
>>> lista
'2'
>>> li=[1,2,3,4,5]
>>> li
[1, 2, 3, 4, 5]
>>> li[0]=0
>>> li
[0, 2, 3, 4, 5]
>>> li[0]=1
>>> li.insert(0,0)
>>> li
[0, 1, 2, 3, 4, 5]
>>> li.remove(0)
>>> li
[1, 2, 3, 4, 5]
>>> li.index(2)
1
>>> len(li)
5
>>> li
[1, 2, 3, 4, 5]
>>> cz=[2, 3, 2]
>>> li + cz
[1, 2, 3, 4, 5, 2, 3, 2]
>>> li.count(2)
1
>>> licz=li+cz
>>> licz
[1, 2, 3, 4, 5, 2, 3, 2]
>>> licz.count(2)
3
>>> li.reverse()
>>> li
[5, 4, 3, 2, 1]
>>> li.sort()
>>> li
[1, 2, 3, 4, 5]
>>> licz.sort()
>>> licz
[1, 2, 2, 2, 3, 3, 4, 5]
>>> licz.pop()
5
>>> licz
[1, 2, 2, 2, 3, 3, 4]
>>> len(licz)
7
>>> del licz
>>> wp=int(input("Wpisz ilosc: "))
Wpisz ilosc: 1
>>> wp
1
>>> wp=int(input("Wpisz: "))
Wpisz: 6
>>> range(wp)
range(0, 6)
>>> lis=[]
>>> lis
[]
>>> for i in range(wp):
	lis.append(i)

	
>>> 
>>> lis
[0, 1, 2, 3, 4, 5]
>>> lis.clear()
>>> for j in range(wp):
	lis.append(i+1)

	
>>> lis
[6, 6, 6, 6, 6, 6]
>>> lis.clear()
>>> for j in range(wp):
	lis.append(j+1)

	
>>> lis
[1, 2, 3, 4, 5, 6]
>>> len(lis)
6
>>> lis
[1, 2, 3, 4, 5, 6]
>>> len(lis)
6
>>> lis.reverse()
>>> lis
[6, 5, 4, 3, 2, 1]
>>> lis.clear()
>>> lis
[]

>>> range(6)
range(0, 6)

>>> for i in range(6):
	lis.append(len(range(6)) - i)

	
>>> 
>>> lis
[6, 5, 4, 3, 2, 1]
>>> 
