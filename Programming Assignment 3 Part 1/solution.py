# Tanner Mahofski tzm5490
# Cole Schutzman cms7721
# Madeyln McNally mvm6535

def get_input():
    infoList = raw_input().split(" ")
    numVerts = int(infoList[0])
    numEdges = int(infoList[1])
    dict = {}

    for i in range(numVerts):
        dict[i] = []


    for i in range(numEdges):
        infoList = raw_input().split(" ")
        start = int(infoList[0])-1
        end = int(infoList[1])-1
        dict[start].append(end)

    return numVerts, dict

def reverse():
    reversed = {}

    for i in range(numVerts):
        reversed[i] = []

    for i in graph:
        for j in graph[i]:
            reversed[j].append(i)

    return reversed

def DFS():
    clock = 0
    for i in range(numVerts):
        if visited[i] == 0:
            explore(i,clock)

def explore(v, clock):
    visited[v] = 1
    pre.append(clock)
    clock += 1
    for j in reversed[v]:
        if visited[j] == 0:
            explore(j, clock)
    post.append(clock)
    clock += 1
    postlist.append(v)

def DFS2():
    numcc = 0
    while len(postlist) != 0:
        x = postlist.pop()
        if visit[x] == 0:
            numcc += 1
            explore2(x, numcc)

    return numcc

def explore2(v,numcc):
    visit[v] = numcc
    for j in graph[v]:
        if visit[j] == 0:
            explore2(j, numcc)


numVerts, graph = get_input()
visited = [0] * (numVerts+1)
visit = [0] * (numVerts+1)
stack = []
pre = []
post = []
postlist = []
stack = []
reversed = reverse()
DFS()
#15243
#04132
print(DFS2())
