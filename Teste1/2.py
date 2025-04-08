#124833 - Martim Lopes Gil 
import numpy as np
import matplotlib.pyplot as plt

#Considerei a altura inicial igual a 30 e a posição do liquido em 0

#a) 

t0 = 0
tf = 2.5
x0 = 30
v0 = 0
dt = 0.001
m = 0.05

g = 9.8

t = np.arange(t0,tf,dt)
v = np.empty(np.size(t))
x = np.empty(np.size(t))


#a)
v[0]=v0
x[0] = x0

for i in range(np.size(t)-1):
    v[i+1] = v[i] - g*dt
    x[i+1] = x[i] + v[i]*dt

plt.plot(t,x)
plt.title("Gráfico da posição em função do tempo")
plt.xlabel("Tempo(s)")
plt.ylabel("Posição(cm)")
plt.show()
plt.plot(t,v)
plt.title("Gráfico da velocidade em função do tempo")
plt.xlabel("Tempo(s)")
plt.ylabel("Velocidade(cm/s)")
plt.show()

#b)
izero = np.size(x) - np.size(x[x<0])
tzero = t[izero]
vzero = v[izero]



print("b) A velocidade final atingida no liquido é {:.2f} m/s".format(vzero))
print("O tempo até atingir o liquido é de {:.2f}s".format(tzero))
print("Como se pode verificar o valor obtido para o tempo é extremamente semelhante ao obtido na constante C. Desse modo conclui-se que a constante C se encontra relacionada com o tempo de queda da bola.")

