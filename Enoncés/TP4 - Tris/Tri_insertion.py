#%%Tri insertion

#%% Fonction insere

def insere(l,i):
    L=l[:]
    S=L[i]
    j=0
    while S>L[j] and j<i:
        j=j+1
    L[j+1:i+1]=L[j:i]
    L[j]=S
    return(L)

#%% Tri

def tri_insertion(l):
    n=len(l)
    L=l[:]
    for i in range(1,n):
        L=insere(L,i)
    return(L)
    
#%%Ou, en place : 

#%% Fonction insere

def insere(i,l):
    j=0
    S=l[i]
    while S>l[j] and j<i:
        j=j+1
    l[j+1:i+1]=l[j:i]
    l[j]=S

#%% Tri

def tri_insertion(l):
    n=len(l)
    for i in range(1,n):
        insere(i,l)