class Node:
    def __init__(self,state,action):
        self.state = state
        self.parent = None
        self.action = action
        self.costfromstart = float("inf")

def actionsequence(goalstate,graph):
    solution = [goalstate]
    currentparent = graph[goalstate].parent

    while currentparent is not None:
        solution.append(currentparent)
        currentparent = graph[currentparent].parent

    solution.reverse()
    
    return solution

def heuristic(city):
    heuristics = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
        'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
        'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
        'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }
    return heuristics.get(city, float('inf')) 

def AStar():
    initialState = 'Arad'
    goalState = 'Bucharest'

    graph = {
        'Arad': Node('Arad',  [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)]),
        'Zerind': Node('Zerind',  [('Arad', 75), ('Oradea', 71)]),
        'Oradea': Node('Oradea',  [('Zerind', 71), ('Sibiu', 151)]),
        'Sibiu': Node('Sibiu',  [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)]),
        'Fagaras': Node('Fagaras',  [('Sibiu', 99), ('Bucharest', 211)]),
        'Rimnicu Vilcea': Node('Rimnicu Vilcea',  [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)]),
        'Pitesti': Node('Pitesti',  [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)]),
        'Craiova': Node('Craiova',  [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)]),
        'Drobeta': Node('Drobeta',  [('Mehadia', 75), ('Craiova', 120)]),
        'Mehadia': Node('Mehadia',  [('Lugoj', 70), ('Drobeta', 75)]),
        'Lugoj': Node('Lugoj',  [('Timisoara', 111), ('Mehadia', 70)]),
        'Timisoara': Node('Timisoara',  [('Arad', 118), ('Lugoj', 111)]),
        'Bucharest': Node('Bucharest',  [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)]),
        'Giurgiu': Node('Giurgiu',  [('Bucharest', 90)]),
        'Urziceni': Node('Urziceni',  [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)]),
        'Hirsova': Node('Hirsova',  [('Urziceni', 98), ('Eforie', 86)]),
        'Eforie': Node('Eforie',  [('Hirsova', 86)]),
        'Vaslui': Node('Vaslui',  [('Urziceni', 142), ('Iasi', 92)]),
        'Iasi': Node('Iasi',  [('Vaslui', 92), ('Neamt', 87)]),
        'Neamt': Node('Neamt',  [('Iasi', 87)]),
    }

    graph[initialState].costfromstart = 0

    frontier = [(heuristic(initialState),initialState)]

    explored = set()
    while frontier:
        frontier.sort()
        heuristic_cost , currentnode = frontier.pop(0)

        if currentnode == goalState:
            return actionsequence(goalState,graph)
        
        explored.add(currentnode)
        for child ,cost in graph[currentnode].action:
                newcostfromstart = graph[currentnode].costfromstart + cost
                newheuristiccost = newcostfromstart + heuristic(child)

                if child in explored:
                    continue

                if newcostfromstart < graph[child].costfromstart:
                    graph[child].costfromstart = newcostfromstart
                    graph[child].parent = currentnode
                    frontier.append((newheuristiccost , child))
    
    return None

print(AStar())