## TP7
"""
Dans l'idéal on sait résoudre :
ax + b = 0
ax² + bx + c = 0
ax³ + bx² + cx + d = 0
ax⁴ + bx³ + cx² + d = 0
avec tout ce qui s'y ramène
(plus de formules pour polynôme de degré supérieur ou égal à 5)

Peut-on trouver un algorithme qui étant donnée une équatin f(x) ) 0 dont on sait quelle a une solution, permettre d'en trouver une valeur approchée ?

Deux algorithmes proposés :
- dichotomie (au programme)
- méthode de Newton (classique)
"""

# Fonctions de tests
f1 = lambda x: 3*x - 1
f2 = lambda x: x**5 + 3*x**2 - 10
f2prime = lambda x: 5*x**4 + 6*x

## Dichotomie
"""
Principe de la dichotomie :
Soit f une fonction continue sur [a, b] telle que f(a)*f(b) >= 0 (f change de signe)

On pose c = (a+b)/2 (milieu de [a, b])
Si f(c)*f(a)<= 0, la fonction change de signe entre a et c, donc l'intervalle [a, c] contient la solution, on peut remplacer b par c.
Sinon, la solution est entre c et b et on peut remplacer a par c.
Maintenant la solution est entre a et b mais on a divisé la taille de l'intervalle par 2.
"""

def dichotomie(f, a, b, epsilon):
    """
    par une fonction récursive
    f la fonction continue
    (a, b) l'intervalle sur lequel f change de signe
    epsilon la précision
    """
    if abs(a-b) <= epsilon:
        return (a, b)

    c = (a + b)/2
    if f(c)*f(a) <= 0:
        return dichotomie(f, a, c, epsilon)
    else:
        return dichotomie(f, c, b, epsilon)


def dichotomie2(f, a, b, epsilon):
    """
    par une boucle while
    f la fonction continue
    (a, b) l'intervalle sur lequel f change de signe
    epsilon la précision
    """
    while abs(a-b) > epsilon:
        c = (a + b)/2
        if f(c)*f(a) <= 0:
            b = c
        else:
            a = c
    return (a, b)


def dichotomie3(f, a, b, epsilon):
    """
    par une boucle for
    f la fonction continue
    (a, b) l'intervalle sur lequel f change de signe
    epsilon la précision
    """
    n = int(abs(a-b)/epsilon)
    for _ in range(n):
        c = (a + b)/2
        if f(c)*f(a) <= 0:
            b = c
        else:
            a = c
    return (a, b)


## Newton
"""
Principe de la méthode de Newton :
Le théorème dit qu'on a la suite définie par x_0 et x_(n+1) = x_n - f(x_n)/f'(x_n), qui converge vers l telle que l est la solution à f(x)=0 à condition que tout aille bien (x_0 bien choisi, f'(l)!=0 et f'(x_0)!=0).

Comme x_n tend vers la, pour n assez grand, x_n est environ égal à l.
On s'arrête [arbitrairement] quand x_(n+a) - x_n <= epsilon (critère discutable).
"""

def terme_suivant(f, fprime, x):
    return x - f(x)/fprime(x)

def newton(f, fprime, x0, epsilon):
    x = x0
    y = terme_suivant(f, fprime, x)
    while abs(y - x) > epsilon:
        x = y
        y = terme_suivant(f, fprime, x)
    return y

## Application physique

def application(H=142, latitude=48.5734053, g=9.81, omega=7.3*10**-5, epsilon=10**-5):
    from math import cos, pi

    z = lambda t: -g/2*t**2 + (omega**2*g*cos(latitude*2*pi/360)**2)/6*t**4+H
    zprime = lambda t: -g*t + 4*(omega**2*g*cos(latitude*2*pi/360)**2)/6*t**3

    return dichotomie1(z, 0, 100, epsilon), newton(z, zprime, 5, epsilon)

