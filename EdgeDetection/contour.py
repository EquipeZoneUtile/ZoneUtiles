import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog


def main():
    root = Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    plt.subplot(121)
    plt.imshow(cv2.imread(path))
    plt.subplot(122)
    plt.imshow(edges(path, 250), cmap='grey')
    plt.show()


def edges(path : str, seuil : int = 50) -> list[list]:
    '''
    Réalise la détection de contour de l'image dont le chemin d'accès est path
    le paramètre seuil réprésente la précision de la détection.
    Si il y a du bruit sur le résultat il faut ausgmenter le seuil
    Si les contours ne sont pas détectés, il faut baisser le paramètre
    '''
    # Charger l'image en niveaux de gris
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
    main()

