


import math
from icecream import ic 
from matplotlib import pyplot as plt
import numpy as np
from point import Point

def main():
    c = Outline([Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)])
    d = Outline([Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)])
    ic(hash(c), hash(d))
    dic = {c : 1}
    
    c.densify(1)
    ic(dic[d])
    
class Outline:


    def __init__(self, points : list[Point]):

        self.points = points
        self.__base_points = points.copy()
    
    def __hash__(self) -> int:
        coordinates = np.array([[point.x_coordinate, point.y_coordinate] for point in self.__base_points])
        coordinates = coordinates.flatten()
        return hash((x for x in coordinates))
    

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Outline):
            return self.__base_points == __value.__base_points
        return False
    
    def densify(self, precision : float):
        '''
        Densifie le contour en ajoutant des points dans les segments trop grands
        '''

        nb = len(self.points)
        pairs = [(self.points[i], self.points[(i + 1)%nb]) for i in range(nb)]

        for index, (p1, p2) in enumerate(pairs):
            distance = p1.distance(p2)
            if distance > precision:
                nb_points_ajouter = math.ceil(distance / precision)
                self.__ajouter_points(p1, p2, nb_points_ajouter, index)
    

    def __ajouter_points(self, p1 : Point, p2 : Point, nb_points : int, index : int):
        '''
        Ajouter nb_points points sur le segment [p1, p2]
        '''

        dx = (p2.x_coordinate - p1.x_coordinate) / nb_points
        dy = (p2.y_coordinate - p1.y_coordinate) / nb_points

        xs = [p1.x_coordinate + i * dx for i in range(1, nb_points)]
        ys = [p1.y_coordinate + i * dy for i in range(1, nb_points)]

        points_ajouter = [Point(x, y) for x, y in zip(xs, ys)]

        for i, point in enumerate(points_ajouter):
            self.points.insert(index + i, point)


    def get_pointers(self):
        '''
        Renvoie un dictionnaire contenant les pointeurs de chanque point vers le contour
        '''

        return {point: self for point in self.points}

    def display(self, ax, color = 'black') -> None:
        for point in self.points:
            ax.add_patch(point.get_geometric((ax.get_xlim()[1] - ax.get_xlim()[0])/500, color=color))
        pass

if __name__ == '__main__':
    main()

