# -*- coding: utf-8 -*-
"""
Created on Fri May 13 23:21:14 2022

@author: vitor.torres
"""
import numpy as np


def intlagv(xinp,xm1,xm2,xm3,ym1,ym2,ym3):  
    # Interpolação quadrática usando o polinómio de Lagrange
    # Dados (input): xinp, (x0,y0), (x1,y1) e (x2,y2) 
    # Resultados (output): xinp, yout 

    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    xi1=xinp-xm1
    xi2=xinp-xm2
    xi3=xinp-xm3
    
    a=xi2*xi3/(xab*xac)
    b=-xi1*xi3/(xab*xbc)
    c=xi1*xi2/(xac*xbc)

    yout=a*ym1+b*ym2+c*ym3
    return xinp, yout    
 
def intlaginvv(yinp,xm1,xm2,xm3,ym1,ym2,ym3):  
    # interpolaçáo inversa usando o polinómio de Lagrange
    # Dados (input): yinp, (x0,y0), (x1,y1) e (x2,y2) 
    # Resultados (output): xout  (e yout) 

    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    am=a+b+c
    bm=a*(xm2+xm3)+b*(xm1+xm3)+c*(xm1+xm2)
    cm=a*xm2*xm3+b*xm1*xm3+c*xm1*xm2-yinp

    xout=(bm+np.sqrt(bm*bm-4*am*cm))/(2*am)
    if xm3 > xm1 and (xout < xm1 or xout > xm3): 
        xout=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)

    if xm1 > xm3 and (xout < xm3 or xout > xm1):
        xout=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)

    xta=xout-xm1
    xtb=xout-xm2
    xtc=xout-xm3
    yout=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xout, yout   


def maxminv(xm1,xm2,xm3,ym1,ym2,ym3):  
    # Máximo ou mínimo usando o polinómio de Lagrange
    # Dados (input): (x0,y0), (x1,y1) e (x2,y2) 
    # Resultados (output): xm, ymax 
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xm=0.5*xmla/(a+b+c)

    xta=xm-xm1
    xtb=xm-xm2
    xtc=xm-xm3

    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xm, ymax