import random as rd 
import matplotlib.pyplot as plt 
import numpy as np

def mystere(n):
    H=1 
    k=1 
    indices=[1] 
    for i in range(2,n+1):
        while H<i:
              k=k+1
              H=H+1./k
        print(k,H)
        indices.append(k) 
    return(indices)
    
n=8 
plt.plot(range(1,n+1),mystere(n)) 
t=np.linspace(1,n,1000) 
plt.plot(t,np.exp(t)) 
plt.show()