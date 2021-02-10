#%% Exercice 9

def puissance(a,n):
    puis=1
    for _ in range(n): #le nom du compteur n'a pas d'importance car il ne sert pas dans la boucle
        puis=puis*a
    return(puis)
    
def puissance2(a,n):
    if n==0:
        return(1)
    else:
        return(a*puissance(a,n-1))