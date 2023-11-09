from icecream import ic
from pointVar import PointVar
from point import Point
from pychoco import Model
from vector import Vector


class ConvexPolygon:
    def __init__(self, points: list) -> None:
        self.points = points
        self.size = len(points)

    def __str__(self) -> str:
        resultat = ''
        resultat += f'polygone à {self.size} côtés :\n'
        for point in self.points:
            resultat += str(point)
        return resultat

    
    
    def post_contraints(self, model : Model, P : PointVar):
        """
        Créé les contraintes pour que le point P soit à l'intérieur du polygone
        """
        for index in range(self.size):
            index_ = int((index + 1)%self.size)
            self.post_under_segment_contraint(model, self.points[index_], self.points[index], P)

    def get_maximum_value(self) -> int :
        liste = [p.x_coordinate for p in self.points] + [p.y_coordinate for p in self.points]
        return max(liste)
    
    def post_under_segment_contraint(self, model : Model, A : Point, B : Point, P : PointVar):
        """
        Créé la contrainte qui force P à être \'sous\' la droite (AB)
        (être au-dessus de (AB) revient à être \'sous\' (BA))
        """
        AB = Vector(A, B)
        max_area = self.get_maximum_value() ** 2
        x = model.intvar(-max_area, max_area)
        model.times(P.x, AB.y, x).post()

        y = model.intvar(-max_area, max_area)
        model.times(P.y, -AB.x, y).post()

        z = A.x_coordinate * B.y_coordinate - B.x_coordinate * A.y_coordinate
        
        model.arithm(x + y, "<=", z).post()
    
    def get_boundaries(self, marge):
        '''
        Renvoie les bornes [(xmin, xmax), (ymin, ymax)] du polygone
        La marge s'ajoute (ou se soustrait) aux bornes
        '''
        xs = [p.x_coordinate for p in self.points]
        ys = [p.y_coordinate for p in self.points]
        xmin, xmax = min(xs) - marge, max(xs) + marge
        ymin, ymax = min(ys) - marge, max(ys) + marge
        return [(xmin, xmax), (ymin, ymax)]
    
    def display(self, axis, color):
        xs = [p.x_coordinate for p in self.points]
        ys = [p.y_coordinate for p in self.points]
        axis.fill(xs, ys, color=color, alpha=0.2)

    




    