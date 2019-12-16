import matplotlib.pyplot as plt
import numpy as np

x = np.genfromtxt('frequenz2.csv',delimiter=',',unpack=True,usecols=0)
y = np.genfromtxt('frequenz2.csv',delimiter=',',unpack=True,usecols=1)
z = np.genfromtxt('frequenz2.csv',delimiter=',',unpack=True,usecols=2)
w=(y/z)*2*np.pi
a=np.linspace(180,300,50)
b=[np.pi/4]*50
c=[np.pi/2]*50
d=[np.pi*3/4]*50
plt.plot(x[7:20]*2*np.pi, w[7:20],'x', label='Messwerte')

plt.xlabel(r'$\omega \:/\: \si{\kilo\hertz}$')
plt.ylabel(r'$\phi$')
plt.grid()
plt.yticks([np.pi/8,np.pi/4,np.pi*3/8,np.pi/2,np.pi*5/8,np.pi*3/4],[r'$\frac{1}{8}\pi$',r'$\frac{1}{4}\pi$',r'$\frac{3}{8}\pi$',r'$\frac{1}{2}\pi$',r'$\frac{5}{8}\pi$',r'$\frac{3}{4}\pi$'])
plt.legend(loc='best')



plt.savefig('build/plot5.pdf')
