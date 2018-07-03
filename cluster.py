# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 15:24:54 2018

@author: Nicco
"""

import numpy as np
import matplotlib.pyplot as plt
import functions as fx
# =============================================================================
# Main code
# =============================================================================

T=3000
risol=20
cut=100

beta=np.linspace(0.35,0.46,risol)

binder=np.zeros(risol)
susc=np.zeros(risol)
stbinder=np.zeros(risol)
stsusc=np.zeros(risol)
sizes=[10,12]

msusc=np.zeros(len(sizes))
mbeta=np.zeros(len(sizes))
merr=np.zeros(len(sizes))


for L in sizes:
    print "Lattice dimension:",L
    for j in range(len(beta)):
        conf=2*np.random.randint(2, size=(L,L))-1    
        magn=fx.clusteralg(conf,beta[j], beta[j],T)
        print(j)
        susc[j]=fx.suscet(magn[cut:],conf)
        stsusc[j]=fx.bootstrap(magn[cut:],500,fx.suscet,conf)
        binder[j]=fx.bindercum(magn[cut:],conf)
        stbinder[j]=fx.bootstrap(magn[cut:],500,fx.bindercum,conf)
# =============================================================================
#         if (L==28):
#             plt.figure(j+4)
#             plt.title('beta=' + str(beta[j]))
#             plt.hist(magn, normed="True")
#             plt.savefig('histBeta=' + str(beta[j]) + '.pdf')
# =============================================================================
    msusc[sizes.index(L)]=susc.max()
    mbeta[sizes.index(L)]=beta[list(susc).index(susc.max())]    
    merr[sizes.index(L)]=stsusc[list(susc).index(susc.max())]    
    plt.figure(2)
    plt.grid(True)
    plt.title("Cumulante di binder")
    plt.xlabel("Beta")
    plt.ylabel("Binder")
    plt.errorbar(beta,binder,yerr=stbinder, marker='o', markersize=1.4, capsize=3, label=L)
    plt.legend()
    plt.savefig("clusterbinder.pdf")
    plt.figure(3)
    plt.grid(True)
    plt.title("suscettibilita'")
    plt.xlabel("Beta")
    plt.ylabel("Suscettibilita'")
    plt.errorbar(beta,susc, yerr=stsusc, marker='o', markersize=1.4, capsize=3, label=L)
    plt.legend()
    plt.savefig("clustersusc.pdf")
plt.figure(4)
plt.grid(True)
plt.title("Susc. massima vs lattice size")
plt.xlabel("Size")
plt.ylabel("Suscettibilita' max")
plt.errorbar(sizes,msusc, yerr=merr, marker='o', markersize=1.4, capsize=3, label=L)
plt.legend()
plt.savefig("maxsusc.pdf")    
