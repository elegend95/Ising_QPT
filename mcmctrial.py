# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 11:05:03 2018

@author: Nicco
"""

import numpy as np
import matplotlib.pyplot as plt

L=20
N=20
X,Y=np.meshgrid(range(N),range(L))
#beta=0.2
a=beta/N
# =============================================================================
# kappa=a
# gamma=1.2
# gammah=-0.5*np.log(np.tanh(a*gamma))
# 
# =============================================================================
kappa=1
gammah=1

# =============================================================================
# def updatemcmc(c, k, g, sp, ti):
#     x=np.random.randint(0,sp)
#     y=np.random.randint(0,ti)
#     r=np.exp(-2*beta*c[x,y]*(k*(c[(x-1)%L,y]+c[(x+1)%L,y])+g*(c[x,(y-1)%N]+c[x,(y+1)%N]))) #acceptance
#     #r=np.exp(-2*beta*conf[x,y]*(conf[(x-1)%L,y]+conf[(x+1)%L,y]+conf[x,(y-1)%L]+conf[x,(y+1)%L])) 
# 
#     if r>np.random.rand():
#         c[x,y]*=-1
#     return c
# =============================================================================

conf=2*np.random.randint(2, size=(L,N))-1
#conf=np.ones([L,N])
T=100000

binder=np.zeros(12)
beta=np.linspace(0.2,0.6,12)
for j in range(len(beta)):
    conf=2*np.random.randint(2, size=(L,N))-1
    magn=np.zeros(T)
    for i in range(T):
        x=np.random.randint(0,L)
        y=np.random.randint(0,N)
        r=np.exp(-2*beta[j]*conf[x,y]*(kappa*(conf[(x-1)%L,y]+conf[(x+1)%L,y])+gammah*(conf[x,(y-1)%N]+conf[x,(y+1)%N]))) #acceptance
    
        if r>np.random.rand():
            conf[x,y]*=-1
        magn[i]=(float(sum(sum(conf[:,:])))/(L*N))
    cut=20000
    binder[j]=(sum(magn[cut:]**4)/((sum(magn[cut:]**2))**2))*(T-cut)


plt.figure(1)
plt.plot(beta,binder)
