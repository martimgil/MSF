import numpy as np
import matplotlib.pyplot as plt


def maximo(xm1, xm2, xm3, ym1, ym2, ym3):  # máximo pelo polinómio de Lagrange
    xab = xm1-xm2
    xac = xm1-xm3
    xbc = xm2-xm3

    a = ym1/(xab*xac)
    b = -ym2/(xab*xbc)
    c = ym3/(xac*xbc)

    xmla = (b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xmax = 0.5*xmla/(a+b+c)

    xta = xmax-xm1
    xtb = xmax-xm2
    xtc = xmax-xm3

    ymax = a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xmax, ymax


x0 = 1.5
v0 = 0.5
k = 2
m = 0.5
ti = 0
tf = 20
dt = 0.001
n = int((tf-ti)/dt)
alpha = -0.1
beta = 0.02
b = 0.05

t = np.linspace(ti, tf, n+1)

x = np.empty(n+1)
v = np.empty(n+1)
a = np.empty(n+1)
Em = np.empty(n+1)
Ep = np.empty(n+1)
x[0] = x0
v[0] = v0

countMaximos = 0
maxTotal = 0
difTempos = []
maximos = []

for i in range(n):
    força = (-k*x[i]) - ((3*alpha)*(x[i]**2)) + ((4*beta)*(x[i]**3))
    a[i] = força/m

    v[i+1] = v[i] + a[i]*dt

    x[i+1] = x[i] + v[i+1]*dt

    Ep[i] = 0.5*k*(x[i]**2) + alpha*x[i]**3 - beta*x[i]**4

    Em[i] = Ep[i] + 0.5*m*v[i]**2

Ep[n] = 0.5*k*(x[n]**2) + alpha*x[n]**3 - beta*x[n]**4
Em[n] = Ep[n]+0.5*m*v[n]**2


Amp = []
AmpNeg = []

tempos = []
periodos = []
freq = []
freqAngular = []

for i in range(n):
    if (x[i-1] < x[i] > x[i+1] and i > 0):
        Amp.append(x[i])
        tempos.append(t[i])

for i in range(n):
    if (x[i-1] > x[i] < x[i+1] and i > 0):
        AmpNeg.append(x[i])


for i in range(1, len(tempos)-1):
    periodos.append(tempos[i+1]-tempos[i])
    freq.append(1/periodos[i-1])
    freqAngular.append(2*np.pi*freq[i-1])

A = sum(Amp)/(len(Amp))
T = sum(periodos)/(len(periodos))

print("Amplitude+:")
print("{:0.4f},{:0.4f}".format(Amp[0], Amp[-1]))
print("Amplitude-:")
print("{:0.4f},{:0.4f}".format(AmpNeg[0], AmpNeg[-1]))
print("Periodo:")
print("{:0.4f},{:0.4f}".format(periodos[0], periodos[-1]))
print("Frequencia:")
print("{:0.4f},{:0.4f}".format(freq[0], freq[-1]))
print("Frequencia Angular:")
print("{:0.4f},{:0.4f}".format(freqAngular[0], freqAngular[-1]))