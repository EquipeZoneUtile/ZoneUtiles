import sys

sys.path.append('src')

from OutLine import Outline
import tools
from rectangle import RectangleBoundary
import matplotlib.pyplot as plt
from point import Point
from setOfPoint import SetOfPoint
from icecream import ic
import time
import statistics



def main():

    # Définir la taille de la plaque 
    TOP_BOURNDARY = 9.1
    BOTTOM_BOUNDARY = 0.9
    LEFT_BOUNDARY = 0.9
    RIGHT_BOUNDARY = 9.1

    NUMBER_OF_POINTS = 2000

    base_rectangle = RectangleBoundary(TOP_BOURNDARY, BOTTOM_BOUNDARY, LEFT_BOUNDARY, RIGHT_BOUNDARY)

    # Créer les contours
    c = Outline([Point(1, 1), Point(1, 2), Point(9, 2), Point(9, 1)])
    c2 = Outline([Point(1, 4), Point(1, 9), Point(9, 9), Point(9, 4)])
    i = Outline([Point(2, 5), Point(2, 8), Point(8, 8), Point(8, 5)])
    # ...

    # Le second parmètre un dictionnaire avec en clé les contours intérieurs 
    # et en objet la liste des contours interieurs de ce contour
  
    results = merAlgo(base_rectangle, {c : [], c2 : [i]})   
    tools.display_result(results[:2], base_rectangle, results[2])

def merAlgo(base_rectangle : RectangleBoundary, outlines : dict[Outline, list[Outline]]
             ) -> tuple[RectangleBoundary, float]:
    
    actual_rectangle = RectangleBoundary(0, 0, 0, 0)

    points = []
    pointers = {}
    precision = base_rectangle.get_area()**(0.5) / 100

    for outline, inlines in outlines.items():
        outline.densify(precision)
        points += outline.points
        pointers.update(outline.get_pointers(False))
        for inline in inlines:
            inline.densify(precision)
            points += inline.points
            pointers.update(inline.get_pointers(True, outline))
    

    
    
    
    set_of_point = SetOfPoint(points)

    start = time.perf_counter()
    # Calcul de la plus grand aire de départ (type 1 vertical)
    maximum_gap = tools.max_gap([base_rectangle.left_boundary, base_rectangle.right_boundary] +
                                set_of_point.get_x_coordinates())
    
    maximum_area = maximum_gap[0] * base_rectangle.get_height()
    final_rectangle = RectangleBoundary(base_rectangle.top_boundary, base_rectangle.bottom_boundary, min(maximum_gap[1]), max(maximum_gap[1]))

    # Sort S according to the Y coordinates of the points in descending order
    set_of_point.sort_points("y_coordinate", True)
    p1, p2, p3, p4 = (p for p in set_of_point.points[:4])
    for p_index, point in enumerate(set_of_point.points):
        p4 = point
        actual_rectangle.left_boundary = base_rectangle.left_boundary
        actual_rectangle.right_boundary = base_rectangle.right_boundary

        for point_ in set_of_point.points[p_index + 1:]:
            p3 = point_
            if (actual_rectangle.left_boundary < point_.x_coordinate and point_.x_coordinate < actual_rectangle.right_boundary):

                actual_area = actual_rectangle.get_width() * (point.y_coordinate - point_.y_coordinate)

                outside = not(((pointers[p1][0] == pointers[p2][0])) and 
                              ((pointers[p2][0] == pointers[p3][0])) and
                              ((pointers[p3][0] == pointers[p4][0])) and
                              ((pointers[p4][0] == pointers[p1][0])))

                # Si tous les points supports sont dans le même contour et c'est un contour intérieur
                in_inner = ((pointers[p1][1] == pointers[p2][1])  and pointers[p1][1] == pointers[p3][1] and pointers[p1][1] == pointers[p4][1]) and pointers[p1][1]

                if maximum_area < actual_area and (outside or in_inner):
                    maximum_area = actual_area
                    final_rectangle = RectangleBoundary(point.y_coordinate, point_.y_coordinate,
                                                actual_rectangle.left_boundary, actual_rectangle.right_boundary)
                    
                if point_.x_coordinate > point.y_coordinate:
                    actual_rectangle.right_boundary = point_.x_coordinate
                    p2 = point_
                else :
                    actual_rectangle.left_boundary = point_.x_coordinate
                    p1 = point_
        # Type 3 triangles ()
        actual_area = actual_rectangle.get_width() * (point.y_coordinate - base_rectangle.bottom_boundary)
        if maximum_area < actual_area:
            maximum_area = actual_area
            final_rectangle = RectangleBoundary(point.y_coordinate, base_rectangle.bottom_boundary, 
                                        actual_rectangle.left_boundary, actual_rectangle.right_boundary)
        # Type 3 triangles (top boundary)
        right_list = [base_rectangle.right_boundary] 
        left_list = [base_rectangle.left_boundary]

        for point_ in set_of_point.points[:p_index]:
            if point_.x_coordinate > point.x_coordinate:
                right_list += [point_.x_coordinate]
            if point_.x_coordinate < point.x_coordinate:
                left_list += [point_.x_coordinate]
        min_right = min(right_list)
        max_left = max(left_list)

        maximum_area = max(maximum_area, (max_left - min_right) * (base_rectangle.top_boundary - point.y_coordinate))
        actual_area = (max_left - min_right) * (base_rectangle.top_boundary - point.y_coordinate)
        if maximum_area < actual_area:
            maximum_area = actual_area
            final_rectangle = RectangleBoundary(base_rectangle.top_boundary, point.y_coordinate, max_left, min_right)
    end = time.perf_counter()
    computing_time = end - start
    return final_rectangle, computing_time, set_of_point


if __name__ == "__main__":
    main()

