#%% Exercice 8

def factorielle(n):
    facto=1
    for k in range(1,n+1): #k varie de 1 à n
        facto=facto*k
    return(facto)

def factorielle2(n):
    if n<=1:
        return 1
    else:
        return(n*factorielle2(n-1))