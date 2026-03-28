class node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

def actionsequece(goalstate,graph):
    solution = [goalstate]
    currentparent = graph[goalstate].parent

    while currentparent is not None:
        solution.append(currentparent.state)
        currentparent = graph[currentparent.state].parent
    
    solution.reverse()

    return solution

def dls(node,goalstate,graph,maxdepth,visited):
    if maxdepth < 0:
        return None
    
    if node.state == goalstate:
        return True
    visited.add(node.state)

    for child in node.action:
        if child not in visited:
            graph[child].parent = node
            result = dls(graph[child],goalstate,graph,maxdepth-1,visited)

            if result != None:
                return result
    
    return None

def iddfs():
    intialstate = "0"
    goalstate = "7"

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

    depthlimit = 0

    while True:
        result = dls(graph[intialstate],goalstate,graph,depthlimit,set())

        if result != None:
            return actionsequece(goalstate,graph)
        
        depthlimit += 1

        if depthlimit > len(graph):
            return None

print(iddfs())