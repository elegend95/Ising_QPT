# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 11:05:03 2018

@author: Nicco
"""

import numpy as np
import matplotlib.pyplot as plt
import functions as fx


kappa=1
gamma=1

#conf=2*np.random.randint(2, size=(L,N))-1
conf=np.ones([L,N])
T=3000

#cold start, high temp phase

# =============================================================================
# beta=0.2
# for size in [10, 50, 80]:
#     conf=np.ones([size,size])
#     mag, confee=fx.metropolis(conf,beta,T)
#     plt.figure(1)
#     plt.grid(True)
#     plt.title('Relaxation (cold start, beta=0.2, 2D Ising)')
#     plt.xlabel('Monte Carlo time')
#     plt.ylabel('Magnetization')
#     plt.plot(range(T),mag,linestyle='',marker='o',markersize=1, label=size)
# plt.legend()
# plt.savefig('relaxation2D.png')
# 
# beta=1
# =============================================================================

#ergodicity breaking test

# =============================================================================
# beta=0.5
# for i in [0,1,2]:
#     for size in [10]:
#         conf=2*np.random.randint(2, size=(size,size))-1    
#         mag, confee=fx.metropolis(conf,beta,T)
#         plt.figure(1)
#         plt.grid(True)
#         plt.title('Ergodicity breaking (hot start, beta=0.5, 2D Ising, size=10)')
#         plt.xlabel('Monte Carlo time')
#         plt.ylabel('Magnetization')
#         plt.scatter(range(T),mag,marker='o',s=1)
# 
# plt.legend()
# plt.savefig('nonergodic2D.png')
# 
# =============================================================================

#cluster relaxation test

beta=0.2
for size in [10,20,30,40,50]:
    conf=np.ones([size,size])
    mag, confee=fx.clusteralg(conf,beta, beta,T)
    plt.figure(1)
    plt.grid(True)
    plt.title('Cluster relaxation (cold start, beta=0.2, 2D Ising)')
    plt.xlabel('Monte Carlo time')
    plt.ylabel('Magnetization')
    plt.plot(range(T)[5:],mag[5:],linestyle='',marker='o',markersize=1, label=size)
plt.legend()
#plt.savefig('relaxation2Dcluster.png')
T=200

# =============================================================================
# beta=1
# for i in [0]:
#     for size in [50]:
#         conf=2*np.random.randint(2, size=(size,size))-1    
#         mag, confee=fx.metropolis(conf,beta,T)
#         plt.figure(1)
#         plt.grid(True)
#         plt.title('Ergodicity (hot start, beta=1, 2D Ising, size=50)')
#         plt.xlabel('Monte Carlo time')
#         plt.ylabel('Magnetization')
#         plt.scatter(range(T),mag,marker='o',s=3)
# 
# plt.legend()
# #plt.savefig('ergodic2Dcluster.png')
# 
# =============================================================================
