# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 13:54:37 2018

@author: Nicco
"""
import numpy as np
import matplotlib.pyplot as plt

def nearneigh(ind, rang, num): #mi individua i near.neigh. a uno spin dato
    nearn=list()
    for i in range(len(ind)):
        for j in range(-num,num+1):
            if(j==0): continue
            NN = list(ind)
            NN[i] +=j
            if(NN[i] >= rang[i]):
                NN[i] = NN[i] - rang[i]
            if(NN[i] < 0):
                NN[i] = rang[i]+NN[i]
            nearn.append(tuple(NN))
    return nearn;

def magnetization(c): #magn singolo passo MC (singola configurazione)
    d=np.prod(c.shape)
    return (float(np.sum(c)))/d

def clusteralg(c,bx, by,steps):
    mag=np.zeros(steps)
    N=c.shape
    px=1-np.exp(-2*bx) #prob transizione
    py=1-np.exp(-2*by)
    for t in range(steps):
        cambio=np.ones(N) #matrice degli spin da cambiare
        visitati=np.zeros(N) #ricorda i siti già visti
        trial=[]
        for i in range(len(N)):
            trial.append(np.random.randint(0,N[i]))
        trial=tuple(trial)
        visitati[trial]=1
        frontold=[trial]
        cambio[trial]=-1
        while(len(frontold)!=0):
            frontnew=[]
            for pos in frontold:
                spin=c[tuple(pos)]
                neiglist=nearneigh(pos,N,1)
                for neigsite in neiglist:
                    nn=tuple(neigsite)
                    if (c[nn]==spin and visitati[nn]==0 and nn[0]==pos[0]):
                        if (np.random.rand()<py):
                            frontnew.append(nn)
                            visitati[nn]=1
                            cambio[nn]=-1
                    if (c[nn]==spin and visitati[nn]==0 and nn[1]==pos[1]):
                        if (np.random.rand()<px):
                            frontnew.append(nn)
                            visitati[nn]
                            cambio[nn]=-1                                  
            frontold=frontnew
        c=c*cambio
        mag[t]=magnetization(c)

    return mag, c

def bootstrap(m, M, func,c): #m sample montecarlo, M numero copie fake, func funzione da chiamare
    estim_prov=np.zeros(M)
    for i in range(M):
        estim_prov[i]=func(np.random.choice(m, len(m)),c)
    stdev=np.sqrt(np.mean(estim_prov**2)-(np.mean(estim_prov))**2)
    return stdev

def bindercum(m,c):
    return len(m)*(sum(m**4))/(sum(m**2))**2

def suscet(m,c):
    d=np.prod(c.shape)
    return d*(np.mean(m**2)-(np.mean(abs(m))**2))

def intersection(array1,array2,base):
    for i in np.array(range(len(array1)))+1:
        if (array1[i]>array2[i] and array1[i-1]<array2[i-1]):
            x=np.linspace(base[i-1],base[i])
            y1=np.linspace(array1[i-1],array1[i],100)
            y2=np.linspace(array2[i-1],array2[i],100)
            inter=list(abs(y1-y2)).index(abs(y1-y2).min())
            return base[inter]
        
        if (array2[i]>array1[i] and array2[i-1]<array1[i-1]):
            x=np.linspace(base[i-1],base[i])
            y1=np.linspace(array1[i-1],array1[i],100)
            y2=np.linspace(array2[i-1],array2[i],100)
            inter=list(abs(y1-y2)).index(abs(y1-y2).min())
            return base[inter]
        
        
    
            
        
        
        
    

