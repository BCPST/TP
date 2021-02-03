"""TP 4 : tri de listes"""

## Tri sélection

def indice_min(l, i):
    """renvoie l'indice du minimum de l"""
    imin = i
    while i < len(l):
        if l[imin] > l[i]:
            imin = i
        i += 1
    return imin

def echange(out, i, j):
    """procédure d'échange de i et j sur l"""
    out[i], out[j] = out[j], out[i]

def tri_selection(l):
    """renvoie une liste triée par ordre croissante en utilisant des fonctions annexes et par principe de selection"""
    out = l[:]
    for n in range(len(out)-1):
        echange(out, n, indice_min(out, n))
    return out

def tri_selection_2(l):
    """renvoie une liste triée par ordre croissante sans utiliser de fonctions annexes et par principe de selection"""
    out = l[:]
    for n in range(len(out)-1):
        m = n
        i = n
        while i < len(l):
            if l[m] > l[i]:
                m = i
            i += 1
        out[n], out[m] = out[m], out[n]
        echange(out, n, indice_min(out, n))
    return out

## Tri insertion

def insere(l, i):
    """renvoie une liste avec une insertion de l'élément d'indice i dans l tel que les i premiers termes de la liste de sortie sont triés par ordre croissant"""
    j = 0
    while l[i] > l[j] and j < len(l):
        j += 1
    return l[:j] + [l[i]] + l[j:i] + l[i+1:]

def tri_insertion(l):
    """renvoie une liste triée par ordre croissante en utilisant des fonctions annexes et par principe d'insertion"""
    for k in range(len(l)):
        l = insere(l, k)
    return l

def tri_insertion_2(l):
    """renvoie une liste triée par ordre croissante sans utiliser de fonctions annexes et par principe d'insertion"""
    for k in range(len(l)):
        j = 0
        while l[i] > l[j] and j < len(l):
            j += 1
        l = l[:j] + [l[i]] + l[j:i] + l[i+1:]
    return l

def tri_insertion_3(l, k=0):
    """renvoie une liste triée par ordre croissante en utilisant une récurssion et par principe d'insertion"""
    if k >= len(l):
        return l
    j = 0
    while l[k] > l[j] and j < len(l):
        j += 1
    return tri_insertion_3(l[:j] + [l[k]] + l[j:k] + l[k+1:], k+1)




## Tri à bulles

def tri_bulle(l):
    """renvoie une liste triée par ordre croissante sans utiliser de fonctions annexes et par principe de tri à bulles"""
    out = l[:]
    for k in range(len(out)-1):
        for n in range(len(out)-1):
            if out[n] > out[n+1]:
                out[n], out[n+1] = out[n+1], out[n]
    return out

def tri_bulle_variante(l):
    """renvoie une liste triée par ordre croissante sans utiliser de fonctions annexes et par principe de tri à bulles avec une légère optimisation"""
    out = l[:]
    for k in range(len(out)-1):
        operation = False
        for n in range(len(out)-1):
            if out[n] > out[n+1]:
                operation = True
                out[n], out[n+1] = out[n+1], out[n]
        if not operation:
            break
    return out
