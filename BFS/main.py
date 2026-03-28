class node:
    def __init__(self,state,parent,action):
        self.state = state #name of the current node
        self.parent = parent #current parent of the node
        self.action = action #current neighbours of the node

def action_sequence(graph,goalstate): #This is used for backtracking meaning that onces we hv found our goal state to track the path back to the intial state we use this
    solution = [goalstate] #the first value in our solution list will be our goal
    currentparent = graph[goalstate].parent #first parent is the parent of our goal

    while currentparent is not None: #checks if we are at the root node or starting node or not starting node
        solution.append(currentparent) #if parent is not null we add it to our solution
        currentparent = graph[currentparent].parent #we set the current parent of graph to be the parent of the parent of root node
    
    solution.reverse() #reverse the list so we track path from root to goal not from goal to root

    return solution

def bfs():
    initial_State = "0"
    goal_State = "7"

    graph = {
        "0" : node("0",None,["1","2","3"]),
        "1" : node("1",None,["4","5","0"]),
        "2" : node("2",None,["6","0"]),
        "3" : node("3",None,["7","0"]),
        "4" : node("4",None,["1"]),
        "5" : node("5",None,["1"]),
        "6" : node("6",None,["2"]),
        "7" : node("7",None,["3"]),
    }

    frontier = [initial_State]
    explored = []

    while frontier:
        currentnode = frontier.pop(0)

        if graph[currentnode].state == goal_State:
            return action_sequence(graph ,currentnode)
        
        if currentnode not in explored:
            explored.append(currentnode)

            for child in graph[currentnode].action:
                if child not in frontier and child not in explored :
                    graph[child].parent = currentnode
                
                if graph[child].state == goal_State:
                    return action_sequence(graph ,goal_State)
                
                frontier.append(child)

print(bfs())
