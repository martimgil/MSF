import numpy as np
import matplotlib.pyplot as plt

#Energia Potencial oscilador cúbico

k = 1 #N/m
alpha = 0.05 #N/m^2

x = np.linspace(-8,4,100)

Ep = 0.5*k*(x**2) + alpha*(x**3) # Ep=0.5*k*x^2 + alpha*x^3

plt.xlabel("x (m)")
plt.ylabel("Energia Potencial (J)")
plt.plot(x,Ep)
plt.plot(x,7*np.ones(len(x)),'r--')
plt.grid()
plt.show()

#O corpo de massa 1kg oscila entre as posições em que a EP <=7J. Como a energia potencial não é simétrica à 
#volta da posição de equilíbrio (considerada x=0), o movimento oscilatório tem uma posição média (por período) > 0
#Se a energia total for maior que 8J, o corpo não oscila.