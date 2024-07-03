class Graph:
    def __init__(self, path):
        fin = open(path, 'r')

        self.numNodes = int(fin.readline())
        self.start, self.end = map(int, fin.readline().split())
        self.adjMatrix = [list(map(int, fin.readline().split())) for i in range(self.numNodes)]
        self.heuristic = list(map(int, fin.readline().split()))

        fin.close()

        self.directed = self.isDirected()

    def isDirected(self):
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                if self.adjMatrix[i][j] != self.adjMatrix[j][i]:
                    return True
        return False
    
    def toAdjacencyList(self):
        self.adjList = [[] for _ in range(self.numNodes)]
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                if self.adjMatrix[i][j] != 0:
                    self.adjList[i].append((j, self.adjMatrix[i][j]))

    def printGraph(self, type=''):
        print('Number of nodes:', self.numNodes)
        print('Start node:', self.start)
        print('End node:', self.end)
        if type=='adjacency matrix':
            print('Adjacency matrix:')
            for row in self.adjMatrix:
                print(row)
        elif type=='adjacency list':
            print('Adjacency list')
            for node in range(self.numNodes):
                print(f'{node}: {self.adjList[node]}')
        print('Heuristic:')
        print(self.heuristic)