from point import Point
from vector import Vector
import numpy as np
import matplotlib.pyplot as plt
from icecream import ic 

class Rectangle:

    def __init__(self, A : Point, B : Point, C: Point, D: Point) -> None:
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.points = [A, B, C, D]


    def __str__(self) -> str:
        resultat = 'Rectangle : '
        resultat += f'A : {self.A}, B : {self.B}, C : {self.C}, D : {self.D} -'
        resultat += f'- Area : {self.get_area()}'
        return resultat
    

    def get_width(self):
        '''Renvoie la largeur du rectangle'''
        width = Vector(self.B, self.C).get_norm()
        return width
    
    def get_height(self): 
        '''renvoie la hauteur du rectangle'''
        height = Vector(self.A, self.B).get_norm()
        return height
    def get_area(self):
        '''Renvoie l'aire du rectangle'''
        height = self.get_height()
        width = self.get_width()
        return height * width
    
    def get_geometric(self, color):
        '''Renvoie l'objet matplotlib lié au rectangle'''
        AB = Vector(self.A, self.B)
        angle = np.arccos(AB.x/AB.get_norm())*180/np.pi
        ic(angle, AB.y)
        if AB.y < 0:
            angle = - angle
        rectangle = plt.Rectangle((self.A.x_coordinate, self.A.y_coordinate), self.get_height(), self.get_width(), angle=angle, rotation_point='xy', color=color, fill=False)
        return rectangle

        
    
    
