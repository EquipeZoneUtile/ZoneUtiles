from rectangle import RectanglePoint
from point import Point
from convexPolygon import ConvexPolygon
import matplotlib.pyplot as plt

convexPolygon = ConvexPolygon([Point(0, 0), Point(0, 5), Point(3, 10), Point(10, 10), Point(20, 5), Point(10, 0)])
rectangle = RectanglePoint(Point(2, 0), Point(1, 6), Point(13, 8), Point(14, 2))

fig, ax = plt.subplots()
ax.add_patch(rectangle.get_geometric('red'))
convexPolygon.display(ax, 'green')
ax.set_aspect('equal')
plt.show()