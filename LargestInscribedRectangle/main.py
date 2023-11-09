from pychoco import Model
from icecream import ic
import matplotlib.pyplot as plt
from rectangleVar import RectangleVar
from convexPolygon import ConvexPolygon
from rectangle import Rectangle
from point import Point
from pointVar import PointVar
from maxValue import MAX_VALUE
import time

'''
En partant d'un set de point formant un polygone convexe, on cherhce a obtenir le rectangle inscrit de plus grand aire

On utlisera pychco et la programmation par contrainte pour résoudre le problème
'''

NBR_SOMMETS = 4
DIMENSION = 2

def affichage(rectangle : Rectangle, polygon : ConvexPolygon):
    fig, ax = plt.subplots()
    boundaries = polygon.get_boundaries(2)
    ax.set_xlim(boundaries[0])
    ax.set_ylim(boundaries[1])
    ax.set_aspect('equal')
    ax.add_patch(rectangle.get_geometric('red'))
    polygon.display(ax, 'green')
    plt.show()


model = Model()
# Données 

convexPolygon = ConvexPolygon([Point(0, 0), Point(0, 10), Point(6, 20), Point(20, 20), Point(34, 18), Point(40, 10), Point(20, 0)])

# Variables

coords = model.intvars(NBR_SOMMETS * DIMENSION, 0, convexPolygon.get_maximum_value())
A = PointVar(coords[0], coords[1])
B = PointVar(coords[2], coords[3])
C = PointVar(coords[4], coords[5])
D = PointVar(coords[6], coords[7])

rectangle = RectangleVar(A, B, C, D)

# Contraintes

for point in rectangle.points:
    convexPolygon.post_contraints(model, point)
    point

rectangle.post_constraints()

# Résolution 
ax, ay, bx, by, cx, cy, dx, dy = tuple(rectangle.get_vars())
solver = model.get_solver()
solver.set_input_order_lb_search(ax, ay, bx, by, cx, cy, dx, dy)
maxi = rectangle.get_squared_area()
start = time.perf_counter()
solutions = [solver.find_optimal_solution(maxi, True)]
solving_time = time.perf_counter() - start
ic(solving_time)
#solutions = solver.find_all_solutions()
# Affichage
for solution in solutions:
    ic(solution)
    if solution :
        rectangle_solution = rectangle.solution(solution)
        print(str(rectangle_solution))
        affichage(rectangle_solution, convexPolygon)
        



