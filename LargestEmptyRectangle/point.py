import matplotlib.pyplot as plt

class Point:
    def __init__(self, x : int, y: int):
        self.x_coordinate = x
        self.y_coordinate = y


    def __str__(self) -> str:
        return f"Point : ({self.x_coordinate}; {self.y_coordinate})"


    def __hash__(self) -> int:
        return hash((self.x_coordinate, self.y_coordinate))


    def __eq__(self, __value: object) -> bool:
        return (self.x_coordinate == __value.x_coordinate) and (self.y_coordinate == __value.y_coordinate)


    def get_geometric(self, size):

        '''
        Renvoie l'objet matplotlib associé au point
        '''
        
        return plt.Circle((self.x_coordinate, self.y_coordinate), size, color="black")


    
    

