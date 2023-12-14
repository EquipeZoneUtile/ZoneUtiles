import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x : int, y: int):
        self.x_coordinate = x
        self.y_coordinate = y


    def __str__(self) -> str:
        return f"Point : ({self.x_coordinate}; {self.y_coordinate})"


    def __hash__(self) -> int:
        return hash((self.x_coordinate, self.y_coordinate))


    def __eq__(self, __value: object) -> bool:
        return (self.x_coordinate == __value.x_coordinate) and (self.y_coordinate == __value.y_coordinate)


    def set(self, point : object):
            self.x_coordinate = point.x_coordinate
            self.y_coordinate = point.y_coordinate
        
    def get_geometric(self, size, color : str = 'black'):

        '''
        Renvoie l'objet matplotlib associé au point
        '''
        
        return plt.Circle((self.x_coordinate, self.y_coordinate), size, color=color)
    

    def distance(self, __value : object) -> float:
        '''
        Renvoie la distance entre les deux points
        '''

        return math.sqrt((self.x_coordinate - __value.x_coordinate)**2 + (self.y_coordinate - __value.y_coordinate)**2)

    
    

