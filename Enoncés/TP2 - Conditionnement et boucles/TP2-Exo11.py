#%% Exercice 11 

def binomial(n,p):
    """ on suppose factorielle déjà écrite, cf exo 8"""
    return(factorielle(n)//(factorielle(p)*factorielle(n-p)))