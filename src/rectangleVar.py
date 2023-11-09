from pychoco import Model
from icecream import ic
from pointVar import PointVar
from vectorVar import VectorVar
from pychoco.variables.variable import Variable
from pychoco.solution import Solution
from rectangle import RectanglePoint
from maxValue import MAX_VALUE
from pychoco.variables.intvar import IntVar


class RectangleVar:

    def __init__(self, A : PointVar, B : PointVar, C : PointVar, D : PointVar) -> None:
        self.model = A.model
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.points = [A, B, C, D]
    
    
    
    def post_constraints(self):
        """
        Créer les contraintes pour forcer ABCD à être un rectangle
        """

        post_perpendicular_constraint(self.model, self.D, self.A, self.B)
        post_perpendicular_constraint(self.model, self.A, self.B, self.C)
        post_perpendicular_constraint(self.model, self.B, self.C, self.D)
        post_perpendicular_constraint(self.model, self.C, self.D, self.A)

    
    def get_squared_area(self) -> Variable:
        """
        Renvoie l'aire du rectangle sous forme d'un IntVar
        """
        height = VectorVar(self.A, self.B).get_squared_norm()
        width = VectorVar(self.B, self.C).get_squared_norm()
        area = self.model.intvar(0, MAX_VALUE**4)
        self.model.times(height, width, area).post()
        return area
    
    def solution(self, solution: Solution):
        
        A, B, C, D = (p.solution(solution) for p in self.points)
        
        return RectanglePoint(A, B, C, D)
    
    def get_vars(self) -> list[IntVar]:

        '''
        Renvoie une liste de tous les intVar qui définissent le rectangle
        '''

        vars = []
        for point in self.points:
            vars += point.get_vars()
        return vars

        


    



def post_perpendicular_constraint(model: Model, A : PointVar, B : PointVar, C : PointVar) -> None:
    
    """
    Crée les contraintes pour forcer AB normal à BC
    """

    x1, y1 = B.x - A.x, B.y - A.y
    x2, y2 = C.x - B.x, C.y - B.y
    model.arithm(x1 * x2 + y1 * y2, "=", 0).post()
    pass
