"""TP 5 : Matrices"""

"""
Matrices avec python :
- soit des lites de listes (oblige à réécrire les méthodes d'opérations)
- soit convertir une liste de listes en tableau : "array", il faut utiliser le module numpy
"""

import numpy as np
import numpy.linalg as alg  # se note aussi lg

A = np.array([[1, 2, 3], [4, 5, 6]]) # créer une matrice à partir d'une liste de listes
B = np.array([i for i in range(1, 7)])
C = B.reshape((3, 2))  # créer une matrice de taille 3*2 avec les coefficients de B

np.zeros((2, 4))  # renvoie une matrice de taille 2*4 avec des coefficients nuls
np.ones((2, 4))  # renvoie une matrice de taille 2*4 avec des coefficients égal à 1
np.eye(3) # renvoie la matrice identité

np.random.rand(30, 40)  # renvoie une matrice de taille 30*40 avec des ciefficients aléatoires entre 0 et 1
np.random.randint(10, size=(30, 40)) # renvoie une matrice de taille 30*40 avec des ciefficients aléatoires entiers entre 0 et 9

A = np.random.randint(10, size=(10, 10))
a, b, i, j = 5, 6, 4, 2

A.shape  # renvoie la taille de la matrice A sous forme de tuple (i*j)
A[i, j]  # renvoie le coefficient à la i-ème ligne et j-ème colonne
A[0, :]  # on prends tous les a(i, j) tels que i=0 et j est quelconque (matrice de la première ligne)
A[0:1, :]  # renvoie la matrice ligne d'indice 0
A[a: b, :]  # renvoie les coefficients tels que a<=i<b et j quelconque

A.sum() # renvoie la somme de tous les coefficients
A.sum(axis=0)  # renvoie la somme de tous les coefficients à la verticale
A.sum(axis=1)  # renvoie la somme de tous les coefficients à l'horizontale

# un masque est une matrice de bool
A.sum(axis=1) > 4  # est un masque

A, B = np.random.randint(10, size=(10, 10)), np.random.randint(10, size=(10, 10))
a, b, i, j = 5, 6, 4, 2

A + B  # somme
3 * A   # produit
np.dot(A, B)  # produit de A par B
A.dot(B)  # produit de A par B

alg.inv(A)  # renvoie l'inverse de A si inversible, sinon renvoie un message d'erreur
alg.matrix_rank(A)  # rang(A), le rang d'une matrice
alg.matrix.power(A, n)  # A^n, A puissance n
np.transpose(A)  # A^T, transposée de A
A.T  # A^T, transposée de A
