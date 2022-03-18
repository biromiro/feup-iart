""" 
a)
State Representation: (matrix, (zero_pos_row, zero_pos_col))
Initial State: (randomized matrix, random position in matrix)
(matrix should have the numbers from 0 to rows*cols)
Operators: (zero_pos_x >= 0) moveup -> (matrix, (zero_pos_row, zero_pos_col)) => (upt_matrix, (zero_pos_row - 1, zero_pos_col))
           (zero_pos_x < rows) movedown -> (matrix, (zero_pos_row, zero_pos_col)) => (upt_matrix, (zero_pos_row + 1, zero_pos_col))
           (zero_pos_y >= 0) moveleft -> (matrix, (zero_pos_row, zero_pos_col)) => (upt_matrix, (zero_pos_row, zero_pos_col - 1))
           (zero_pos_y < cols) moveright -> (matrix, (zero_pos_row, zero_pos_col)) => (upt_matrix, (zero_pos_row, zero_pos_col + 1))

upt_matrix consists in the same matrix but with the element in the position of the new zero position swapped with the previous zero position
All operators have a cost of 1.
Objective Test: Check if the matrix is ordered and the zero is positioned in the last cell
"""
from algorithms import *
from functools import reduce
import operator
import numpy as np
import copy


class NPuzzle:

    @staticmethod
    def flatten(matrix):
        return reduce(operator.concat, matrix)

    def __init__(self, matrix, zero_pos, previousNode=None, distance=0):
        all_elems_list = sorted(NPuzzle.flatten(matrix))

        if (all_elems_list != list(range(len(matrix) * len(matrix[0])))):
            raise ValueError('Invalid Input Matrix')

        x, y = zero_pos

        if (matrix[x][y] != 0):
            raise ValueError('Zero position is not correct')

        self.matrix = matrix
        self.zero_pos = zero_pos
        self.distance = distance
        self.previousNode = previousNode

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return NPuzzle.flatten(self.matrix) == NPuzzle.flatten(
                other.matrix) and self.zero_pos == other.zero_pos
        return False

    def __repr__(self):
        matrix_repr = np.array(self.matrix)
        return f'\n{matrix_repr}\n'

    def __str__(self):
        matrix_repr = np.array(self.matrix)
        return f'\n{matrix_repr}\n'

    def __lt__(self, other):
        return self.distance < other.distance

    def edgeNodes(self, distance=0):
        edgeNodesList = []
        x, y = self.zero_pos

        if (x - 1 >= 0):
            matrixcopy = copy.deepcopy(self.matrix)
            matrixcopy[x][y] = matrixcopy[x - 1][y]
            matrixcopy[x - 1][y] = 0

            edgeNodesList.append(
                NPuzzle(matrixcopy, (x - 1, y), self, distance))

        if (x + 1 < len(self.matrix)):
            matrixcopy = copy.deepcopy(self.matrix)
            matrixcopy[x][y] = matrixcopy[x + 1][y]
            matrixcopy[x + 1][y] = 0

            edgeNodesList.append(
                NPuzzle(matrixcopy, (x + 1, y), self, distance))

        if (y - 1 >= 0):
            matrixcopy = copy.deepcopy(self.matrix)
            matrixcopy[x][y] = matrixcopy[x][y - 1]
            matrixcopy[x][y - 1] = 0

            edgeNodesList.append(
                NPuzzle(matrixcopy, (x, y - 1), self, distance))

        if (y + 1 < len(self.matrix[0])):
            matrixcopy = copy.deepcopy(self.matrix)
            matrixcopy[x][y] = matrixcopy[x][y + 1]
            matrixcopy[x][y + 1] = 0

            edgeNodesList.append(
                NPuzzle(matrixcopy, (x, y + 1), self, distance))

        return edgeNodesList


def condition(node):
    return NPuzzle.flatten(node.matrix) == list(
        range(1,
              len(node.matrix[0]) * len(node.matrix))) + [0]


def heuristic1(node):
    row_length = len(node.matrix[0])
    sum_h = 0
    for row, row_val in enumerate(node.matrix):
        for col, item in enumerate(row_val):
            sum_h += 1 if item != row * row_length + col + 1 else 0

    return sum_h


def heuristic2(node):
    curr_pos = {}
    correct_pos = {}
    row_length = len(node.matrix)
    col_length = len(node.matrix[0])

    for row, row_val in enumerate(node.matrix):
        for col, item in enumerate(row_val):
            curr_pos[item] = (row, col)
            correct_pos[row * row_length + col + 1] = (row, col)

    sum_manhattan = 0
    for i in range(1, row_length * col_length):
        sum_manhattan += abs(curr_pos[i][0] -
                             correct_pos[i][0]) + abs(curr_pos[i][0] -
                                                      correct_pos[i][0])

    return sum_manhattan


initial = NPuzzle(
    [[5, 1, 3, 4], [2, 0, 7, 8], [10, 6, 11, 12], [9, 13, 14, 15]], (1, 1))

print(ucost(initial, condition))
print('-------H1----------')
print(greedy(initial, condition, heuristic1))
print('-------H1----------')
print(astar(initial, condition, heuristic1))
print('-------H2----------')
print(greedy(initial, condition, heuristic2))
print('-------H2----------')
print(astar(initial, condition, heuristic2))