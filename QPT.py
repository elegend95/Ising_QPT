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

beta=np.array([2.]) 

binder=np.zeros(risol)
susc=np.zeros(risol)
stbinder=np.zeros(risol)
stsusc=np.zeros(risol)
sizes=[10,13,16]

for i in beta:
    print("Temperature:" + str(1/i))
    a=0.1
    N=int(i/a)
    gamma=np.linspace(1,2,risol)
    gammah=-0.5*np.log(np.tanh(a*gamma))
    for L in sizes:
        for j in range(len(gamma)):
            kappa=a*np.ones(risol)
            conf=2*np.random.randint(2, size=(L,N))-1    
            magn=fx.clusteralg(conf,kappa[j],gamma[j],T)
            print(j)
        #        susc[j]=fx.suscet(magn[cut:],conf)
        #        stsusc[j]=fx.bootstrap(magn[cut:],500,fx.suscet,conf)
            binder[j]=fx.bindercum(magn[cut:],conf)
            stbinder[j]=fx.bootstrap(magn[cut:],500,fx.bindercum,conf)
        
        plt.figure(2)
        plt.grid(True)
        plt.title("Cumulante di binder")
        plt.xlabel("Beta")
        plt.ylabel("Binder")
        plt.errorbar(gamma,binder,yerr=stbinder, marker='o', markersize=1.4, capsize=3, label=i)
        print('ue')
        plt.legend()
        
        plt.figure(3)
        plt.grid(True)
        plt.title("suscettibilita'")
        plt.xlabel("Beta")
        plt.ylabel("Suscettibilita'")
        plt.errorbar(gamma,susc, yerr=stsusc, marker='o', markersize=1.4, capsize=3, label=i)
        plt.legend()