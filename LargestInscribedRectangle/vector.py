from point import Point
import math as mt
from icecream import ic

class Vector:

    def __init__(self, A : Point, B : Point) -> None:
        self.x = B.x_coordinate - A.x_coordinate
        self.y = B.y_coordinate - A.y_coordinate
    
    def get_norm(self):
        return mt.sqrt(self.x**2 + self.y**2)
    
    def dot_product(self, v):
        return self.x * v.x + self.y * v.y
    
    def cross_product(self, v):
        return self.x * v.y - self.y * v.x
    
    def angle(self, v):
        dot = self.dot_product(v)
        cross = self.cross_product(v)
        angle = mt.acos(dot/(self.get_norm() * v.get_norm()))*180/mt.pi - 90
        ic(dot, angle, cross)
        if cross < 0:
            angle = - angle
        
        return angle