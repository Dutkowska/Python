Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=1
>>> def test(x=a)
SyntaxError: invalid syntax
>>> def test(x=a):
	return x

>>> a=2
>>> print(test())
1
>>> aa=[1]
>>> def testt(x=aa):
	return x

>>> aa.append(2)
>>> print(test())
1
>>> print(testt())
[1, 2]
>>> #Jeżeli nazwa ostatniego parametru funkcji zaczyna się od gwiazdki to funkcja może przyjmować dowolną liczbę argumentów:
>>> def test(*args):
	return args

>>> print(test("a", "b", 1, 2, 3))
('a', 'b', 1, 2, 3)
>>> #**args - przechwyci on wszystkie nie pasujące argumenty hasłowe
>>> def dod():
	return "abc"

>>> test.a = 1
>>> dod.a=1
>>> dod.lol="omg"
>>> print(dod())
abc
>>> print(dod._dict_)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(dod._dict_)
AttributeError: 'function' object has no attribute '_dict_'
>>> print(dod.__dict__)
{'a': 1, 'lol': 'omg'}
>>> #dodatkowe atrybuty wyrzuciłam
>>> 
