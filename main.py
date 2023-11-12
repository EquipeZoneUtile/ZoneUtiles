import sys
sys.path.append('src')
sys.path.append('EdgeDetection')

from icecream import ic
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
from MerAlgo1 import merAlgo1
from rectangle import RectangleBoundary
from setOfPoint import SetOfPoint
from contour import edges
from tableaupoint import ExtractionPoint
import tools

root = tk.Tk()
root.withdraw()

path_image = filedialog.askopenfilename() # On charge l'image à traiter
seuil = int(input('Seuil : ') or 250) # On deamande le seuil de detection de contour
reduction = int(input('Reduction : ') or 2) # On demande le facteur de réduction du nombre de points

edges_image = edges(path_image, seuil)
set_of_point = SetOfPoint(ExtractionPoint(edges_image, reduction))
top_boundary = len(edges_image) # On mesure la hauteur de l'image
right_boundary = len(edges_image[0]) # On mesure la largeur de l'image
base_rectangle = RectangleBoundary(top_boundary, 0, 0, right_boundary)  # On initialise le rectangle 
                                                                        # dans lequel va se dérouler la résolution

# Résolution :
results = merAlgo1(base_rectangle, set_of_point)


# Affichage des résultats

tools.display_result(results, base_rectangle, set_of_point, path_image)