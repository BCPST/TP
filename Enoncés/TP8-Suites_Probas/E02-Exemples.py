import random as rd
import matplotlib.pyplot as plt
import numpy as np

#%% Exemple 1

L=[rd.random() for k in range(2000)]
Bornes=np.linspace(0,1,11)
plt.hist(L,Bornes)
plt.show()
 
#%% Exemple 2

L=[int(6*rd.random()+1) for k in range(2000)]
Frequences=[L.count(k)/2000 for k in range(1,7)]
plt.bar(np.arange(1,7),Frequences)
plt.show()

#%% Exemple 3
p=0.7 
L=[rd.random()<p for k in range(2000)] 
Frequences=[L.count(k)/2000 for k in [True,False]] 
plt.bar(np.arange(1,3),Frequences) 
plt.show()
