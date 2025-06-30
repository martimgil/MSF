import numpy as np
from matplotlib import pyplot as plt

global g,vt

g=9.8
tf=4
dt=0.5
n=int(tf/dt)
t=np.linspace(0,tf,n+1)

vt=6.8 #Apesar de não ser dada no enunciado considerei ser 6.8m/s

v0=0 #velocidade inicial
x0=2 #posiçao inicial


def acel(t,x,v):
    return g-g/vt**2*np.abs(v)*v


def rk4_1D(t,x0,v0,dt,n):
    #Método de Runge-Kutta de 4ª ordem que retorna a posição e a velocidade
    x=np.empty(n+1)
    x[0]=x0
    v=np.empty(n+1)
    v[0]=v0
    for i in range(n):
        ax1=acel(t[i],x[i],v[i])
        c1v=ax1*dt
        c1x=v[i]*dt
        
        ax2=acel(t[i]+dt/2,x[i]+c1x/2,v[i]+c1v/2)
        c2v=ax2*dt
        c2x=(v[i]+c1v/2)*dt
        
        ax3=acel(t[i]+dt/2,x[i]+c2x/2,v[i]+c2v/2)
        c3v=ax3*dt
        c3x=(v[i]+c2v/2)*dt
        
        ax4=acel(t[i]+dt/2,x[i]+c2x/2,v[i]+c2v/2)
        c4v=ax4*dt
        c4x=(v[i]+c3v)*dt
        
        x[i+1]=x[i]+(c1x+2*c2x+2*c3x+c4x)/6
        v[i+1]=v[i]+(c1v+2*c2v+2*c3v+c4v)/6
    return x,v

def euler(t,x0,v0,dt,n):
    x=np.empty(n+1)
    x[0]=x0
    v=np.empty(n+1)
    v[0]=v0
    for i in range(n):
        a=acel(t[i],x[i],v[i])
        v[i+1]=v[i]+a*dt
        x[i+1]=x[i]+v[i]*dt
    return x,v

x_rk=rk4_1D(t,x0,v0,dt,n)[0]

plt.plot(t,x_rk,label="Runge-Kutta")
plt.legend()

plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid()
plt.plot()
plt.show()