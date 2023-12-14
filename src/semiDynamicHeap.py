from point import Point
from rectangle import RectangleBoundary
from setOfPoint import SetOfPoint
from icecream import ic
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
    

    def get_subtree_leaves(self, root : int | Point) -> SetOfPoint:

        '''
        Renvoie les feuilles du subtree de root
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
        subTree_leaves = [root]
        
        while self.get_line(subTree_leaves[0]) < self.heigh:
        
            subTree_leaves = get_childs(subTree_leaves)
            if not(subTree_leaves):
                return SetOfPoint([])
        subTree_leaves = SetOfPoint(subTree_leaves)

        return subTree_leaves
    
    def get_sol(self, root : int | Point):

        '''
        Renvoie le Point d'ordonnée la plus grande parmis les feuilles du subtree de root
        '''

        subTree_leaves = self.get_subtree_leaves(root)
        return subTree_leaves.get_max('y_coordinate')
    def lElement(self, root : int | Point) -> int:

        '''
        Renvoie la plus petite abscisse du sous-arbre de root
        '''

        if isinstance(root, Point):
            return root.x_coordinate

        subtree_leaves = self.get_subtree_leaves(root)
        return subtree_leaves.get_min('x_coordinate').x_coordinate


    def rElement(self, root : int | Point) -> int:

        '''
        Renvoie la plus grande abscisse du sous-arbre de root
        '''
        if isinstance(root, Point):
            return root.x_coordinate
        
        subtree_leaves = self.get_subtree_leaves(root)
        return subtree_leaves.get_max('x_coordinate').x_coordinate


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

    
    def delete(self) -> Point:
        
        '''
        Suppprime le point de coordonnées (x, y)
        '''
        point = self.get_sol(self.heap[0])
        index = self.heap_index[point]
        self.heap_index[point] = None
        self.heap[index] = 0

        return point

    def is_even(self, x : int):
        return not(x%2)
    

    def find(self, rectangle : RectangleBoundary, base_rectangle : RectangleBoundary) -> Point:
        
        '''
        Renvoie le Point qui a la plus grande ordonnée et qui est dans le rectangle rectangle
        '''

        vertice = self.heap[0]
        point = Point(0, base_rectangle.bottom_boundary)
        t_left, t_right = rectangle.left_boundary, rectangle.right_boundary

        ## Step 2 to 5 ##
        goto_2 = True
        while goto_2 :
            # Step 2 #
            if t_left < self.lElement(vertice) and t_right > self.rElement(vertice) :
                point.set(self.get_sol(vertice))
                ic('step2')
                return point
            # Step 3 #
            if isinstance(vertice, Point):
                ic('step3')
                return point
            
            goto_2 = False
            # Step 4 #
            if t_left >= self.rElement(self.lSon(vertice)):
                vertice = self.rSon(vertice)
                goto_2 = True
            # Step 5 #
            if t_right <= self.lElement(self.rSon(vertice)):
                vertice = self.lSon(vertice)
                goto_2 = True
        
        # Step 6 #
        u, w = self.lSon(vertice), self.rSon(vertice)

        # Step 7 #
        do_step_8 = True
        if t_left < self.lElement(vertice):
            self.switch(u, point)
            do_step_8 = False

        if do_step_8 : # Step 8 #
            # Step 9 #
            while isinstance(u, int):
                if t_left < self.rElement(self.rSon(u)):
                    
                    self.switch(self.rSon(u), point)
                    u = self.lSon(u)
                else :
                    u = self.rSon(u)
        # Step 10 #
        if t_right > self.rElement(w):
            self.switch(w, point)
            ic('step10')
            return point
        
        # Step 11 #
        while isinstance(w, int):
            ic('step11')
            if t_right > self.rElement(self.lSon(w)):
                self.switch(self.lSon(w), point)
                w = self.rSon(w)
            else:
                w = self.lSon(w)
        ic('fin')
        return point
    

    def switch(self, vertice : int | Point, point : Point):

        '''
        Change la valeur du point si cela permet d'augmenter l'air du rectangle
        '''

        sol_vertice = self.get_sol(vertice)
        if sol_vertice.y_coordinate > point.y_coordinate:
            point.set(sol_vertice)
        

if __name__ == "__main__":
    heap = SDH(SetOfPoint([Point(- i, i) for i in range(1, 8)]))
    heap.delete()
    ic(heap.heap, heap.heap_index)
