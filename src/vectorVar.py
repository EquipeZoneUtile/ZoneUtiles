from icecream import ic 
from pointVar import PointVar
from pychoco import Model
from maxValue import MAX_VALUE

class VectorVar:

    def __init__(self, A : PointVar, B : PointVar) -> None:
        self.x = B.x - A.x
        self.y = B.y - A.y
        self.model = A.model
    
    def get_squared_norm(self):
        x2 = self.model.intvar(0, MAX_VALUE**2)
        y2 = self.model.intvar(0,  MAX_VALUE**2)
        self.model.times(self.x, self.x, x2).post()
        self.model.times(self.y, self.y, y2).post()
        return x2 + y2