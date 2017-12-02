import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from matplotlib.ticker import MaxNLocator #do barchart
from matplotlib.ticker import FuncFormatter
from collections import namedtuple #do barchart

"""t=np.arange(0., 5., 0.1)
def f(t):
    return np.cos(t*np.pi*2)"""

#fig = plt.figure and then ax = fig.add_subplot(111)
"""fig, ax=plt.subplots()
ax.plot(t, f(t))
ax.set(xlabel="os ox", title="tytul")
ax.grid()
ax.plot(t, t**2)
ax.set(title="tytul2")
ax.grid()
plt.show()"""

# kropki
"""x1=np.linspace(0.,5.)
print(x1)
x2=np.linspace(0., 2.)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)
plt.subplot(211)
plt.plot(x1,y1,'o-')
plt.title('tytul')
plt.subplot(212)
plt.plot(x2,y2,'.-')
plt.show()"""

#histogram z linią regresji
"""np.random.seed(2000)
mu, sigma = 100, 15
x=mu+sigma*np.random.randn(1000)
num_bins=50
fig, ax=plt.subplots()
n, bins, patches=ax.hist(x, num_bins, normed=1)
ax.text(70, .025, r'$\mu=100, \sigma=15$')
#dodanie linii
y=mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('wystepowanie')
ax.set_title('histogram z linią regresji')
#tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()"""


#rysowanie barchart
"""def f(t):
    return t+2
def g(t):
    return t-2
def h(t):
    return t
def get_f(t):
    return f(t), g(t), h(t)
fig, ax = plt.subplots()
ind=np.arange(1,4)
#plt.show(block=False) #pokaz figure, nie block
a,b,c=plt.bar(ind, get_f(4))
a.set_facecolor('r')
b.set_facecolor('g')
c.set_facecolor('b')
ax.set_xticks(ind)
ax.set_xticklabels(['a','b','c'])
ax.set_ylabel('wynik')
ax.set_title('barchart')
ax.legend()
plt.show() """




"""names=['a','b','c']
values=[6,5,8]
plt.figure(1, figsize=(9,3)) #bo będą trzy koło siebie wykresy
plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values) #kropki
plt.subplot(133)
plt.plot(names, values) #polaczenie kreskowe
plt.suptitle('Wykresy')
plt.show()"""

obj=('python', 'c++', 'java')
np.random.seed(191991)
print(np.random.randn(1))
x=np.random.randn(1)+100
y=np.random.randn(1)+100
z=np.random.randn(1)+100
per=[x,y,z]
y_pos = np.arange(len(obj))
plt.bar(y_pos, per, alpha=0.5) #alpha - przezroczystosc koloru
plt.xticks(y_pos, obj) #(pozycja, napis)
plt.ylabel('Uzytkownikow')
plt.title('Języki programowania')
plt.show()

"""n_groups=5 #ilosc grup, w każdej men i women
means_men=(20, 35, 30, 35, 27)
std_men=(2,3,4,1,2)
means_women=(25,32,34,20,25)
std_women=(3,5,2,3,3)

fig, ax=plt.subplots()
index=np.arange(n_groups) #0,1,2,3,4 (do n-1)
bar_width=0.35
opacity=0.4 #nieprzeźroczystość
error_config = {'ecolor': '0.3'}
#bar(x, height, width, bottom, *, align='center', **kwargs)"""
