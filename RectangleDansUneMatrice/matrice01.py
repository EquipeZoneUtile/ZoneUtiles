class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        
    def update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if idx <= mid:
                self.update(left_child, start, mid, idx, value)
            else:
                self.update(right_child, mid + 1, end, idx, value)
            self.tree[node] = max(self.tree[left_child], self.tree[right_child])
    
    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_max = self.query(left_child, start, mid, left, right)
        right_max = self.query(right_child, mid + 1, end, left, right)
        return max(left_max, right_max)

def maximalRectangle(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0

    heights = [0] * cols
    segment_tree = SegmentTree(cols)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                heights[j] = 0
            else:
                heights[j] += 1
            segment_tree.update(0, 0, cols - 1, j, heights[j])

        for j in range(cols):
            left = j
            while left > 0 and heights[j] <= heights[left - 1]:
                left = left - 1
            right = j
            while right < cols - 1 and heights[j] <= heights[right + 1]:
                right = right + 1
            max_area = max(max_area, heights[j] * (right - left + 1))

    return max_area

# Exemple d'utilisation
import random

def generate_random_matrix(n, m):
    matrix = []
    for _ in range(n):
        row = [random.choice(["0", "1"]) for _ in range(m)]
        matrix.append(row)
    return matrix

# Exemple d'utilisation
n = 600  # Nombre de lignes
m = 1700  # Nombre de colonnes
random_matrix = generate_random_matrix(n, m)

#print(random_matrix)






result = maximalRectangle(random_matrix)
print(result)  # Affiche la plus grande aire de rectangle composée de zéros
