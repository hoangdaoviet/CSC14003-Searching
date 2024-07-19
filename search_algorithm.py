import timeit
from heapdict import heapdict as PriorityQueue
from queue import Queue, LifoQueue as Stack
import tracemalloc

class SearchAlgorithm:
    def __init__(self):
        pass
    
    def solve(self, problem):
        tracemalloc.start()
        
        start = timeit.default_timer()
        before = tracemalloc.take_snapshot()

        result = self.forward(problem)
        
        after = tracemalloc.take_snapshot()
        end = timeit.default_timer()

        stats = after.compare_to(before, 'lineno')
        tracemalloc.stop()        

        totalMemory = sum([stat.size_diff for stat in stats])
        totalTime = end - start
        return result, totalTime, totalMemory
    
    def buildPath(self, parent, end):
        trace = end
        path = list()
        while trace != -1:
            path.append(trace)
            trace = parent[trace]
        path.reverse()
        return path

    def forward(self, problem):
        raise NotImplementedError
    
class BFS(SearchAlgorithm):
    def forward(self, problem):
        queue = Queue() # queue for BFS
        explored = [False] * problem.numNodes # mark the explored nodes
        parent = [-1] * problem.numNodes # list of parentious nodes to trace back the path

        queue.put(problem.start) # put the starting node to the queue
        explored[problem.start] = True # mark the starting node as explored

        while queue.qsize() != 0:
            node = queue.get()
            neighbors = problem.adjList[node]
            for next, _ in neighbors:
                if next == problem.end:
                    parent[next] = node
                    return super().buildPath(parent, problem.end)
                if explored[next] == False:
                    queue.put(next)
                    explored[next] = True
                    parent[next] = node

        return []

class DFS(SearchAlgorithm):
    def forward(self, problem):
        stack = Stack() # stack for DFS
        explored = [False] * problem.numNodes # mark the explored nodes
        parent = [-1] * problem.numNodes # list of parentious nodes to trace back the path

        stack.put(problem.start) # put the starting node to the stack
        explored[problem.start] = True # mark the starting node as explored

        while stack.qsize() != 0:
            node = stack.get()
            neighbors = problem.adjList[node]
            for next, _ in neighbors:
                if next == problem.end:
                    parent[next] = node
                    return super().buildPath(parent, problem.end)
                if explored[next] == False: # the mechanism to avoid infinite loop
                    stack.put(next)
                    explored[next] = True
                    parent[next] = node

        return []

class UCS(SearchAlgorithm):
    def forward(self, problem):
        pq = PriorityQueue()
        expanded = [False] * problem.numNodes
        parent = [-1] * problem.numNodes

        pq[problem.start] = 0

        while len(pq) != 0:
            node, costNode = pq.popitem()
            expanded[node] = True
            if node == problem.end:
                return super().buildPath(parent, problem.end)
            neighbors = problem.adjList[node]
            for next, costNext in neighbors:
                if expanded[next] == False:
                    if next not in pq or pq[next] > costNode + costNext:
                        pq[next] = costNode + costNext
                        parent[next] = node

        return []
    
class DLS(SearchAlgorithm):
    def forward(self, problem, limit):
        stack = Stack() # stack for DFS
        explored = [False] * problem.numNodes
        parent = [-1] * problem.numNodes

        stack.put((problem.start, 0))
        explored[problem.start] = True

        while stack.qsize() != 0:
            node, depth = stack.get()
            neighbors = problem.adjList[node]
            if depth < limit:
                for next, _ in neighbors:
                    if next == problem.end:
                        parent[next] = node
                        return super().buildPath(parent, problem.end)
                    if explored[next] == False:
                        stack.put((next, depth+1))
                        explored[next] = True
                        parent[next] = node

        return []
    
class IDS(SearchAlgorithm):
    def __init__(self, MAX_DEPTH_ALLOWED=10):
        super().__init__()
        self.MAX_DEPTH_ALLOWED = MAX_DEPTH_ALLOWED

    def forward(self, problem):
        limit = 0
        while True:
            if limit == self.MAX_DEPTH_ALLOWED:
                break
            result = DLS().forward(problem, limit)
            if len(result) > 0:
                return result
            limit += 1

        return []
    
class GBFS(SearchAlgorithm):
    def forward(self, problem):
        pq = PriorityQueue()
        explored = [False] * problem.numNodes 
        parent = [-1] * problem.numNodes

        pq[problem.start] = problem.heuristic[problem.start]
        explored[problem.start] = True

        while len(pq) != 0:
            node, _ = pq.popitem()
            neighbors = problem.adjList[node]
            for next, _ in neighbors:
                if next == problem.end:
                    parent[next] = node
                    return super().buildPath(parent, problem.end)
                if explored[next] == False:
                    pq[next] = problem.heuristic[next]
                    explored[next] = True
                    parent[next] = node
                    
        return []

    
class AStar(SearchAlgorithm):
    def forward(self, problem):
        pq = PriorityQueue()
        expanded = [False] * problem.numNodes
        parent = [-1] * problem.numNodes

        pq[problem.start] = problem.heuristic[problem.start]

        while len(pq) != 0:
            node, costNode = pq.popitem()
            expanded[node] = True
            if node == problem.end:
                return super().buildPath(parent, problem.end)
            costNode -= problem.heuristic[node] # costNode now is the actual cost
            neighbors = problem.adjList[node]
            for next, costNext in neighbors:
                if expanded[next] == False:
                    if next not in pq or pq[next] > costNode + costNext + problem.heuristic[next]:
                        pq[next] = costNode + costNext + problem.heuristic[next]
                        parent[next] = node

        return []
    
class SimpleHillClimbing(SearchAlgorithm):
    def forward(self, problem):
        parent = [-1] * problem.numNodes

        currentNode = problem.start
        
        while True:
            bestNode = None
            bestHeuristic = 1e18
            neighbors = problem.adjList[currentNode]
            for next, _ in neighbors:
                if next == problem.end:
                    parent[next] = currentNode
                    return super().buildPath(parent, problem.end)
                if problem.heuristic[next] < bestHeuristic:
                    bestHeuristic = problem.heuristic[next]
                    bestNode = next
            if bestHeuristic >= problem.heuristic[currentNode]:
                return []
            parent[bestNode] = currentNode
            currentNode = bestNode