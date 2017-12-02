Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 19:28:18) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> t=np.arange(0.,2., 0.01)
>>> s=1+np.sin(2*np.pi*t)
>>> # fig = plt.figure and then ax = fig.add_subplot(111)
>>> fig, ax=plt.subplots()
>>> ax.plot(t,s)
[<matplotlib.lines.Line2D object at 0x00D1EFD0>]
>>> ax.set(xlabel='time(s)', ylabel='voltage', title='tytul')
[Text(0,0.5,'voltage'), Text(0.5,0,'time(s)'), Text(0.5,1,'tytul')]
>>> ax.grid()
>>> fig.savegif("test.png")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fig.savegif("test.png")
AttributeError: 'Figure' object has no attribute 'savegif'
>>> plt.show()
>>> import matplotlib.pyplot as plt
>>> x1=np.linspace(0.,5.)
>>> print(x1)
[ 0.          0.10204082  0.20408163  0.30612245  0.40816327  0.51020408
  0.6122449   0.71428571  0.81632653  0.91836735  1.02040816  1.12244898
  1.2244898   1.32653061  1.42857143  1.53061224  1.63265306  1.73469388
  1.83673469  1.93877551  2.04081633  2.14285714  2.24489796  2.34693878
  2.44897959  2.55102041  2.65306122  2.75510204  2.85714286  2.95918367
  3.06122449  3.16326531  3.26530612  3.36734694  3.46938776  3.57142857
  3.67346939  3.7755102   3.87755102  3.97959184  4.08163265  4.18367347
  4.28571429  4.3877551   4.48979592  4.59183673  4.69387755  4.79591837
  4.89795918  5.        ]
>>> x2=np.linspace(0.,2.)
>>> x2
array([ 0.        ,  0.04081633,  0.08163265,  0.12244898,  0.16326531,
        0.20408163,  0.24489796,  0.28571429,  0.32653061,  0.36734694,
        0.40816327,  0.44897959,  0.48979592,  0.53061224,  0.57142857,
        0.6122449 ,  0.65306122,  0.69387755,  0.73469388,  0.7755102 ,
        0.81632653,  0.85714286,  0.89795918,  0.93877551,  0.97959184,
        1.02040816,  1.06122449,  1.10204082,  1.14285714,  1.18367347,
        1.2244898 ,  1.26530612,  1.30612245,  1.34693878,  1.3877551 ,
        1.42857143,  1.46938776,  1.51020408,  1.55102041,  1.59183673,
        1.63265306,  1.67346939,  1.71428571,  1.75510204,  1.79591837,
        1.83673469,  1.87755102,  1.91836735,  1.95918367,  2.        ])
>>> y1=np.cos(2*np.pi*x1)*np.exp(-x1)
>>> y2=np.cos(2*np.pi*x2)
>>> 
>>> plt.sublop(2,1,1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    plt.sublop(2,1,1)
AttributeError: 'module' object has no attribute 'sublop'
>>> plt.subplot(2,1,1)
<matplotlib.axes._subplots.AxesSubplot object at 0x00CD32B0>
>>> plt.plot(x1,y1,'o-')
[<matplotlib.lines.Line2D object at 0x00CFAFD0>]
>>> plt.title('A tale of 2 subplots')
Text(0.5,1,'A tale of 2 subplots')
>>> plt.subplot(2,1,2)
<matplotlib.axes._subplots.AxesSubplot object at 0x00CFA7F0>
>>> plt.plot(x2,y2,'.-')
[<matplotlib.lines.Line2D object at 0x011662B0>]
>>> plt.show()
>>> import matplotlib.pyplot as plt
>>> import matplotlib.mlab as mlab
>>> np.random.seed(2000)
>>> mu, sigma = 100, 15
>>> x=mu+sigma*np.random.randn(1000)
>>> num_bins=50
>>> fig, ax=plt.subplots()
>>> n, bins, patches=ax.hist(x, num_bins, normed=1)
>>> #dodanie linii
>>> y=mlab.normpdf(bins, mu, sigma)
>>> ax.plot(bins, y, '--')
[<matplotlib.lines.Line2D object at 0x0119A5B0>]
>>> ax.set_xlabel('Smarts')
Text(0.5,0,'Smarts')
>>> ax.set_title(r'Histogram, $\mu=100$, $\sigma=15$')
Text(0.5,1,'Histogram, $\\mu=100$, $\\sigma=15$')
>>> Tweak spacing to prevent clipping of ylabel
SyntaxError: invalid syntax
>>> #Tweak spacing to prevent clipping of ylabel
>>> fig.tight_layout()
>>> plt.show()
>>> plt.show()
>>> 
