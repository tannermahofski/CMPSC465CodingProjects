from heapq import heapify, heappop

class Graph():

    def __init__(self,nodes,edges):
        self.adjGraph = [[-1] * nodes for i in range(nodes)]
        for i in range(edges):
            a,b,c = input().split(" ")
            a,b,c = int(a)-1,int(b)-1,int(c)
            self.adjGraph[a][b] = c



def decQueue(queue, v, val):
    for i in range(len(queue)):
        if v == queue[i][1]:
            queue[i] = (val, v)
            heapify(queue)
            return queue


numNodes, numEdges, sourceNode =  input().split(" ")
numNodes, numEdges, sourceNode = int(numNodes), int(numEdges), int(sourceNode)-1
g = Graph(numNodes, numEdges)


dist = [9999999] * numNodes
q = [(9999999,i) for i in range(numNodes)]

dist[sourceNode] = 0
decQueue(q, sourceNode, 0)

while len(q) > 0:
    vs = heappop(q)[1]
    for u,d in enumerate(g.adjGraph[vs]):
        if d != -1 and dist[u] > dist[vs] + d:
            dist[u] = dist[vs] + d
            q = decQueue(q, u, dist[u])

for i in dist:
    if i < 9999999:
        print(i)
    else:
        print(-1)
