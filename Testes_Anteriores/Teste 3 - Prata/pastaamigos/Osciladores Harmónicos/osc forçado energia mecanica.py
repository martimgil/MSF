# -*- coding: utf-8 -*-
"""
@author: diogul_dumb
"""

import matplotlib.pyplot as plt
import numpy as np

def grafico(x,y,xlabel,ylabel):
    plt.plot(x,y)
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def graficoBarras(ii,lst,xlabel,ylabel):
    plt.figure()
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.bar(ii,np.abs(lst))
    plt.grid(True)
    plt.show()

def maximo(xm1,xm2,xm3,ym1,ym2,ym3):  # máximo pelo polinómio de Lagrange
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3
    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)
    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xmax=0.5*xmla/(a+b+c)
    xta=xmax-xm1
    xtb=xmax-xm2
    xtc=xmax-xm3
    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xmax, ymax
    
def zerosv(xm1,xm2,xm3,ym1,ym2,ym3):  # raiz pelo polinómio de Lagrange
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3
    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)
    am=a+b+c
    bm=a*(xm2+xm3)+b*(xm1+xm3)+c*(xm1+xm2)
    cm=a*xm2*xm3+b*xm1*xm3+c*xm1*xm2
    xzero=(bm+np.sqrt(bm*bm-4*am*cm))/(2*am)
    if xm3 > xm1 and (xzero < xm1 or xzero > xm3): 
        xzero=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)
    if xm1 > xm3 and (xzero < xm3 or xzero > xm1):
        xzero=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)
    xta=xzero-xm1
    xtb=xzero-xm2
    xtc=xzero-xm3
    yzero=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xzero, yzero

def main():
    m=1 
    k=1
    wf=1.0
    fo=7.5
    b=0.05
    tf=300
    ti=0

    dt= 0.0001
    n=int((tf-ti)/dt)
    t=np.linspace(ti,n*dt,n)


    x0=-4.0
    vx0=-2
    #ax0=0
    x_=np.empty(n)
    vx_=np.empty(n)
    ax_=np.empty(n-1)
    energia=np.empty(n-1)
    x_[0]=x0
    vx_[0]=vx0


    for i in range(n-1):
        fext=fo*np.cos(wf*t[i])
        fem=-b*vx_[i]
        fx=-k*x_[i]
        ax_[i]=(fext+fem+fx)/m
        vx_[i+1]=vx_[i]+ax_[i]*dt
        x_[i+1] =x_[i]+vx_[i+1]*dt
        energia[i]=0.5*k*x_[i]**2+ 0.5*m*vx_[i]**2  #Em = U +Ec   U = 0.5kx^2   Ec = 0.5mv^2
        

    grafico(t[:-1],energia, "t(s)", "Energia mecânica (J)")
main()
print("Não conserva a energia mecânica")