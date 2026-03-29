class node:
    def __init__(self,state,parent,action,totalcost):
        self.state = state
        self.parent = parent
        self.action = action
        self.totalcost = totalcost

def actionsequence(goalstate,graph):
    solution = [goalstate]
    currentparent = graph[goalstate].parent

    while currentparent is not None:
        solution.append(currentparent)
        currentparent = graph[currentparent].parent

    solution.reverse()
    
    return solution

def findmin(frontier):
    mincost = float('inf')
    minnode = None

    for node,cost in frontier:
        if cost < mincost:
            mincost = cost
            minnode = node
    
    return minnode,mincost

def ucs():
    initialstate = 'A'
    goalstate = 'G'
  
    graph = {
        'A': node('A', None, [('B', 6), ('C', 9), ('E', 1)], float('inf')),
        'B': node('B', None, [('A', 6), ('D', 3), ('E', 4)], float('inf')),
        'C': node('C', None, [('A', 9), ('F', 2), ('G', 3)], float('inf')),
        'D': node('D', None, [('B', 3), ('E', 5),('F', 7)], float('inf')),
        'E': node('E', None, [('A', 1), ('B', 4), ('D', 5),('F', 6)], float('inf')),
        'F': node('F', None, [('C', 2),('E', 6),('D', 7)], float('inf')),
        'G': node('G', None, [('C', 3)], float('inf'))
    }

    if initialstate == goalstate:
        return actionsequence(initialstate,graph)
    graph[initialstate].totalcost = 0

    frontier = [(initialstate,0)]    
    explored = []
    
    while frontier:
        currentnode , currentcost = findmin(frontier)
        frontier.remove((currentnode,currentcost))
        explored.append(currentnode)
        if graph[currentnode].state == goalstate:
            return actionsequence(goalstate,graph)
        
        for child,cost in graph[currentnode].action:
            newcost = currentcost + cost
            if child not in explored:
                if (child,newcost) not in frontier and graph[child].totalcost > newcost:
                    graph[child].parent = currentnode
                    graph[child].totalcost = newcost
                    frontier.append((graph[child].state,newcost))
    
    return None

print(ucs())