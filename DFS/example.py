class node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

def dfs():
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

    for i in range(4):
        for j in range(4):
            intial_state = (i,j)

            frontier = [(intial_state , graph[intial_state].state , [(i,j)] )]

            while frontier:
                currentnode , currentword , visited = frontier.pop()

                if currentword in words:
                    found.append(currentword)

                for child in graph[currentnode].action:
                    if child not in visited:
                        new_word = currentword + graph[child].state
                        new_visited = visited + [child]
                        if any(word.startswith(new_word) for word in words):
                            frontier.append((child,new_word,new_visited))
    return set(found)

print(dfs())
