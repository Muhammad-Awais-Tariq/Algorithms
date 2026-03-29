class node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

def actionsequence(goalstate,graph):
    solution = [graph[goalstate].state]
    currentparent = graph[goalstate].parent

    while currentparent is not None:
        solution.append(graph[currentparent].state)
        currentparent = graph[currentparent].parent
    
    solution.reverse()

    return solution

def dls(currentnode,goalstate,graph,depthlimit,visited):

    if depthlimit < 0:
        return None
    
    if currentnode == goalstate:
        return goalstate
    
    visited.add(graph[currentnode].state)  

    for child in graph[currentnode].action:
        if child not in visited:
            graph[child].parent = currentnode

            result = dls(child,goalstate,graph,depthlimit-1,visited)

            if result is not None:
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
        result = dls(intialstate,goalstate,graph,depthlimit,set())

        if result != None:
            return actionsequence(result,graph)

        depthlimit +=1

        if depthlimit > len(graph):
            return None    
        
print(iddfs())