import matplotlib.pyplot as plt
import numpy as np

x = np.genfromtxt('frequenz1.csv',delimiter=',',unpack=True,usecols=0)
y = np.genfromtxt('frequenz1.csv',delimiter=',',unpack=True,usecols=1)


plt.plot(x[7:17]*2*np.pi, y[7:17]/2.3, 'x',label='Messwerte')
plt.ylabel(r'$\frac{U_C}{U_0}$')
plt.xlabel(r'$\omega \:/\: \si{\kilo\hertz}$')
plt.legend(loc='best')



plt.savefig('build/plot3.pdf')
