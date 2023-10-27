import tools
from rectangle import Rectangle
import matplotlib.pyplot as plt
from point import Point
from setOfPoint import SetOfPoint
from icecream import ic
import time
import statistics
TOP_BOURNDARY = 1000
BOTTOM_BOUNDARY = 0
LEFT_BOUNDARY = 0
RIGHT_BOUNDARY = int(1000 * 16 / 9)
base_rectangle = Rectangle(TOP_BOURNDARY, BOTTOM_BOUNDARY, LEFT_BOUNDARY, RIGHT_BOUNDARY)
NUMBER_OF_POINTS = 200
set_of_point = tools.random_set_of_point(NUMBER_OF_POINTS, base_rectangle)

base_rectangle = Rectangle(TOP_BOURNDARY, BOTTOM_BOUNDARY, LEFT_BOUNDARY, RIGHT_BOUNDARY)
def main():
    results = merAlgo1(base_rectangle, set_of_point)
    tools.display_result(results, base_rectangle, set_of_point)

def merAlgo1(base_rectangle, set_of_point):
    
    actual_rectangle = Rectangle(0, 0, 0, 0)

    

    start = time.perf_counter()
    # Calcul de la plus grand aire de départ (type 1 vertical)
    maximum_gap = tools.max_gap([base_rectangle.left_boundary, base_rectangle.right_boundary] +
                                set_of_point.get_x_coordinates())
    
    maximum_area = maximum_gap[0] * base_rectangle.get_height()
    final_rectangle = Rectangle(base_rectangle.top_boundary, base_rectangle.bottom_boundary, min(maximum_gap[1]), max(maximum_gap[1]))

    # Sort S according to the Y coordinates of the points in descending order
    set_of_point.sort_points("y_coordinate", True)

    for p_index, point in enumerate(set_of_point.points):
        actual_rectangle.left_boundary = base_rectangle.left_boundary
        actual_rectangle.right_boundary = base_rectangle.right_boundary

        for point_ in set_of_point.points[p_index + 1:]:
            if (actual_rectangle.left_boundary < point_.x_coordinate and point_.x_coordinate < actual_rectangle.right_boundary):

                actual_area = actual_rectangle.get_width() * (point.y_coordinate - point_.y_coordinate)
                if maximum_area < actual_area:
                    maximum_area = actual_area
                    final_rectangle = Rectangle(point.y_coordinate, point_.y_coordinate,
                                                actual_rectangle.left_boundary, actual_rectangle.right_boundary)
                    
                if point_.x_coordinate > point.y_coordinate:
                    actual_rectangle.right_boundary = point_.x_coordinate
                else :
                    actual_rectangle.left_boundary = point_.x_coordinate
        # Type 3 triangles ()
        actual_area = actual_rectangle.get_width() * (point.y_coordinate - base_rectangle.bottom_boundary)
        if maximum_area < actual_area:
            maximum_area = actual_area
            final_rectangle = Rectangle(point.y_coordinate, base_rectangle.bottom_boundary, 
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
            final_rectangle = Rectangle(base_rectangle.top_boundary, point.y_coordinate, max_left, min_right)
    end = time.perf_counter()
    temps_de_calcul = end - start
    return final_rectangle, temps_de_calcul


if __name__ == "__main__":
    main()

