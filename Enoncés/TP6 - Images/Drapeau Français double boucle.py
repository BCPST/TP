import matplotlib.pyplot as plt
import numpy as np

##
image = np.ones((50,90, 3),dtype = np.uint8)

for l in range(50):
    for c in range(90):
        if c < 31 :
            image[l,c,2]=255
        if c >= 31 and c < 61 :
            image[l,c]= 255
        if c >= 61 :
            image[l,c,0] = 255
plt.imshow(image)
plt.show()



##

