import sys
sys.path.append('src')
from contour import edges
from tableaupoint import ExtractionPoint
from semiDynamicHeap import SDH
import tools
from rectangle import RectangleBoundary
import matplotlib.pyplot as plt
from point import Point
from setOfPoint import SetOfPoint
from icecream import ic
import time


def merAlgo2(base_rectangle : RectangleBoundary, set_of_point : SetOfPoint
             ) -> tuple[RectangleBoundary, float]:
    
    actual_rectangle = RectangleBoundary(0, 0, 0, 0)

    

    start = time.perf_counter()
    # Calcul de la plus grand aire de départ (type 1 vertical)
    maximum_gap = tools.max_gap([base_rectangle.left_boundary, base_rectangle.right_boundary] +
                                set_of_point.get_x_coordinates())
    
    maximum_area = maximum_gap[0] * base_rectangle.get_height()
    final_rectangle = RectangleBoundary(base_rectangle.top_boundary, base_rectangle.bottom_boundary, min(maximum_gap[1]), max(maximum_gap[1]))
    
    # Step 3 #
    heap = SDH(set_of_point)
    # Step 4 #
    for _ in range(set_of_point.lenth):
        ic("for")
        # Step 5 #
        actual_rectangle.left_boundary = base_rectangle.left_boundary
        actual_rectangle.right_boundary = base_rectangle.right_boundary
        point = Point(0, base_rectangle.top_boundary)
        # Step 6 #
        point_ref = heap.delete()

        # Step 7 #
        while point.y_coordinate != base_rectangle.bottom_boundary:
            
            point.set(heap.find(actual_rectangle, base_rectangle))
            ic(str(point))
            actual_area = actual_rectangle.get_width() * (point_ref.y_coordinate - point.y_coordinate)
            maximum_area = max(maximum_area, actual_area)
            if actual_area == maximum_area:
                final_rectangle = RectangleBoundary(point.y_coordinate, point_ref.y_coordinate,
                                                       actual_rectangle.left_boundary, actual_rectangle.right_boundary)
            if point.x_coordinate > point_ref.x_coordinate:
                actual_rectangle.right_boundary = point.x_coordinate
            else:
                actual_rectangle.left_boundary = point.x_coordinate
    
    # Step 8 #
    set_of_point.sort_points('x_coordiantes', False)
    lx = set_of_point.get_x_coordinates()
    next = {lx[index - 1] : set_of_point.points[index] for index in range(1, len(lx))}
    next[lx[-1]] = None
    before = {lx[index + 1] : set_of_point.points[index] for index in range(len(lx) - 1)}
    before[lx[0]] = None

    set_of_point.sort_points('y_coordinates', False)
    ly = set_of_point.get_y_coordinates()
    pyx = {y : p for y, p in zip(ly, set_of_point.points) }

    # Step 9 #
    for y in range(len(ly)):
        x = pyx[y]
        # Step 10 #
        right = next[x]
        # Step 11 #
        left = before[x]
        # Step 12 #
        actual_area = (right - left) * (base_rectangle.top_boundary - y)
        maximum_area = max(maximum_area, (right - left) * (base_rectangle.top_boundary - y))
        if actual_area == maximum_area:
            final_rectangle = RectangleBoundary(base_rectangle.top_boundary, y, left, right)
        # Step 13 #
        next[before[x]], before[next[x]] = before[x], next[x]
        lx.remove(x)
        ly.remove(y)

    end = time.perf_counter()
    temps_execution = end - start
    return final_rectangle, temps_execution

if __name__ == "__main__":
    '''path_image ="C:/Users/Baptiste/Documents/IMT/Projet Commande Entreprise/ZoneUtiles/test_image/dessinautiste.jpg" # On charge l'image à traiter
    seuil = 250 # On deamande le seuil de detection de contour
    reduction = 4 # On demande le facteur de réduction du nombre de points

    edges_image = edges(path_image, seuil)
    set_of_point = SetOfPoint(ExtractionPoint(edges_image, reduction))
    top_boundary = len(edges_image) # On mesure la hauteur de l'image
    right_boundary = len(edges_image[0]) # On mesure la largeur de l'image'''

    set_of_point = SetOfPoint([Point(x,5) for x in range(1, 5)])
    top_boundary = 10
    right_boundary = 10
    base_rectangle = RectangleBoundary(top_boundary, 0, 0, right_boundary)  # On initialise le rectangle 
                                                                            # dans lequel va se dérouler la résolution

    # Résolution :
    #results = merAlgo1(base_rectangle, set_of_point)
    results = merAlgo2(base_rectangle, set_of_point)
    # Affichage des résultats
    ic(results)
    #tools.display_result(results, base_rectangle, set_of_point, path_image)











