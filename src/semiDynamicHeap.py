from point import Point
from setOfPoint import SetOfPoint
from icecream import ic
#from sol import SOL
import math as mt
import numpy as np
import time
class SDH:

    def __init__(self, points : SetOfPoint) -> None:
        points.sort_points('x_coordinate')
        self.points = points.points
        self.size = len(self.points)
        self.heigh = int(np.log2(self.size)) + 1
        self.lenth = 2 ** self.heigh
        self.heap, self.heap_index = self.contruct_heap()

    def contruct_heap(self) -> (list[int | Point], dict):

        '''
        Contruit le heap assicié à la liste de points
        '''

        heap = {}
        liste = [0] * self.lenth

        for index, point in enumerate(self.points):
            liste[index] = point

        ## Construction d'un binary heap
        total, l_max = self.lenth, int(self.lenth/2)
        while l_max:
            ligne = []
            for _ in range(l_max):
                total += 1
                ligne += [total]

            liste = ligne + liste
            l_max = int(l_max/2)
        
        for index, value in enumerate(liste):
            heap[value] = index       
        return liste, heap
    

    def get_sol(self, root : int) -> SetOfPoint:

        '''
        Renvoie l'ensemble des feuilles dépendant de root
        '''

        def get_childs(fathers : list):
            childs = []
            for father in fathers:
                l_son, r_son = self.lSon(father), self.rSon(father)
                if l_son:
                    childs += [l_son]
                if r_son:
                    childs += [r_son]
            return childs
        sol = [root]
        while self.get_line(sol[0]) < self.heigh:
            sol = get_childs(sol)
        return SetOfPoint(sol)
    
    
    def lElement(self, sol : SetOfPoint) -> int:

        '''
        Renvoie la plus petite abscice du sous-arbre sol
        '''

        return sol.get_min('x_coordinate')


    def rElement(self, sol: SetOfPoint) -> int:

        '''
        Renvoie la plus grande abscisse du sous-arbre sol
        '''

        return sol.get_max('x_coordinate')


    def father(self, vertice : int | Point):

        '''
        Renvoie le parent du sommet
        '''

        index = int((self.heap_index[vertice] - 1) / 2)
        return self.heap[index]
    

    def lSon(self, vertice : int | Point):

        '''
        Renvoie le fils gauche du sommet
        '''

        index = self.heap_index[vertice] * 2 + 1
        return self.heap[index]


    def rSon(self, vertice : int | Point):

        '''
        Renvoie le fils de droite du sommet
        '''

        index = self.heap_index[vertice] * 2 + 2
        return self.heap[index]
    

    def get_line(self, vertice):

        '''
        Renvoie le numéro de ligne du sommet
        '''

        return  int(mt.log2(self.heap_index[vertice] + 1))

    
    def delete(self, x : int, y : int) -> None:
        
        '''
        Suppprime le point de coordonnées (x, y)
        '''

        index = self.heap_index[Point(x, y)]
        self.heap_index[Point(x, y)] = None
        self.heap[index] = 0

        if self.is_even(index):
            brother_index = index - 1
        pass

    def is_even(self, x : int):
        return not(x%2)



heap = SDH(SetOfPoint([Point(- i, i) for i in range(1, 8)]))
heap.delete(- 6, 6)
ic(heap.heap, heap.heap_index)
