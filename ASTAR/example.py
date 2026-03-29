class node:
    def __init__(self,state,action):
        self.state =state
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

def calculateheuristic(state,goalstate):
    x1 , y1 = state
    x2 , y2 = goalstate

    heuristic = abs(x2-x1) + abs(y2-y1)

    return heuristic

def astar():
    intialstate = (5, 0)
    goalstate = (0, 5)
    maze = [
        [1,1,0,1,0,0],
        [0,0,0,0,1,0],
        [0,0,1,0,0,0],
        [0,0,0,1,0,0],
        [0,1,0,1,1,1],
        [0,1,0,0,0,0],
    ]

    graph = {}
    for i in range(6):
        for j in range(6):
            action = []
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for move in moves:
                nr,nc = i+move[0] , j+move[1]
                if 0<=nr<6 and 0<=nc<6 and maze[nr][nc] == 0:
                    action.append(((nr,nc),1))
                
            graph[(i,j)] = node((i,j),action)

    frontier = [(0,intialstate)]
    explored = set()

    graph[intialstate].costfromstart = 0
    while frontier:
        frontier.sort()
        heuristiccost , currentnode = frontier.pop(0)

        if currentnode == goalstate:
            return actionsequence(goalstate,graph)
        
        explored.add(currentnode)

        for child,cost in graph[currentnode].action:
            newcost = graph[currentnode].costfromstart + cost
            newheuristic = newcost + calculateheuristic(child,goalstate)
            if child in explored:
                continue

            if newcost < graph[child].costfromstart:
                graph[child].parent = currentnode
                graph[child].costfromstart = newcost

                frontier.append((newheuristic,child))
    
    return None

print(astar())