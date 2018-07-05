# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 11:23:46 2018

@author: Nicco
"""
import numpy as np
import matplotlib.pyplot as plt
import functions as fx


L=10

T=5000
risol=10
cut=100

beta=np.array([1.5]) 

binder=np.zeros(risol)
susc=np.zeros(risol)
stbinder=np.zeros(risol)
stsusc=np.zeros(risol)
sizes=[8,10]

for N in [10]:
 #   for i in beta:
    print("Temperature:" + str(0.05/30))
    a=0.5
    N=30
    gamma=np.linspace(1/1.2,1/0.8,risol)
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
        plt.figure(100)
        plt.plot(1/gamma,ueue,marker='o')
        
        
        plt.figure(N)
        plt.grid(True)
        plt.title("Cumulante di binder")
        plt.xlabel("gamma")
        plt.ylabel("Binder")
        plt.errorbar(1/gamma,binder,yerr=stbinder, marker='o', markersize=1.4, capsize=3, label=N)
        print('ue')
        plt.legend()
        
        plt.figure(N+1)
        plt.grid(True)
        plt.title("suscettibilita'")
        plt.xlabel("Beta")
        plt.ylabel("Suscettibilita'")
        plt.errorbar(1/gamma,susc, yerr=stsusc, marker='o', markersize=1.4, capsize=3, label=N)
        plt.legend()
            
            