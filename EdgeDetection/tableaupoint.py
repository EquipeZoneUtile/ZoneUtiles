import sys
sys.path.append('./LargestEmptyRectangle')  # Remplacez cela par le chemin réel de votre dossier contenant la classe

from point import Point
from contour import edges
import cv2

gruyere = cv2.imread('C:\\Users\hmm26\\OneDrive\\Bureau\\IMT_2023_2024\\projet_commande_entrprise\\ZoneUtiles\\EdgeDetection\\gruyere.jpg', 0)  # Charge l'image en niveaux de gris

def ExtractionPoint(image):

    edges_image = edges(image)
    
    Liste_Point = []
    

    for index_row, row in enumerate(edges_image[::-1]) :
        if index_row % 3 == 0 :
            for index_column, pixel in enumerate(row):
                if index_column % 3 == 0:
                    if pixel == 0 :
                        Liste_Point += [Point(index_column, index_row)]

    return Liste_Point

if __name__ == '__main__':
    liste_point = ExtractionPoint(gruyere)
    print(len(liste_point))
    print(liste_point)