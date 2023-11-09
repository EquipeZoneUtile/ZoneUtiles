import cv2
import matplotlib.pyplot as plt

# Charger l'image en niveaux de gris
gruyere = cv2.imread('C:\\Users\\Baptiste\\Documents\\IMT\\Projet Commande Entreprise\\ZoneUtiles\\EdgeDetection\\gruyere.jpg', 0)  # Charge l'image en niveaux de gris
#gruyere est un tableau numpy de taille (hauteur x largeur) de l'image qui représente les pixels
#les pixels ont une valeur entre 0 et 255 qui représente le niveau de gris


def edges(image):
    # Appliquer la détection de contours avec Canny
    edges_image = cv2.Canny(image,50,50) 
    #le premier seuil élimine les grandient qui lui sont inférieur

    # Inverser les couleurs pour afficher les contours en noir
    edges_image = cv2.bitwise_not(edges_image)

    # Binariser l'image pour avoir les contours en noir et le reste en blanc
    ret, edges_image = cv2.threshold(edges_image, 0, 255, cv2.THRESH_BINARY)
    
    return edges_image


edges_gruyere=edges(gruyere)

# Afficher l'image binarisée (contours noirs, fond blanc)
plt.imshow(edges_gruyere, cmap='gray')
plt.axis('off')
plt.show()

