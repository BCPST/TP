"""
Principes de programmation :
1. Trouver les variables d'entrée de de sortie
2. Ecrire un algorithme qui permette de passer de l'entrée à la sortie
3. Prévoir les tests à effectuer pour voir que le programme fonctionne
4. On ouvre Python et on programme
5. Commenter le code
6. Tester le code avec le 3.
7. Débugger le code
8. Utiliser le code
"""

def E1(x):
    """Valeur absolue de x"""
    if x >= 0:
        return x
    else:
        return -x
    # return ((x)**2)**(1/2)
    # return sqrt(x*x)
    # return abs(x)

def E2(x):
    """Partie entière de x"""
    a = 0
    if x > 0:
        # return int(x)
        while a < x:
            a += 1
        return a-1
    else:
        # if -int(-x) == x:
        #     return -int(-x)
        # else:
        #     return -int(-x)-1
        while a < x:
            a-= 1
        return a

def E3(a, b):
    """Reste de la division euclidienne de a par b"""
    t = a
    if b >= 0:
        while t >= 0:
            t = t - b
        r = t + b
    else:
        r = 0
    return r
    # return a-E2(a/b)*b
    # return a%b

def E4(x, y):
    """Maximum de x et y"""
    if x >= y:
        return x
    else:
        return y
    # return max((x, y))

def E5(year):
    """Est-ce que l'année est bisextile ?"""
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False

def E6(n, u=3):
    """n-ième terme de la suite"""
    for k in range(1, n+1):
        u = 2*u - 1
    return u

def E7(n):
    """Somme des n premiers termes de la suite u de l'exo 6"""
    s = 0
    for k in range(0, n+1):
        s += E6(k)
    return s
    # return sum(E6(k) for k in range(0, n+1))

def E8(n):
    """Factorielle de n"""
    p = 1
    for k in range(n):
        p *= k+1
    return p
    # if n == 0:
    #     return 1
    # else:
    #     return n*E8(n-1)

def E9(a, n):
    """a puissance n"""
    if n >= 0:
        p = 1
        for k in range(1, n+1):
            p *= a
        return p
    else:
        return 1/E9(a, -n)
    # return a**n

def E10(n):
    """Somme triangulaire i/j"""
    s = 0
    for j in range(1, n+1):
        for i in range(1, j+1):
            s += i/j
    return s

def E11(n, p):
    """p parmis n"""
    return E8(n)/(E8(p)*E8(n-p))

def E12(n):
    """Renvoie le triangle de pascal des n premiers termes sous forme de texte"""
    pascal = []
    for i in range(0, n):
        line = [1]
        for j in range(1, i+1):
            line.append(pascal[i-1][j-1]+pascal[i-1][j])
        line.append(1)
        pascal.append(line)
    pascal = [[1]] + pascal
    text = ''
    for line in pascal:
        for number in line:
            text += str(number) + ' '
        text += '\n'
    text = text[:-2]
    return text

def E12b(n):
    out = ''
    for i in range(0, n+1):
        for j in range(0, i+1):
            out += f'{int(E11(i, j))} '
        out += '\n'
    return out
