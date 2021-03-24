import random as rd
import matplotlib.pyplot as plt
import numpy as np

nb_individus_total=1000 
L=[] 
for f in range(0,101):
    nb_positifs=0
    nb_malades_positifs=0
    for k in range(1,nb_individus_total):
        Individu_malade=False
        Test_positif=False
        if 100*rd.random()<f:
            Individu_malade=True
            if rd.random()<0.99:
                 Test_positif=True 
        else:
            if rd.random()<0.002:
                 Test_positif=True
        if Test_positif and Individu_malade:
            nb_malades_positifs = nb_malades_positifs+1
        if Test_positif:
            nb_positifs = nb_positifs+1
    L.append(nb_malades_positifs/nb_positifs)
    
A=np.arange(101) 
plt.plot(A,L)
plt.show()
