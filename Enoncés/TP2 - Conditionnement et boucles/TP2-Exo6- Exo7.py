#%%Exercice 6

#%% Première version
# Avec boucle for et range ne contenant qu'un argument

def suite1(n):
    u=3
    for k in range(n): # on répète n fois
        u=2*u-1
    return(u)
    
#%%Deuxième version
# Avec boucle for et range contenant 2 arguments 

def suite2(n):
    u=3
    for k in range(1,n+1): #on répète aussi n fois
        u=2*u-1
    return(u)
    
#%%Troisième version
# Avec boucle while

def suite3(n):
    u=3
    k=0
    while k<n:
        u=2*u-1
        k=k+1
    return(u)
    
#%%Quatrième version
# en utilisant des listes

def suite4(n):
    u=[3]
    for k in range(1,n+1):
        u.append(2*u[k-1]-1) #on ajoute un terme à chaque fois
    return(u) #on devrait renvoyer u[n]. Ici je retourne u pour réutiliser toute la liste plus tard
    
#%%Cinquième version
# avec un programme récursif

def suite5(n):
    if n==0:
        return(3)
    else:
        return(2*suite(n-1)-1)
        
#%% Exercice 7

#%%Première version

def somme1(n):
    S=3
    for k in range(1,n+1):
        S=S+suite1(k)
    return(S)
    
#%%Deuxième version

def somme2(n):
    u=3
    S=3
    for k in range(1,n+1):
        u=2*u-1
        S=S+u
    return(S)
    
#%%Troisième version

def somme3(n):
    return(sum(suite4(n)))

    