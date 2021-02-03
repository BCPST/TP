from math import pi
import math
import matplotlib.pyplot as plt

"""
Opérateurs :
+ addition
- soustraction
* multiplication
/ division
// quotient de la division des entiers
% modulo
** puissance

Opérateurs de comparaison
== test d'égalité
!= test d'inégalité
>
>=
<
<=

Opérateurs logiques
or
and
not

Types en Python

int pour integer (entier)
float pour floating point number (décimaux)
complex (complexes)
bool pour booleans (booléens)
str pour string (chaine de caractère)
list (liste)
tuple (tuple)
dict pour dictionnary (dictionnaire)

Modules

import math
import math as m
from math import exp
from math import *

Commenter un programme

# précède un commentaire
"""""" contenant au milieu une description
"""

def cir(r):
    return 2*pi*r

def moy(a, b):
    return (a+b)/2

def hms(tps):
    h = tps//(60*60)
    min = (tps - 60*60*h)//60
    sec = (tps - 60*60*h - 60*min)
    return h, min, sec

def draw_cos(a, b):
    x = []
    y = []
    for i in range(1, 10):
        x.append(i*a)
        y.append(math.cos(i*a))
    plt.plot(x, y)
    plt.show()

def double(n):
    return 2*n

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def fact2(n):
    s = 1
    for k in range(2, n+1):
        s *= k
    return s