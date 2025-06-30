import numpy as np  
import matplotlib.pyplot as plt


t0 = 0
tf = 365
dt = 0.001  
v0 = 2.3*np.pi  
x0 = 1
y0 = 0
m = 1
M = 3*m
G = 4 * np.pi**2  

t = np.arange(t0, tf, dt)
N = len(t)

a = np.zeros([np.size(t),2])
x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
Ep = np.zeros(N)
Ec = np.zeros(N)

x[0] = x0
y[0] = 0
vx[0] = 0
vy[0] = v0

for i in range(N-1):
    #Metodo de Euler-Cromer
    r = np.sqrt(x[i]**2 + y[i]**2)
    ax = -G * x[i] / r**3 #aceleração instantanea
    ay = -G * y[i] / r**3
    
    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y[i] + vy[i+1] * dt
    v = np.sqrt(vx[i+1]**2 +vy[i+1]**2)

    Ep[i+1] = -G*m/r
    Ec[i+1] = 0.5*m*v**2

Et = Ec + Ep

plt.figure(figsize=(6,6))
plt.plot(x, y, label="Órbita da Terra", color='b')
plt.scatter(0, 0, color='orange', label="Sol")  
plt.xlabel("Posição em X (AU)")
plt.ylabel("Posição em Y (AU)")
plt.show()
print("Como foi possivel verificar no gráfico, é possivel concluir que a trajetoria segue uma forma de elipse e a orbitra da terra a volta do sol parece ser fechada")


plt.show()
#b)

plt.plot(t, Ep, label = "Energia Potencial", color='b')
plt.plot(t, Ec, label ="Energia Cinética", color = 'b')
plt.plot(t, Et, label="Energia Total", color = 'g')
plt.show()

print("Através da analise do grafico é possivel concluir que a energia total encontra-se constante ao longo do tempo, visto que a energia cinetica e a energia potencial devido a conservação da energia mecanica mantem-se constantes.")