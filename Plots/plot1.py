import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
from uncertainties import ufloat

x = (np.genfromtxt('daempfung.csv',delimiter=',',unpack=True,usecols=0))*10**(-9)
y = np.genfromtxt('daempfung.csv',delimiter=',',unpack=True,usecols=1)


params,covariance_matrix = np.polyfit(x,np.log(y),deg=1,cov=True)
x_plot= np.linspace(0,300*10**(-9),2000)
uncertainties= np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:.5f} ± {uncertainty:.5f}')
a=ufloat(params[0],uncertainties[0])
print(1/a)
print(1/a*10**(-9))
#print(a*10**(-9))
r=ufloat(871.6,0.2)
l=ufloat(0.0035,0.00001)
c=ufloat(0.000000005,0.00000000002)


#print(2*l*a)
#print((1/(l*c)-r**2/(2*l**2))**0.5)
#print('Omega1=',r/(2*l)+(r**2/(4*l**2)+1/(l*c))**0.5)
#print('Omega2=',-r/(2*l)+(r**2/(4*l**2)+1/(l*c))**0.5)
#print(1/r*(l/c)**0.5)
#print((4*l**2/(l*c))**0.5)
#print(2*l/np.abs(a))
plt.plot(x,(y), 'x',label='Messwerte')
plt.plot(x_plot,np.exp(params[0]*x_plot)*4,label='Ausgleichskurve')
plt.plot(x_plot,np.exp(-38800*x_plot)*4,label='Theoriekurve')
#plt.plot(96.9,1/np.exp(1),'k',label='wert')

plt.xlabel(r'$t \:/\: \si{\micro\second}$')
plt.ylabel(r'$U_{C,0} \:/\: \si{\volt}$')
plt.xticks([0, 50*10**(-9), 100*10**(-9), 150*10**(-9), 200*10**(-9), 250*10**(-9),300*10**(-9)],
           [r"$0$", r"$50$", r"$100$", r"$150$", r"$200$", r"$250$", r"$300$"])
plt.legend(loc='best')

plt.savefig('build/plot1.pdf')
