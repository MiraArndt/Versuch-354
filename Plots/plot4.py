import matplotlib.pyplot as plt
import numpy as np
import csv

x = np.genfromtxt('frequenz2.csv',delimiter=',',unpack=True,usecols=0)*2*np.pi
y = np.genfromtxt('frequenz2.csv',delimiter=',',unpack=True,usecols=1)
z = np.genfromtxt('frequenz2.csv',delimiter=',',unpack=True,usecols=2)
p=y/z*2*np.pi
x1 = ["%.0f" % elem for elem in x]

prund=["%.2f" % elem for elem in p]
with open("tabelle1.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(x1,y,z,prund))


a=np.linspace(x[0],x[22],50)
plt.plot(x, p,'x', label='Messwerte')
#plt.plot(a,np.abs(np.arctan(-a*871*5*10**(-9)/(1-(3.5*10**(-3)*5*10**(-9)*a**2)))))
plt.xlabel(r'$\omega \:/\: \si{\kilo\hertz}$')
plt.ylabel(r'$\phi$')
plt.xscale('log')
plt.yticks([0,np.pi/8,np.pi/4,np.pi*3/8,np.pi/2,np.pi*5/8,np.pi*3/4,np.pi*7/8,np.pi],[r'$0$',r'$\frac{1}{4}\pi$',r'$\frac{3}{8}\pi$',r'$\frac{1}{2}\pi$',r'$\frac{5}{8}\pi$',r'$\frac{3}{4}\pi$',r'$\frac{7}{8}\pi$',r'$\pi$'])
plt.legend(loc='best')


plt.savefig('build/plot4.pdf')


