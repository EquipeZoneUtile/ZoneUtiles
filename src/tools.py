import numpy as np
from icecream import ic
import matplotlib.pyplot as plt
from rectangle import RectangleBoundary
from setOfPoint import SetOfPoint
from point import Point
import random as rd
import cv2

def max_gap(liste):
    """
    input : list of int
    output : the maximum gap between two elements
    
    """
    gaps = {}
    liste = sorted(liste, reverse= True)
    for index, value in enumerate(liste[: - 1]):
        gaps[value, liste[index + 1]] = value - liste[index + 1]
        
    key_max=max(gaps, key=gaps.get)
    return (gaps[key_max], key_max)


def display_result(results : tuple[RectangleBoundary, float], base_rectangle : RectangleBoundary,
                    set_of_point : SetOfPoint, path : str | None = None):
    final_rectangle, solving_time = results
    ic(final_rectangle.get_area(), solving_time)
    figure, axis = plt.subplots(1, 2)
    ic(axis)
    axis[0].set_aspect('equal')
    axis[0].set_xlim(base_rectangle.left_boundary - 1, base_rectangle.right_boundary + 1)
    axis[0].set_ylim(base_rectangle.bottom_boundary - 1, base_rectangle.top_boundary + 1)
    axis[0].add_patch(base_rectangle.get_geometric("black"))
    axis[0].add_patch(final_rectangle.get_geometric("red"))
    set_of_point.display(axis[0])
    if path:

        plt.subplot(122)
        plt.imshow(cv2.imread(path))
        axis[1].add_patch(final_rectangle.get_geometric_imshow(base_rectangle.top_boundary, "red"))
    plt.show()


def random_set_of_point(n, base_rectangle : RectangleBoundary):
    set_of_point = []
    for i in range(n):
        set_of_point += [Point(rd.randint(base_rectangle.left_boundary, base_rectangle.right_boundary),
                    rd.randint(base_rectangle.bottom_boundary, base_rectangle.top_boundary))]
    return SetOfPoint(set_of_point)