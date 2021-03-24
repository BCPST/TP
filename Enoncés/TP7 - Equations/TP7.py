#%% Tracé de fonction

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(a, b, n) #remplacer a et b par les bornes du tracé et n par le nombre de points souhaités
y = f(x) #où f est la fonction à tracer

plt.plot(x,y) #prépare le dessin
plt.show() #affiche le dessin


#%% Méthode de balayage

def balayage(f,a,epsilon):
    """f est une fonction continue sur [a,b] telle que f(a)*f(b)<=0. 
    On veut retourner un encadrement de largeur epsilon d'une solution de f(x)=0 appartenant à [a,b]
    On considère les points a+epsilon,a+2epsilon,a+3epsilon... et on compare leur signe à celui de f(a). b ne sert pas..."""
    A = f(a)    #je calcule une fois f(a)
    x = a+epsilon    #je me place en a+epsilon; x a vocation à être a+k*epsilon
    compteur = 1    #le compteur est en fait k
    while f(x)*A>0:    #tant que f(a) et f(x) ont même signe (la fonction change de signe entre x et b, donc s'annulera plus tard).
        x = x+epsilon    #j'avance de epsilon
        compteur = compteur+1    # on a fait une itération de plus
    print("on a fait ",compteur,"itérations")
    return(x-epsilon,x)    #comme f(x)*A<=0, f a changé de signe donc s'est annulée lors de la dernière étape


#%% Méthode de dichotomie

def dichotomie(f,a,b,epsilon):
    """f est une fonction continue sur [a,b] telle que f(a)*f(b)<=0. 
    On veut retourner un encadrement de largeur epsilon d'une solution de f(x)=0 appartenant à [a,b]"""
    compteur  = 0 #on va compter le nombre d'itérations
    while abs(b-a)>epsilon: #tant que l'encadrement est de largeur trop grande
        compteur = compteur+1 #on a fait une itération de plus
        c = (a+b)/2. #on prend pour c le milieu de [a,b] (converti en flottant)
        if f(a)*f(c) <= 0: #si f s'annule entre a et c
            b = c #alors on remplace b par c
        else: #sinon nécessairement f s'annule entre c et b
            a = c #et donc on remplace a par c
    print("on a fait ",compteur,"itérations")
    return(a,b) #comme à présent |b-a|<=epsilon et que f s'annule entre a et b, on a gagné
    

#%% Méthode de Newton

def newton(f,fprime,a,epsilon):
    """ f est une fonction qui vérifie les bonnes hypothèses, fprime EST LA DERIVEE de f, 
    a une valeur approchée de la solution de f(x)=0 et epsilon la précision souhaitée"""
    compteur = 1
    x = a
    y = x-f(x)/fprime(x)
    while abs(y-x) > epsilon:
        compteur = compteur +1
        x = y
        y = x-f(x)/fprime(x)
    print("on a fait ",compteur,"itérations")
    return y
    
#%% Les tests
    
def f1(x):
    return 3*x-1
    
def f1prime(x):
    return 3

def f2(x):
    return x**5+3*x**2-10

def f2prime(x):
    return 5*x**4+6*x


print(balayage(f1,0,0.001))
# réponse : on a fait  334 itérations
#(0.33300000000000024, 0.33400000000000024)

print(dichotomie(f1,0,1,0.001))
#on a fait  10 itérations
#(0.3330078125, 0.333984375)

print(newton(f1,f1prime,1,0.001))
#on a fait  2 itérations
#0.33333333333333337

print(balayage(f2,0,0.00001))
#on a fait  135196 itérations
#(1.3519500000003895, 1.3519600000003895)

print(dichotomie(f2,0,2,0.00001))
#on a fait  18 itérations
#(1.3519515991210938, 1.351959228515625)

print(newton(f2,f2prime,1,0.00001))
#on a fait  5 itérations
#1.3519573251585202

