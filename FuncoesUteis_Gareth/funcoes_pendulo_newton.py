# -*- coding: utf-8 -*-
'''
Created on Fri APR 30  2025

@author. gareth.baxter
'''
def acc_toque(dx,d):
    # calcular a aceleração de uma esfera devido ao contacto com a esfera à sua direita
    k = 1e7
    q = 2.0
    if dx<d:
        a = (-k*abs(dx-d)**q)/m
    else:
        a = 0.0
    return a

def acc_i(i,x):
    #calcular a aceleração de esfera i, cuja posicao de equilibrio é d*i
    a = 0

    if i>0: # a primeira esfera não tem vizinho à sua esquerda
        a -= acc_toque(x[i] - x[i-1],d)
    if i < (N-1): # a última esfera não tem vizinho à sua direita
        a += acc_toque(x[i+1] - x[i], d)

    # aceleração de gravidade, afeta todas as esferas
    a -= g*(x[i]-d*i)/l
    return a