import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
from uncertainties import ufloat

x = (np.genfromtxt('daempfung.csv',delimiter=',',unpack=True,usecols=0))
y = np.genfromtxt('daempfung.csv',delimiter=',',unpack=True,usecols=1)


params,covariance_matrix = np.polyfit(x,np.log(y),deg=1,cov=True)
x_plot= np.linspace(0,300,2000)
uncertainties= np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:.5f} ± {uncertainty:.5f}')
a=ufloat(params[0],uncertainties[0])
print(1/a)

plt.plot(x,(y), 'x',label='Messwerte')
plt.plot(x_plot,np.exp(params[0]*x_plot)*4,label='Ausgleichskurve')

plt.plot(96.9,4*1/np.exp(1),'rx',label='Wert')

plt.xlabel(r'$t \:/\: \si{\micro\second}$')
plt.ylabel(r'$U_{C,0} \:/\: \si{\volt}$')
plt.legend(loc='best')

plt.savefig('build/plot1.pdf')
