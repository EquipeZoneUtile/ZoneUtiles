from operator import attrgetter
from icecream import ic
import numpy as np
import matplotlib.pyplot as plt

class SetOfPoint:
    def __init__(self, list_of_points) -> None:
        self.points = list_of_points
        
    def __str__(self) -> str:
        resultat = "Set de point : \n"
        for point in self.points:
            resultat += str(point)
            resultat += ";\n"
        return resultat
        
    def get_x_coordinates(self) :
        return [p.x_coordinate for p in self.points]
    
    def get_y_coordinates(self) :
        return [p.y_coordinate for p in self.points]

    def sort_points(self, coordinate : str, direction = False):
        """
        Sort the points of set of points

        Args:

            coordinate (str) : key of the sorting ('x_coordinate' or 'y_coordinate')
            direction (bool) : False for ascending sorting
        
        """
        self.points = sorted(self.points, key = attrgetter(coordinate), reverse= (direction))
        pass

    def display(self, ax):
        for point in self.points:
            ax.add_patch(point.get_geometric((ax.get_xlim()[1] - ax.get_xlim()[0])/500))
        pass





