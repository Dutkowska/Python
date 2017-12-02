Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> a=2
>>> b=1
>>> if a>b:
	print a
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
>>> if a>b:
	print(a)
else:
	print(b)

	
2

>>> c=2
>>> if a==c:
	print("%s, %f" % ("Liczba jest rowna: ", a))
	else:
		
SyntaxError: invalid syntax
>>> if a==c:
	print("%s, %f" % ("Liczba jest rowna: ", a))

	
Liczba jest rowna: , 2.000000
>>> print("równa")
równa
>>> d=[1,2,3,4]
>>> e=[5,6,7,8]
>>> d.extend(e)
>>> d
[1, 2, 3, 4, 5, 6, 7, 8]
>>> d.pop([7])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d.pop([7])
TypeError: 'list' object cannot be interpreted as an integer
>>> d.pop(7)
8
>>> d
[1, 2, 3, 4, 5, 6, 7]
>>> s.remove(2)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.remove(2)
NameError: name 's' is not defined
>>> d.remove(2)
>>> d
[1, 3, 4, 5, 6, 7]
>>> d[1]=2
>>> d
[1, 2, 4, 5, 6, 7]
>>> text=[ala,beata,cecylia,dalia]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    text=[ala,beata,cecylia,dalia]
NameError: name 'ala' is not defined
>>> text=["ala","beata","Cecylia","Dalia"]
>>> text.capitalize()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    text.capitalize()
AttributeError: 'list' object has no attribute 'capitalize'
>>> text
['ala', 'beata', 'Cecylia', 'Dalia']
>>> text.capitalize
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    text.capitalize
AttributeError: 'list' object has no attribute 'capitalize'
>>> licznik=10
>>> wartosc=15
>>> while licznik <= wartosc
SyntaxError: invalid syntax
>>> while licznik <= wartosc:
	licznik += 1
	print(licznik)

	
11
12
13
14
15
16
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(3, 5):
	print(i)

	
3
4
>>> for i in range(0,10,2):
	print(i)

	
0
2
4
6
8
>>> napis = "abcd"
>>> for i in napis:
	print(i)

	
a
b
c
d
>>> bar = {"imie" : "jurek", "nazwisko" : "lepper"}
print bar["imie"]
SyntaxError: multiple statements found while compiling a single statement
>>> bar = {"imie" : "jurek", "nazwisko" : "lepper"}
>>> print(bar["imie"])
jurek
>>> ja = {"imie": "Paula", "nazwisko":"Dutkowska"}
>>> print(ja["imie"])
Paula
>>> for i in ja:
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> 
>>> for i in ja:
	print(i)

	
imie
nazwisko
>>> for i in ja:
	print(i+" - "+ja[i])

	
imie - Paula
nazwisko - Dutkowska
>>> ja.keys()
dict_keys(['imie', 'nazwisko'])
>>> del ja["imie"]
>>> ja.keys()
dict_keys(['nazwisko'])
>>> print ja
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(ja)?
>>> print ja["imie"]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(ja["imie"])?
>>> print ja.get("imie", "brak klucza")
SyntaxError: invalid syntax
>>> print(ja["imie"])
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(ja["imie"])
KeyError: 'imie'
>>> print(ja.get("imie","Brak klucza"))
Brak klucza
>>> def funkcja(arg1, arg2):
	arg3=arg1+" - " + arg2
	return arg3

>>> print(funkcja(1,2))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(funkcja(1,2))
  File "<pyshell#82>", line 2, in funkcja
    arg3=arg1+" - " + arg2
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(funkcja("a","b"))
a - b
>>> def funkcjaa(arg1, arg2="b"):
	global globalna
	arg3=arg1 + " - " + arg2
	globalna = "globalna"
	return arg3

>>> print(funkcja("a"))
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    print(funkcja("a"))
TypeError: funkcja() missing 1 required positional argument: 'arg2'
>>> print(globalna)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    print(globalna)
NameError: name 'globalna' is not defined
>>> print(funkcjaa("a"))
a - b
>>> globalna
'globalna'
>>> class koszyk:
	def __init__ (self):
		self.koszyk = []
	def dodaj(self,obiekt):
		self.koszyk.append(obiekt)
	def rozmiar(self):
		return len(self.koszyk)

	
>>> klasa = koszyk()
>>> klasa.dodaj("pierwszy")
>>> klasa.dodaj("drugi")
>>> print(klasa.rozmiar())
2
>>> print(klasa)
<__main__.koszyk object at 0x03828D50>
>>> print(klasa.koszyk())
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    print(klasa.koszyk())
TypeError: 'list' object is not callable
>>> print(klasa.koszyk)
['pierwszy', 'drugi']
>>> 
