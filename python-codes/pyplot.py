import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter

#plt.plot([1,2,3,4], [1,4,9,16])
#plt.axis([0,5,0,20])
"""a=np.arange(9).reshape((3,3)) #macierz 3x3
print(a)
b=np.arange(12).reshape((3,4)) #(wierszy,kolumn)
print(b)"""

t=np.arange(0.,5.,0.1) #np.arange(poczatek, koniec, krok)
"""print(t)
plt.plot(t, t**2, 'r--', linewidth=3.0) #t, t**3, 'g^', kropki -'bo', k-kreska
line,=plt.plot([1,2,3], [1,4,9])
line.set_antialiased(False) """

"""lines=plt.plot([1,2,3],[1,4,9])
plt.setp(lines, linewidth=3.0, color='r')
plt.setp(lines)""" #wyrzuca parametry linii

#grupa wykresów (dwa okna - kolejny figure):
"""def f(t):
	return np.exp(-t) * np.cos(2*np.pi*t)
t1=np.arange(0.,5.,0.1)
plt.figure(1)
plt.subplot(211)
plt.plot(t, f(t), 'r--')
plt.title('pierwszy')
plt.subplot(212)
plt.plot(t1,f(t1), 'k')"""

#losowe zabawy, histogram
"""np.random.seed(2000)
mu, sigma=100, 15
x=mu+sigma*np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='r', alpha=0.8)
plt.text(90, .025, r'$\mu=100,\ \sigma=15$')
#(90, .025) - pozycja początku tekstu na wykresie (x,y)"""

#wstawianie tekstu na wykres
"""s=np.cos(2*np.pi*t)
line,=plt.plot(t,s,lw=2)
plt.annotate('maksimum', xy=(2,1), xytext=(3,1.5), arrowprops=dict(facecolor='green', shrink=0.05),)"""
#plt.ylim=(-2,2)

#zabawa z nieliniowymi wykresami
#zmieniamy skalę osi:
#plt.xscale('log') lub plt.yscale('linear')
#from matplotlib.ticker import NullFormatter
np.random.seed(19864)
y=np.random.normal(loc=0.5, scale=0.4, size=1000)
#print(y)
y=y[(y>0)&(y<1)]
#print(y)
y.sort()
#print(y)
x=np.arange(len(y)) #[0, 1, 2, ...]
plt.figure(1)
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear')
plt.title('lin')
plt.grid('True')
plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')
plt.title('log')
plt.grid('True')
plt.subplot(223)
plt.plot(x,y-y.mean())
#symetr
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)
plt.show()


plt.title("tytuł")
plt.xlabel("Oś OX")
plt.ylabel("Oś OY")
plt.show()
