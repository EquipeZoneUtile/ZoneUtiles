import sys

from matplotlib import pyplot as plt
sys.path.append('./src')  # Remplacez cela par le chemin réel de votre dossier contenant la classe
from tkinter import Tk, filedialog
from point import Point
from setOfPoint import SetOfPoint
from contour import edges
import cv2


def main():
    path = filedialog.askopenfilename()
    seuil = int(input('Seuil :')) or 250
    edges_image = edges(path, seuil)
    liste_point = ExtractionPoint(edges_image, 3)
    print(liste_point)  


def ExtractionPoint(edges_image, reduction : int = 1):
    '''
    Prend en entrée une image représentant des contours et renvoie une liste de Points correspondant
    '''

    Liste_Point = []
    
    for index_row, row in enumerate(edges_image[::-1]) :
        if index_row % reduction == 0 :
            for index_column, pixel in enumerate(row):
                if index_column % reduction == 0:
                    if pixel == 0 :
                        Liste_Point += [Point(index_column, index_row)]

    return Liste_Point


if __name__ == '__main__':
    main()