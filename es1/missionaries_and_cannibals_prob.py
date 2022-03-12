""" 
a)
State Representation: (miss_a, cann_a, miss_b, cann_b, side)
Initial State: (3, 3, 0, 0, A)
For every state: miss_a >= cann_a && miss_b >= cann_b on result state
Operators: (miss_a, cann_a, miss_b, cann_b, A) -> (miss_a - 1, cann_a, miss_b + 1, cann_b, B)
            (miss_a, cann_a, miss_b, cann_b, A) -> (miss_a , cann_a - 1, miss_b, cann_b + 1, B)
            (miss_a, cann_a, miss_b, cann_b, A) -> (miss_a - 2, cann_a, miss_b + 2, cann_b, B)
            (miss_a, cann_a, miss_b, cann_b, A) -> (miss_a - 1, cann_a - 1, miss_b + 1, cann_b + 1, B)
            (miss_a, cann_a, miss_b, cann_b, A) -> (miss_a, cann_a - 2, miss_b, cann_b + 2, B)
            (miss_a, cann_a, miss_b, cann_b, B) -> (miss_a + 1, cann_a, miss_b - 1, cann_b, A)
            (miss_a, cann_a, miss_b, cann_b, B) -> (miss_a , cann_a + 1, miss_b, cann_b - 1, A)
            (miss_a, cann_a, miss_b, cann_b, B) -> (miss_a + 2, cann_a, miss_b - 2, cann_b, A)
            (miss_a, cann_a, miss_b, cann_b, B) -> (miss_a + 1, cann_a + 1, miss_b - 1, cann_b - 1, A)
            (miss_a, cann_a, miss_b, cann_b, B) -> (miss_a, cann_a + 2, miss_b, cann_b - 2, A)
All operators have a cost of 1.
Objective Test: Check if the state is equal to (0, 0, 3, 3, B)
"""

from algorithms import *;

class MissionariesCannibalsNode:
    def __init__(self, miss_a, cann_a, miss_b, cann_b, onSideA, previousNode = None):
        self.miss_a = miss_a;
        self.cann_a = cann_a;
        self.miss_b = miss_b;
        self.cann_b = cann_b;
        self.onSideA = onSideA;
        self.previousNode = previousNode;
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.miss_a == other.miss_a and self.cann_a == other.cann_a and self.miss_b == other.miss_b and self.cann_b == other.cann_b and self.onSideA == other.onSideA;
        return False;
    
    def __repr__(self):
        return f'({self.miss_a}, {self.cann_a}, {self.miss_b}, {self.cann_b}, {"A" if self.onSideA else "B"})';
    
    def __str__(self):
        return f'({self.miss_a}, {self.cann_a}, {self.miss_b}, {self.cann_b}, {"A" if self.onSideA else "B"})';
    
    @staticmethod
    def isValidState(miss_a, cann_a, miss_b, cann_b):
        if (miss_a < 0 or cann_a < 0 or miss_b < 0 or cann_b < 0): return False;
        return (miss_a >= cann_a or miss_a == 0) and (miss_b >= cann_b or miss_b == 0);
    
    def edgeNodes(self):
        edgeNodesList = []
        
        if (self.onSideA):           
            if(MissionariesCannibalsNode.isValidState(self.miss_a - 1, self.cann_a, self.miss_b + 1, self.cann_b)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a - 1, self.cann_a, self.miss_b + 1, self.cann_b, False, self));
            
            if(MissionariesCannibalsNode.isValidState(self.miss_a, self.cann_a - 1, self.miss_b, self.cann_b + 1)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a, self.cann_a - 1, self.miss_b, self.cann_b + 1, False, self));
            
            if(MissionariesCannibalsNode.isValidState(self.miss_a - 2, self.cann_a, self.miss_b + 2, self.cann_b)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a - 2, self.cann_a, self.miss_b + 2, self.cann_b, False, self));
            
            if(MissionariesCannibalsNode.isValidState(self.miss_a, self.cann_a - 2, self.miss_b, self.cann_b + 2)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a, self.cann_a - 2, self.miss_b, self.cann_b + 2, False, self));
            
            if(MissionariesCannibalsNode.isValidState(self.miss_a - 1, self.cann_a - 1, self.miss_b + 1, self.cann_b + 1)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a - 1, self.cann_a - 1, self.miss_b + 1, self.cann_b + 1, False, self));

        elif (not self.onSideA):

            if(MissionariesCannibalsNode.isValidState(self.miss_a + 1, self.cann_a, self.miss_b - 1, self.cann_b)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a + 1, self.cann_a, self.miss_b - 1, self.cann_b, True, self));
            
            if(MissionariesCannibalsNode.isValidState(self.miss_a, self.cann_a + 1, self.miss_b, self.cann_b - 1)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a, self.cann_a + 1, self.miss_b, self.cann_b - 1, True, self));
            
            if(MissionariesCannibalsNode.isValidState(self.miss_a + 2, self.cann_a, self.miss_b - 2, self.cann_b)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a + 2, self.cann_a, self.miss_b - 2, self.cann_b, True, self));
            
            if(MissionariesCannibalsNode.isValidState(self.miss_a, self.cann_a + 2, self.miss_b, self.cann_b - 2)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a, self.cann_a + 2, self.miss_b, self.cann_b - 2, True, self));
            
            if(MissionariesCannibalsNode.isValidState(self.miss_a + 1, self.cann_a + 1, self.miss_b - 1, self.cann_b - 1)):
                edgeNodesList.append(MissionariesCannibalsNode(self.miss_a + 1, self.cann_a + 1, self.miss_b - 1, self.cann_b - 1, True, self));
            
        return edgeNodesList;

MISS_NUM = 3;
CANN_NUM = 3;    

initial = MissionariesCannibalsNode(MISS_NUM, CANN_NUM, 0, 0, True)

def condition(node):
    return node == MissionariesCannibalsNode(0, 0, MISS_NUM, CANN_NUM, False);

print(bfs(initial, condition))
print(dfs(initial, condition))
print(it_deep(initial, condition))
