import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
n=np.random.seed(2000)
y=np.random.randn(1000)
y=y[(y>0)&(y<1)]
y.sort()

mu, sigma=100, 15
x=mu+sigma*y
fig, ax=plt.subplots()
n, bins, patches = ax.hist(x, 50, normed=1)
ax.text(102, 14, '$\mu=100, \sigma = 15$', color='r')
y=mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
fig.tight_layout()
print(y)
plt.show()

