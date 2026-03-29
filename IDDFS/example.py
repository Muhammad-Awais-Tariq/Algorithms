class node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

def dls(currentnode,graph,words,depthlimit,wordformed,found,visited):

    if depthlimit < 0:
        return None
    
    if wordformed in words:
        found.append(wordformed)
    
    visited.add(currentnode)
    for child in graph[currentnode].action:
        if child not in visited:
            childword = wordformed + graph[child].state
            dls(child,graph,words,depthlimit-1,childword,found,visited)

    visited.remove(currentnode)
    return found
def iddfs():
    words = ["START", "NOTE", "SAND","STONED"]

    box = [
        ["M","S","E","F"],
        ["R","A","T","D"],
        ["L","O","N","E"],
        ["K","A","F","B"],
    ]
    found = []  
    graph = {}
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for l in range(4):
        for m in range(4):
            action = []
            for move in moves:
                nr ,nc = l+move[0] , m+move[1]
                if 0<=nr<4 and 0<=nc<4:
                    action.append((nr,nc))
            graph[(l,m)] = node(box[l][m],None,action)  

    maxdepth = 3
    for depthlimit in range(0,maxdepth+1):
        for i in range(4):
            for j in range(4):
                    wordformed = graph[(i,j)].state
                    dls((i,j),graph,words,depthlimit,wordformed,found,set())

                    if depthlimit > len(box):
                        return None                            
    
    return set(found)

print(iddfs())