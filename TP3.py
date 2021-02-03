"""
Les listes :
C'est un type composé/un conteneur -> type str : chaîne de caractères
par opposition aux types simples float/int/complex/bool

Une liste est une collection d'objets séparés par des virgules et est délimitée par des crochets.

Utilité :
- stocker les éléments d'une suite (les premiers termes)
- les listes de listes permettest de faire des tableaux

Si L est une liste :
- len(l) est le nombre d'éléments de L
- L[i] est l'élément numéro i
- L[0] est le 1er élément
- L[len(L)-1] est le dernier élément
- L[-k] est pareil que L[len(l)-k]
- L[p:n] est partie de la liste allant de l'élément p à l'élément n

Pour copier la liste :
idée : copie = liste => Problème, si je modifie la copie, je modifie la liste !
solution :
from copy import deepcopy
copie = deepcopy(liste)

Definition en extension et en compréhension d'une liste
"""

def E1(ls, value):
    for i in range(len(ls)):
        if ls[i] == value:
            return True
    return False

def is_in(ls, value):
    """value est contenu dans ls"""
    # return value in ls
    for element in ls:
        if element == value:
            return True
    return False

def E2(ls):
    """renvoie la somme des éléments de la liste"""
    # return sum(ls)
    sum = 0
    for value in ls:
        sum += value
    return sum

def E3(ls):
    """renvoie la moyenne des termes de la liste"""
    return E2(ls)/len(ls)

def E4(ls):
    """renvoie le maximum de la liste, qui ne doit pas être vide"""
    max = ls[0]
    for element in ls:
        if element > max:
            max = element
    return max

def E5(ls):
    """renvoie l'indice du maximum de la liste, qui ne doit pas être vide"""
    max = ls[0]
    n = 0
    i = 0
    for element in ls:
        if element > max:
            max = element
            n = i
        i += 1
    return n

def E7(n):
    """renvoie la liste des diviseurs d'un entier n qui sont plus petits que 100"""
    return [x for x in range(100+1) if x%n==0]

def E8():
    out = []
    for b in range(13):
        out += [(a,b) for a in list(range(13)) if a+b==12]
    return out

def maxrecursif(L):
    if len(L) == 1:
        return L[0]
    if L[-1] > maxrecursif(L[:-1]):
        return L[-1]
    else:
        return maxrecursif(L[:-1])

def maximum(L):
    n = 0
    M = L[0]
    for k, el in enumerate(L):
        if el > M:
            M = el
            n = k
    return n


def occurences(L, x):
    ls = [k for k, el in enumerate(L) if el == x]
    return ls