def inversion(image_origine):
    image=np.copy(image_origine)
    nb_lignes,nb_colonnes,_ = image.shape
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            image[i,j,0]=255-image[i,j,0]
            image[i,j,1]=255-image[i,j,1]
            image[i,j,2]=255-image[i,j,2]
    return image