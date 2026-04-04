#instead of finding only the one better neighbour this algorithm collects all of the neighbours 
import math
import random

class Node:
    def __init__(self,state,action,heuristic):
        self.state = state
        self.action = action
        self.heuristic = heuristic

def StochastichillClimbing():
    intialstate = "A"
    goalState = "Y"

    graph = {
        'A': Node('A', ['F'], (0,0)),  #First value is the name of node, Second is the neighbour of the node , Third is the heuristic which right now are cordinates
        'B': Node('B', ['G', 'C'], (2, 0)),
        'C': Node('C', ['H', 'D'], (3, 0)),
        'D': Node('D', ['I', 'E'], (4, 0)),
        'E': Node('E', ['D'], (5, 0)),
        'F': Node('F', ['A', 'H'], (0, 1)),
        'G': Node('G', ['B', 'J'], (2, 1)),
        'H': Node('H', ['F', 'I', 'M'], (0, 2)),
        'I': Node('I', ['H', 'J', 'N'], (1, 2)),
        'J': Node('J', ['G', 'I'], (2, 2)),
        'K': Node('K', ['L', 'P'], (4, 2)),
        'L': Node('L', ['K', 'Q'], (5, 2)),
        'M': Node('M', ['H', 'N', 'R'], (0, 3)),
        'N': Node('N', ['I', 'M', 'S'], (1, 3)),
        'O': Node('O', ['P', 'U'], (3, 3)),
        'P': Node('P', ['O', 'Q'], (4, 3)),
        'Q': Node('Q', ['L', 'P', 'V'], (5, 3)),
        'R': Node('R', ['M', 'S'], (0, 4)),
        'S': Node('S', ['N', 'R', 'T'], (1, 4)),
        'T': Node('T', ['S', 'U', 'W'], (2, 4)),
        'U': Node('U', ['O', 'T'], (3, 4)),
        'V': Node('V', ['Q', 'Y'], (5, 4)),
        'W': Node('W', ['T'], (2, 5)),
        'X': Node('X', ['Y'], (4, 5)),
        'Y': Node('Y', ['V', 'X'], (5, 5))
    }    

    parentNode = intialstate
    parentcost = math.dist(graph[goalState].heuristic, graph[parentNode].heuristic)

    explored = []
    solution = [parentNode]
    while parentNode != goalState:
        explored.append(parentNode)
        best_childs = []

        for child in graph[parentNode].action:
            childnode = child

            if childnode not in explored:
                childcoust = math.dist(graph[goalState].heuristic, graph[childnode].heuristic)

                if childcoust < parentcost:
                    best_childs.append((childnode,childcoust))

        if not best_childs:
            break

        nextnode , nextcost = random.choice(best_childs)

        parentNode = nextnode
        parentcost = nextcost
        solution.append(parentNode)
    
    return solution

print(StochastichillClimbing())