"""
Pour une somme privilégier petits termes en premier pour éviter des arrondis excessifs sur python.
"""

## Ex 12 :

def calc_delta(a, b, c):
    return b**2 - 4*a*c
# 1.
def nbe_racines(a, b, c):
    delta = calc_delta(a, b, c)
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0

# 2.
def solve(a, b, c):
    """Résout un polynome ax²+bx+c=0"""
    delta = calc_delta(a, b, c)
    if delta > 0:
        return (-b-delta**(-1)/(2*a), -b+delta**(-1)/(2*a))
    elif delta == 0:
        return (-b/(2*a))
    else:
        return (None)

## Ex 13 :

def bissextile(year):
    """l'assertion year est-elle une année bissextile ?"""
    if year%4 != 0:
        return False
    elif year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    else:
        return True

## Ex 14 :

# 1.
def maximum(x, y):
    """fonction maximum sans if"""
    return (x+y+abs(x-y))/2

# 2.
def minimum(x, y):
    """fonction minimum sans if"""
    return (x+y-abs(x-y))/2

# 3.
def max4(a,b,c,d):
    return maximum(maximum(a, b),maximum(c, d))

# 4.
def sort3(a, b, c):
    temp = [a, b, c]
    first = int(maximum(maximum(a, b), c))
    last = int(minimum(minimum(a, b), c))
    temp.remove(first)
    temp.remove(last)
    return first, temp[0], last

## Ex 15 :

def anniversaires(j_naiss, m_naiss, a_naiss, jour, mois, annee):
    """nombre d'anniversaire qui ont pu avoir lieu entre les deux dates"""
    n = 0
    b_day = True
    for year in range(a_naiss, annee):
        year += 1
        if not (not bissextile(year) and m_naiss == 2 and j_naiss > 28):
            if year == annee:
                if m_naiss < mois or (m_naiss == mois and j_naiss <= jour):
                    n += 1
            else:
                n += 1
    return n

## Ex 16 :

"""
Ecrire une ligne de commande permettant de déterminer le dernier chiffre de
2017²⁰¹⁹ sans avoir à afficher le nombre en entier :
(2017**2019)%10
int(str(2017**2019)[-1])
Combien de chiffres possède ce nombre :
len(str(2017**2019))
"""