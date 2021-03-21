"""TP 6 : images"""

"""Pour l'ordi, c'est une matrice et un pixel = qq chose qui représente la couleur :
- NB : 0 ou un 1
- gros : un nombre entre 0 et 1
- couleur : un triplet (R,G,B)
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

n, p = 100, 100
i, j = 10, 5
value = 120
"""
mon_image = Image.new("RGB",(n,p),(255,255,255))

# mon_image = Image.open("pie.png")
"""

"""
image = np.zeros((p,n), dtype = np.uint8)
image = np.zeros((n, p, 3), dtype=np.uint8)
# n : nombre de lignes
# p : nombre de colonnes
# 3 : nombre d'éléments dans le tuple

image = 150*np.ones((n, p, 3), dtype=np.uint8)

image[i, j] = [200, 10, 10]  # change la couleur du pixel en position i, j
image[i, j, 0] = value  # change la première composante donc le rouge

plt.imshow(image)  # tracer l'image
plt.axis('off') # retirer les axes
plt.show()
"""

def draw(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def E1a():
    # 05, 20, 64
    # 236, 25, 32
    n, p = 1, 3
    image = np.zeros((n, p, 3), np.uint8)
    image[0, 0] = [5, 20, 64]
    image[0, 1] = [255, 255, 255]
    image[0, 2] = [236, 25, 32]
    return image

def E1b():
    blue = [236, 25, 32]
    white = [255, 255, 255]
    red = [5, 20, 64]
    n, p = 800, 1200
    image = np.zeros((n, p, 3), np.uint8)
    for i, el in enumerate(image):
        for j, _ in enumerate(el):
            q = p//3
            color = white
            if j < q:
                color = blue
            elif q < j < 2*q:
                color = white
            elif j > q:
                color = red
            image[i, j] = color
    return image

def E1c():
    blue = [236, 25, 32]
    white = [255, 255, 255]
    red = [5, 20, 64]
    n, p = 800, 1200
    size = [n, p//3, 3]
    A = blue*np.ones(size)
    B = white*np.ones(size)
    C = red*np.ones(size)
    image = np.concatenate((A, B, C), axis=1)
    return image

def ouvre():
    """ouvre l'image"""
    return np.uint8(plt.imread("pie.png")*255)

# négatif : parcours tous les pixels et remplace chaque couleur ou alors :
def negatif(image):
    return -image

def art(image):
    return abs(30*np.ones(image.shape, np.uint8) - image)

draw(negatif(ouvre()))