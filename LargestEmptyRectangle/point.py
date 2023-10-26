import matplotlib.pyplot as plt

class Point:
    def __init__(self, x : int, y: int):
        self.x_coordinate = x
        self.y_coordinate = y

    def __str__(self) -> str:
        return f"Point : ({self.x_coordinate}; {self.y_coordinate})"
    
    def get_geometric(self, size):
        return plt.Circle((self.x_coordinate, self.y_coordinate), size, color="black")
    