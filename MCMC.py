# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:27:25 2018

@author: Nicco
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation

L=10
T=1000000
X,Y=np.meshgrid(range(L),range(L))
iniz=2*np.random.randint(2, size=(L,L))-1
conf=np.zeros((L,L,T))
conf[:,:,0]=iniz
confee=np.zeros((L,L))
magn=np.zeros(T)


def ham(conf):
    for i in range(L):
        H=0
        H+=-1*conf[i,i]*(conf[(i-1)%L,i]+conf[(i+1)%L,i]+conf[i,(i-1)%L]+conf[i,(i+1)%L])
    return H  

magn[0]=sum(map(sum,conf[:,:,0]))/L**2
for t in range(T-1):
    beta=0.9
    magn[t]=sum(map(sum,conf[:,:,t]))/L**2
    x=np.random.randint(0,L)
    y=np.random.randint(0,L)
    confee[:,:]=conf[:,:,t]
    confee[x,y]*=-1
    r=np.exp(-2*beta*conf[x,y,t]*(conf[(x-1)%L,y,t]+conf[(x+1)%L,y,t]+conf[x,(y-1)%L,t]+conf[x,(y+1)%L,t])) 

    if r>np.random.rand():
        conf[:,:,t+1]=confee[:,:]
    else:
        conf[:,:,t+1]=conf[:,:,t]
    magn[t+1]=sum(map(sum,conf[:,:,t+1]))/L**2

plt.figure(1)
plt.pcolormesh(X, Y, conf[:,:,t], cmap=plt.cm.RdBu);
plt.title('Time=%d'%t); plt.axis('tight')   
plt.figure(2)
plt.plot(range(T),magn)

plt.figure(3)
plt.hist(magn[T-50000:])

