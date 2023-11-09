from pychoco import Model
from icecream import ic
from pychoco.variables.variable import Variable
from pychoco.solution import Solution
from point import Point

class PointVar:

    def __init__(self, x : Variable, y : Variable) -> None:
        self.x = x
        self.y = y
        self.model = x.model

    def solution(self, solution : Solution):
        return Point(solution.get_int_val(self.x), solution.get_int_val(self.y))
    
    def get_lenth(self):
        return self.x + self.y
    
    def get_vars(self):
        return [self.x, self.y]
