import cv2
import matplotlib.pyplot as plt
import os




# Charger l'image en niveaux de gris
  # Charge l'image en niveaux de gris
#gruyere est un tableau numpy de taille (hauteur x largeur) de l'image qui représente les pixels
#les pixels ont une valeur entre 0 et 255 qui représente le niveau de gris


def edges(path, seuil : int = 250):
    '''
    retourne un tableau numpy qui correspond aux contours de image
    '''

    image = cv2.imread(path, 0)
    # Appliquer la détection de contours avec Canny
    edges_image = cv2.Canny(image, seuil, seuil) 
    #le premier seuil élimine lespixel dont gradient lui est inférieur : le bruit
    #le second classe ceux dont le gradient lui est supérieu en contour-fort
    #entre les deux ce sont les contours-faible

    # Inverser les couleurs pour afficher les contours en noir
    edges_image = cv2.bitwise_not(edges_image)

    # Binariser l'image pour avoir les contours en noir et le reste en blanc
    ret, edges_image = cv2.threshold(edges_image, 0, 255, cv2.THRESH_BINARY)
    
    return edges_image




if __name__ == '__main__':
    chemin_gruyere = os.path.join("test_image", "gruyere.jpg")
    edges_gruyere = edges(chemin_gruyere, 50)
    # Afficher l'image binarisée (contours noirs, fond blanc)
    plt.imshow(edges_gruyere, cmap='gray')
    plt.axis('off')
    plt.show()



