# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 15:24:54 2018

@author: Nicco
"""

import numpy as np
import matplotlib.pyplot as plt
import functions as fx
import time
import scipy.optimize as sc
# =============================================================================
# Main code
# =============================================================================

T=6000
risol=25
cut=1000

beta=np.linspace(0.21,0.24,risol) 

binder=np.zeros(risol)
susc=np.zeros(risol)
stbinder=np.zeros(risol)
stsusc=np.zeros(risol)
sizes=[5,10,12]

msusc=np.zeros(len(sizes))
mbeta=np.zeros(len(sizes))
merr=np.zeros(len(sizes))

start = time.time()
mag=np.zeros((len(sizes),risol))

for L in sizes:
    print "Lattice dimension:",L  
    for j in range(len(beta)):
        conf=2*np.random.randint(2, size=(L,L,L))-1    
        magn,cc=fx.clusteralg(conf,beta[j], beta[j],T)
        print(j)
        susc[j]=fx.suscet(magn[cut:],conf)
        stsusc[j]=fx.bootstrap(magn[cut:],500,fx.suscet,conf)
        binder[j]=fx.bindercum(magn[cut:],conf)
        stbinder[j]=fx.bootstrap(magn[cut:],500,fx.bindercum,conf)
        if (L==40):
            plt.figure(j+4)
            plt.title('beta=' + str(beta[j]))
            plt.hist(magn, normed="True")
            plt.savefig('histBeta=' + str(beta[j]) + '.pdf')
    mag[sizes.index(L),:]=np.mean(magn[cut:])
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
    plt.savefig("clusterbinder.png")
    plt.figure(3)
    plt.grid(True)
    plt.title("Suscettibilita'")
    plt.xlabel("Beta")
    plt.ylabel("Suscettibilita'")
    plt.errorbar(beta,susc, yerr=stsusc, marker='o', markersize=1.4, capsize=3, label=L)
    plt.legend()
    plt.savefig("clustersusc.png")

print '%f' %(time.time()-start)

#trova gamma su nu

plt.figure(5)
plt.grid(True)
newerr=merr/msusc
plt.title('Max susc. vs Size (log)')
plt.xlabel('log(size)')
plt.ylabel('log(max.susc.)')
plt.errorbar(np.log(sizes),np.log(msusc),newerr,marker='o', markersize=1.5, linestyle='',capsize=3)
popt,pcov=sc.curve_fit(fx.linearfun, np.log(sizes),np.log(msusc),p0=[1,1],sigma=newerr,absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
plt.plot(np.linspace(1.5,2.75,100),popt[1]+popt[0]*np.linspace(1.5,2.75,100))

#trova 1/nu

plt.figure(5)
plt.grid(True)
newerr=0.03/(0.441-mbeta)
plt.title('Critical beta at finite volume vs Size (log)')
plt.xlabel('log(size)')
plt.ylabel('log(betac(V)-betac)')
plt.scatter(np.log(sizes),np.log(0.441-mbeta),marker='o', s=5, color='Red')
popt,pcov=sc.curve_fit(fx.linearfun, np.log(sizes),np.log(0.441-mbeta),p0=[1,1],sigma=newerr,absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
plt.plot(np.linspace(2.5,3.5,100),popt[1]+popt[0]*np.linspace(2.5,3.5,100))

