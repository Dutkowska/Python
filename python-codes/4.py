Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #wyrażenie lamda - funkcje anonimowe
>>> # lambda argumenty: funkcja
>>> a=lambda x,y: x+y
>>> print a(1,2)
SyntaxError: invalid syntax
>>> print(a(1,2))
3
>>> b=lambda x,y: x*y
>>> print(b(2,3))
6
>>> #funkcja map - wykonuje funkcję dla każdego elementu listy
>>> #map(funkcja, lista)
>>> 
>>> lista=(1,2,3,4)
>>> def funkcja(x):
	return x^2

>>> map(funkcja, lista)
<map object at 0x03E68130>
>>> print(map(funkcja, lista))
<map object at 0x03E68550>
>>> lista=[1,2,3]
>>> print(map(funkcja, lista))
<map object at 0x03E68AB0>
>>> help map
SyntaxError: invalid syntax
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> print(map(x^2, (1,2,3)))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(map(x^2, (1,2,3)))
NameError: name 'x' is not defined
>>> liczby = [1,2,3,4,5]
>>> def dwa(x):
	return x*2

>>> dwa(2)
4
>>> map(dwa, liczby)
<map object at 0x039753F0>
>>> print(map(dwa, liczby))
<map object at 0x03E68130>
>>> map(dwa, *liczby)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    map(dwa, *liczby)
TypeError: 'int' object is not iterable
>>> map(dwa, (1,2,3))
<map object at 0x03E68550>
>>> map(dwa, [1,2,3])
<map object at 0x018D1BD0>
>>> list(map(dwa, liczby))
[2, 4, 6, 8, 10]
>>> for i in map(dwa, liczby)
SyntaxError: invalid syntax
>>> for i in map(dwa, liczby):
	print(i)

	
2
4
6
8
10
>>> 
>>> def ka(x):
	x!
	
SyntaxError: invalid syntax
>>> #mnożenie kartezjańskie
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> print(zip(a,b))
<zip object at 0x035B63C8>
>>> list(print(zip(a,b)))
<zip object at 0x03E592B0>
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list(print(zip(a,b)))
TypeError: 'NoneType' object is not iterable
>>> list(zip(a,b))
[(1, 4), (2, 5), (3, 6)]
>>> for i in zip(a,b):
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> 
>>> for i in zip(a,b):
	print(i)

	
(1, 4)
(2, 5)
(3, 6)
>>> a=[2,2,2,2]
>>> def suma(x,y):
	return x+y

>>> print(reduce(suma,a))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(reduce(suma,a))
NameError: name 'reduce' is not defined
>>> list(reduce(suma,a))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    list(reduce(suma,a))
NameError: name 'reduce' is not defined
>>> from functools import reduce
>>> list(reduce(suma,a))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    list(reduce(suma,a))
TypeError: 'int' object is not iterable
>>> reduce(suma,a)
8
>>> liczby
[1, 2, 3, 4, 5]
>>> def parzyste(x):
	if x%2==0:
		return True
	else:
		return False

	
>>> print(filter(parzyste,liczby))
<filter object at 0x03E8B050>
>>> list(filter(patrzyste,liczby))
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    list(filter(patrzyste,liczby))
NameError: name 'patrzyste' is not defined
>>> list(filter(parzyste,liczby))
[2, 4]
>>> eval('2+2')
4
>>> class product:
	ilosc=0
	def ustaw_ilosc(self,ilosc)
	
SyntaxError: invalid syntax
>>> class produkt:
	ilosc=0
	def ustaw_ilosc(self,ilosc):
		self.ilosc=ilosc

		
>>> class pomidor(produkt)
SyntaxError: invalid syntax
>>> class pomidor(produkt):
	opis="swieze pomidory"

	
>>> p=pomidor()
>>> p.ustaw_ilosc(10)
>>> p.ilosc
10
>>> p.opis
'swieze pomidory'
>>> #dziedziczenie klas
>>> class produkt:
	ilosc=0
	def __init__(self):
		self.ilosc=111
	def ustaw_ilosc(self, ilosc):
		self.ilosc=ilosc

		
>>> class pomidor(produkt):
	def __init__(self):
		produkt.__init__(self)
	opis='swieze pomidory'

	
>>> p=pomidor()
>>> p.ilosc
111
>>> p.opis
'swieze pomidory'
>>> issubclass(pomidor, produkt)
True
>>> #jest podklasą
>>> isinstance(ilosc,pomidor)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    isinstance(ilosc,pomidor)
NameError: name 'ilosc' is not defined
>>> isinstance(ilosc,produkt)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    isinstance(ilosc,produkt)
NameError: name 'ilosc' is not defined
>>> 
