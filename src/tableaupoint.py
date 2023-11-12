import sys
sys.path.append('./LargestEmptyRectangle')  # Remplacez cela par le chemin réel de votre dossier contenant la classe

from point import Point
from contour import edges
import cv2
import os

chemin_gruyere = os.path.join("test_image", "gruyere.jpg")


 # Charge l'image en niveaux de gris

def ExtractionPoint(edges_image, reduction : int = 2):

    
    Liste_Point = []
    

    for index_row, row in enumerate(edges_image[::-1]) :
        if index_row % reduction == 0 :
            for index_column, pixel in enumerate(row):
                if index_column % reduction == 0:
                    if pixel == 0 :
                        Liste_Point += [Point(index_column, index_row)]

    return Liste_Point

if __name__ == '__main__':
    chemin_gruyere = os.path.join("test_image", "gruyere.jpg")
    edges_gruyere = edges(chemin_gruyere, 50)
    liste_point = ExtractionPoint(edges_gruyere, 2)
    print(len(liste_point))
    print(liste_point)