""" 
a)
State Representation: (c1(liters), c2(liters))
Initial State: (0,0)
(Preconds behind the state change)
Operators: (x != 4) fillc1 -> (x, c2_l) => (4, c2_l)
           (x != 3) fillc2 -> (c1_l, x) => (c1_l, 3)
           (x != 0) emptyc1 -> (x, c2_l) => (0, c2_l)
           (x != 0) emptyc2 -> (c1_l, x) => (c1_l, 0)
           (c1_l != 0, c1_l + c2_l < 3) emptyc1pourc2 -> (c1_l, c2_l) => (0, c1_l + c2_l)
           (c2_l != 3, c1_l + c2_l > 3) pourc1c2 -> (c1_l, c2_l) => (c1_l + c2_l - 3, 3)
           (c2_l != 0, c1_l + c2_l < 4) emptyc2pourc1 -> (c1_l, c2_l) => (c1_l + c2_l, 0)
           (c1_l != 4, c1_l + c2_l > 4) pourc2c1 -> (c1_l, c2_l) => (4, c1_l + c2_l - 4) 
All operators have a cost of 1.
Objective Test: Check if the state is of the form (n, _) -> c1_l === n
"""
from algorithms import *

C1_L_MAX = 7
C2_L_MAX = 3
n = 5


class BucketNode:

    def __init__(self, c1_l, c2_l, previousNode=None, distance=0):
        self.c1_l = c1_l
        self.c2_l = c2_l
        self.previousNode = previousNode
        self.distance = distance

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.c1_l == other.c1_l and self.c2_l == other.c2_l
        return False

    def __repr__(self):
        return f'({self.c1_l}, {self.c2_l})'

    def __str__(self):
        return f'({self.c1_l}, {self.c2_l})'

    def __lt__(self, other):
        return self.distance < other.distance

    def edgeNodes(self, distance=0):
        edgeNodesList = []

        if (self.c1_l != C1_L_MAX):
            edgeNodesList.append(
                BucketNode(C1_L_MAX, self.c2_l, self, distance))

        if (self.c2_l != C2_L_MAX):
            edgeNodesList.append(
                BucketNode(self.c1_l, C2_L_MAX, self, distance))

        if (self.c1_l != 0):
            edgeNodesList.append(BucketNode(0, self.c2_l, self, distance))

        if (self.c2_l != 0):
            edgeNodesList.append(BucketNode(self.c1_l, 0, self, distance))

        if (self.c1_l != 0 and self.c1_l + self.c2_l < C2_L_MAX):
            edgeNodesList.append(
                BucketNode(0, self.c1_l + self.c2_l, self, distance))

        if (self.c2_l != C2_L_MAX and self.c1_l + self.c2_l > C2_L_MAX):
            edgeNodesList.append(
                BucketNode(self.c1_l + self.c2_l - C2_L_MAX, C2_L_MAX, self,
                           distance))

        if (self.c2_l != 0 and self.c1_l + self.c2_l < C1_L_MAX):
            edgeNodesList.append(
                BucketNode(self.c1_l + self.c2_l, 0, self, distance))

        if (self.c1_l != C1_L_MAX and self.c1_l + self.c2_l > C1_L_MAX):
            edgeNodesList.append(
                BucketNode(C1_L_MAX, self.c1_l + self.c2_l - C1_L_MAX, self,
                           distance))

        return edgeNodesList


initial = BucketNode(0, 0)


def condition(node):
    return node.c1_l == n


def heuristic(node):
    return abs(node.c1_l + node.c2_l - n)


print('-----------------')
print(greedy(initial, condition, heuristic))
print('-----------------')
print(astar(initial, condition, heuristic))