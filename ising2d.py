# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 11:05:03 2018

@author: Nicco
"""

import numpy as np
import matplotlib.pyplot as plt


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

#conf=np.ones([L,N])
T=1000000

 
plt.figure(1) 
plt.grid()
plt.title("Magnetization (34 sites)")
plt.xlabel("MC step")
plt.ylabel("Magnetization")

for L in [10, 20, 30]:
    N=L
    beta=np.linspace(0.1,0.8,9)
    binder=np.zeros(9)

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
        plt.plot(range(T),magn, label=beta[j])
        cut=20000
        #binder[j]=(sum(magn[cut:]**4)/((sum(magn[cut:]**2))**2))*(T-cut)

#    plt.plot(beta,binder)

#plt.legend(loc='upper right')
plt.savefig("magnetmetropolis.pdf")
