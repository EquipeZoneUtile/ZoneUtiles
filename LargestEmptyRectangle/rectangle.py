import matplotlib.pyplot as plt

class Rectangle:
    def __init__(self, top : int, bottom : int, left : int, right: int) -> None:
        self.top_boundary = top
        self.bottom_boundary = bottom
        self.left_boundary = left
        self.right_boundary = right
    
    def __str__(self) -> str:
        resultat = ""
        resultat += f"Rectangle : l = {self.left_boundary}, r = {self.right_boundary}, t = {self.top_boundary}, b = {self.bottom_boundary} \n"
        resultat += f"Area : A = {self.get_area()}"
        return resultat
    
    def get_area(self) :
        return (self.top_boundary - self.bottom_boundary) * (self.right_boundary - self.left_boundary)
    
    def get_height(self):
        return self.top_boundary - self.bottom_boundary
    
    def get_width(self):
        return self.right_boundary - self.left_boundary
    
    def get_geometric(self, color):
        return plt.Rectangle((self.left_boundary, self.bottom_boundary), self.get_width(), self.get_height(), fill=False, color=color)
    
