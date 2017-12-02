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

"""obj=('python', 'c++', 'java')
per=[10, 8, 6]
y_pos = np.arange(len(obj))
plt.bar(y_pos, per, alpha=0.5) #alpha - przezroczystosc koloru
plt.xticks(y_pos, obj) #(pozycja, napis)
plt.ylabel('Uzytkownikow')
plt.title('Języki programowania')
plt.show()"""

#odwrotny barchart (horizontal): PLT.BARH i YTICKS
"""obj=('A','B','C')
il=(5,6,3)
y_pos=np.arange(len(obj))
plt.barh(y_pos, il, alpha=0.5, align='center')
plt.yticks(y_pos, obj)
plt.show()"""

#porównujące bary
"""a=(90, 57, 67, 92)
b=(87, 67, 91, 84)
ind=np.arange(len(a))
fig, ax=plt.subplots()
bar_width=0.35
opacity=0.8
rects1=plt.bar(ind, a, bar_width, alpha=0.8, facecolor='b', label='Arek')
rects2=plt.bar(ind+bar_width, b, bar_width, alpha=0.8, facecolor='g', label='Bartek')

plt.xlabel('Osoba')
plt.ylabel('pkty')
plt.title('porównanie')
plt.xticks(ind+0.5*bar_width, ('A','B','C','D'))
plt.legend()
plt.tight_layout()
plt.show()"""

"""m=(20,35, 30, 32, 27)
ms=(2,3,4,1,2)
k=(22, 33, 31, 29, 28)
ks=(3,5,2,3,3)
ind=np.arange(len(m))
bar_w=0.35
fig, ax=plt.subplots()
#rects1=ax.barh(ind, m, bar_w, alpha=0.4, facecolor='b', yerr=ms, label="Facet")
rects1=ax.barh(ind, m, bar_w, alpha=0.4, facecolor='b', label="Facet")
rects2=ax.barh(ind+bar_w, k, bar_w, alpha=0.4, facecolor='r', label="Kobieta")
#plt.xlabel('Płeć')
ax.set_ylabel('Klasa')
#plt.ylabel('Wystapienia w klasie')
ax.set_xlabel('Wystapienia w klasie')
#plt.xticks(ind+0.5*bar_w, ('A', 'B', 'C', 'D', 'E'))
ax.set_yticks(ind+0.5*bar_w)
ax.set_yticklabels(('A', 'B', 'C', 'D', 'E'))
ax.legend()
fig.tight_layout()
plt.show()"""


#naklejany bar od płci (BOTTOM=M)
"""m=(20,35, 30, 32, 27)
ms=(2,3,4,1,2)
k=(22, 33, 31, 29, 28)
ks=(3,5,2,3,3)
ind=np.arange(len(m))
bar_w=0.35
p1=plt.bar(ind, m, bar_w, alpha=0.4, facecolor='b', yerr=ms, label='Facet')
p2=plt.bar(ind, k, bar_w, bottom=m, facecolor='r', alpha=0.4, yerr=ks, label='Kobieta')
plt.ylabel('Wystapienia')
plt.xlabel('Klasa')
plt.xticks(ind, ('A', 'B', 'C', 'D', 'E'))
plt.yticks(np.arange(0, 75, 15))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
plt.show()"""

#pie chart przeliczy mi sa procenty
labels='zaby', 'koty', 'psy', 'chomiki'
#sizes=[15,30,45,10]
sizes=[215, 130, 202, 150]
explode=(0,0,0.2,0) #explode trzeci
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
fig1, ax1=plt.subplots()
#autopct napisze procenty na wykresie
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
ax1.legend()
plt.show()

