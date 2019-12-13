import matplotlib.pyplot as plt
import numpy as np

x = np.genfromtxt('daempfung.csv',delimiter=',',unpack=True,usecols=0)
y = np.genfromtxt('daempfung.csv',delimiter=',',unpack=True,usecols=1)


plt.plot(x, y, label='Kurve')
plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
plt.legend(loc='best')



plt.savefig('build/plot4.pdf')
