class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):

        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def breadth_first_search(self, s):
        queue = []
        s.color = 'gray'
        queue.append(s)
        while queue:
            current = queue.pop(0)
            for nbr in current.getConnections():
                if nbr.color == 'white':
                    nbr.color = 'gray'
                    queue.append(nbr)
            current.color = 'black'

    def depth_first_search(self):
        for vertex in self:
            if vertex.color == 'white':
                self.DFS(vertex)

    def DFS(self, vid, path):
        vid.color = 'gray'
        path.append(vid)
        for nbr in vid.getConnections():
            if nbr.color == 'white':
                self.DFS(nbr, path)
        vid.color = 'black'
