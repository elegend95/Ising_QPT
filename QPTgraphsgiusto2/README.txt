T=6500
risol=20 
cut=800
   
#beta=np.array([15.]) 

binder=np.zeros(risol)
susc=np.zeros(risol)
stbinder=np.zeros(risol)
stsusc=np.zeros(risol)
sizes=[8,12,16]

start = time.time()

for N in [50,75]: 