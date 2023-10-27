import numpy as np
from icecream import ic
import matplotlib.pyplot as plt
from rectangle import Rectangle
from setOfPoint import SetOfPoint
from point import Point
import random as rd


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


def display_result(results, base_rectangle : Rectangle, set_of_points : SetOfPoint):
    final_rectangle, solving_time = results
    ic(final_rectangle, solving_time)
    figure, axis = plt.subplots()
    axis.set_aspect('equal')
    axis.set_xlim(base_rectangle.left_boundary - 1, base_rectangle.right_boundary + 1)
    axis.set_ylim(base_rectangle.bottom_boundary - 1, base_rectangle.top_boundary + 1)
    axis.add_patch(base_rectangle.get_geometric("black"))
    axis.add_patch(final_rectangle.get_geometric("red"))
    set_of_points.display(axis)

    plt.show()


def random_set_of_point(n, base_rectangle : Rectangle):
    set_of_point = []
    for i in range(n):
        set_of_point += [Point(rd.randint(base_rectangle.left_boundary, base_rectangle.right_boundary),
                    rd.randint(base_rectangle.bottom_boundary, base_rectangle.top_boundary))]
    return SetOfPoint(set_of_point)