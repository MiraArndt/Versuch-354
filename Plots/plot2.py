import matplotlib.pyplot as plt
import numpy as np
import csv

x = np.genfromtxt('frequenz1.csv',delimiter=',',unpack=True,usecols=0)
y = np.genfromtxt('frequenz1.csv',delimiter=',',unpack=True,usecols=1)
x2=x*2*np.pi
x1=["%.0f" % elem for elem in x2]

with open("tabelle2.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(x1,y))

plt.plot((x)*2*np.pi, (y)/2.3, 'x',label='Messwerte')
plt.xscale('log')


plt.ylabel(r'$\frac{U_C}{U_0}$')
plt.xlabel(r'$\omega \:/\: \si{\kilo\hertz}$')
plt.legend(loc='best')



plt.savefig('build/plot2.pdf')
