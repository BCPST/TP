
#%% Première version
#on écrit sum_i (sum_j)

def sommedouble1(n):
    S=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            S=S+i/j
    return(S)
    
#%% Deuxième version
#on écrit sum_j (sum_i)

def sommedouble2(n):
    S=0
    for j in range(1,n+1):
        for i in range(1,j+1):
            S=S+i/j
    return(S)
    
#%% Troisème version
#on éfait une somme rectangulaire et on garde ce qui nous intéresse

def sommedouble3(n):
    S=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i<=j:
                S=S+i/j
    return(S)