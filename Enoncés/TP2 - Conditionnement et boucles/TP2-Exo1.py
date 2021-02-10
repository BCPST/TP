#%% Exercice 1

def valeur_absolue(x):
    """|x| vaut x si x>=0 et -x si x<0"""
    if x>=0:
        return(x)
    else:
        return(-x)
        
def valeur_absolue2(x):
    """|x| vaut x si x>=0 et -x si x<0"""
    if x>=0:
        return(x)
    elif x<0:
        return(-x)