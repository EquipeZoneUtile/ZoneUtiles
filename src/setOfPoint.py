from operator import attrgetter
from icecream import ic
import numpy as np
import matplotlib.pyplot as plt
from point import Point

class SetOfPoint:
    def __init__(self, list_of_points : list[Point]) -> None:
        self.points = list_of_points
        
    def __str__(self) -> str:
        resultat = "Set de point : \n"
        for point in self.points:
            resultat += str(point)
            resultat += ";\n"
        return resultat
        
    def get_x_coordinates(self) -> list[int]:
        return [p.x_coordinate for p in self.points]
    
    def get_y_coordinates(self) -> list[int]:
        return [p.y_coordinate for p in self.points]

    def sort_points(self, coordinate : str, direction = False) -> None:
        """
        Ordonne les points de l'ensemble de point

        Args:

            coordinate (str) : Clé de triage  ('x_coordinate' or 'y_coordinate')
            direction (bool) : False pour trier en ordre croissant
        
        """
        self.points = sorted(self.points, key = attrgetter(coordinate), reverse= (direction))
        pass

    def get_max(self, coordinate) -> int:
        '''Renvoie la plus grande abscisse/ordonnée de l'ensemble de points'''
        return max(self.points, key = attrgetter(coordinate))
    
    def get_min(self, coordinate) -> int:
        '''Renvoie la plus petite abscisse/ordonnée de l'ensemble de points'''
        return min(self.points, key = attrgetter(coordinate))


    def display(self, ax) -> None:
        for point in self.points:
            ax.add_patch(point.get_geometric((ax.get_xlim()[1] - ax.get_xlim()[0])/500))
        pass





