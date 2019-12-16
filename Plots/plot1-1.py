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


plt.plot((x),np.log(y), 'x',label='Messwerte')
plt.plot(x_plot,params[0]*x_plot+params[1],label='Ausgleichsgerade')

#plt.plot(96.9,4*1/np.exp(1),'rx',label='Wert')

plt.xlabel(r'$t \:/\: \si{\micro\second}$')
plt.ylabel(r'$\ln(U_{C,0})$')
plt.legend(loc='best')

plt.savefig('build/plot1-1.pdf')
