import numpy as np
import matplotlib.pyplot as plt

m=75
u = 0.005  
C_res = 0.8  
A = 0.3
rho_ar = 1.225  
g = 9.80  
p =  250
v0 = 2
x0 = 0

# Forças constantes
F_rol = -u * m * g  # resistência ao rolamento

def acceleration(v, p):
    if v == 0:
        F_ciclista = 0
    else:
        F_ciclista = p / v
    F_res = -0.5 * C_res * A * rho_ar * abs(v) * v
    F_total = F_ciclista + F_rol + F_res
    return F_total / m

def simulate(p, v0, x0):
    dt = 0.001
    t_max = 500
    steps = int(t_max / dt)

    time = np.zeros(steps)
    x = np.zeros(steps)
    v = np.zeros(steps)
    a = np.zeros(steps)

    time[0] = 0
    x[0] = x0
    v[0] = v0

    for i in range(1, steps):
        time[i] = time[i-1] + dt
        a[i-1] = acceleration(v[i-1], p)
        v[i] = v[i-1] + a[i-1] * dt
        x[i] = x[i-1] + v[i-1] * dt
        vT = v[i-1] + a[i-1] * dt

        if x[i] >= 3000:
            break

    time = time[:i+1]
    x = x[:i+1]
    v = v[:i+1]
    a = a[:i]



    t_3km = time[-1]
    

    print(f"Tempo para percorrer 3 km: {t_3km:.2f} s")
    print(f"A sua velocidade terminal é: {vT:.2f} m/s")
    

    
    return time, x,v, t_3km




t, x,v, t_3km= simulate(p, v0, x0)
plt.plot(t, x)
plt.title('Posição vs Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid()
plt.show()

#Calcular o trabalho feito pela força de resistencia do ar
def f_res(x):
    return -0.5 * C_res * A * rho_ar * abs(v) * v


I_exato = 1

def trapz(n):
    b = 3000
    a = 0
    x = np.linspace(a, b, n+1)
    h = (b-a)/n
    dx = (b-a)/n
    y = f_res(x)
    return dx*(np.sum(y)-(y[0]+y[-1])/2)


print("O trabalho feito pela resistencia do ar até o ciclista atingir os 3km é {:.2f} J".format(trapz(276)))