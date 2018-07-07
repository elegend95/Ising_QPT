# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 11:23:46 2018

@author: Nicco
"""
import numpy as np
import matplotlib.pyplot as plt
import functions as fx
import time

L=10

T=7500
risol=30 
cut=100
   
#beta=np.array([15.]) 

binder=np.zeros(risol)
susc=np.zeros(risol)
stbinder=np.zeros(risol)
stsusc=np.zeros(risol)
sizes=[8,15]

start = time.time()

for N in [50,75,100]: 
 #   for i in beta:
    temp=0.1
    a=1./(N*temp)
    gamma=np.linspace(0.8,1.3,risol)
    gammah=-0.5*np.log(np.tanh(a*gamma))
    ueue=np.zeros(risol)
    for L in sizes:
        for j in range(len(gamma)):
            kappa=a*np.ones(risol)
            conf=2*np.random.randint(2, size=(L,N))-1    
            magn, c=fx.clusteralg(conf,kappa[j],gamma[j],T) 
            ueue[j]=np.mean(abs(magn[cut:]))
            print(j)
            susc[j]=fx.suscet(magn[cut:],conf)
            stsusc[j]=fx.bootstrap(magn[cut:],500,fx.suscet,conf)
            binder[j]=fx.bindercum(magn[cut:],conf)
            stbinder[j]=fx.bootstrap(magn[cut:],500,fx.bindercum,conf)
        
        plt.figure(66)
        plt.grid(True)
        plt.title('magnetization')
        plt.plot(gamma,ueue,marker='o')
        
        
        plt.figure(N)
        plt.grid(True)
        plt.title("Cumulante di binder ("+str(N)+" passi")
        plt.xlabel("gamma")
        plt.ylabel("Binder")
        plt.errorbar(gamma,binder,yerr=stbinder, marker='o', markersize=1.4, capsize=3, label=L)
        plt.legend()
        plt.savefig('bindercum'+str(N)+'.pdf')
        
        plt.figure(N+1)
        plt.grid(True)
        plt.title("Suscettibilita' ("+str(N)+" passi")
        plt.xlabel("gamma")
        plt.ylabel("Suscettibilita'")
        plt.errorbar(gamma,susc, yerr=stsusc, marker='o', markersize=1.4, capsize=3, label=L)
        plt.legend()
        plt.savefig('suscett'+str(N)+'.pdf')    
        
print '%f' %(time.time()-start)