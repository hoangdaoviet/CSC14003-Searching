import timeit
from heapdict import heapdict as PriorityQueue
from queue import Queue, LifoQueue as Stack
class SearchAlgorithm:
    def __init__(self):
        pass
    
    def solve(self, problem):
        start = timeit.default_timer()
        result = self.forward(problem)
        end = timeit.default_timer()
        return result[0], end - start
    
    def buildPath(self, prev, end):
        trace = end
        path = list()
        while trace != -1:
            path.append(trace)
            trace = prev[trace]
        path.reverse()
        return path

    def forward(self, problem):
        raise NotImplementedError
    
class BFS(SearchAlgorithm):
    def forward(self, problem):
        queue = Queue() # queue for BFS
        visited = [False] * problem.numNodes # list of visited nodes
        expanded = list() # list of expanded nodes
        prev = [-1] * problem.numNodes # list of previous nodes to trace back the path

        queue.put(problem.start) # put the starting node to the queue
        visited[problem.start] = True # mark the starting node as visited

        while queue.qsize() != 0:
            node = queue.get()
            expanded.append(node)
            neighbors = problem.adjList[node]
            for next, _ in neighbors:
                if next == problem.end:
                    prev[next] = node
                    return super().buildPath(prev, problem.end), expanded, queue
                if visited[next] == False:
                    queue.put(next)
                    visited[next] = True
                    prev[next] = node

        return [], expanded, queue

class DFS(SearchAlgorithm):
    def forward(self, problem):
        stack = Stack() # stack for DFS
        visited = [False] * problem.numNodes # list of visited nodes
        expanded = list() # list of expanded nodes
        prev = [-1] * problem.numNodes # list of previous nodes to trace back the path

        stack.put(problem.start) # put the starting node to the stack
        visited[problem.start] = True # mark the starting node as visited

        while stack.qsize() != 0:
            node = stack.get()
            expanded.append(node)
            neighbors = problem.adjList[node]
            for next, _ in neighbors:
                if next == problem.end:
                    prev[next] = node
                    return super().buildPath(prev, problem.end), expanded, stack
                if visited[next] == False: # the mechanism to avoid infinite loop
                    stack.put(next)
                    visited[next] = True
                    prev[next] = node
        return [], expanded, stack

class UCS(SearchAlgorithm):
    def forward(self, problem):
        pq = PriorityQueue()
        expanded = list()
        prev = [-1] * problem.numNodes

        pq[problem.start] = 0
        while len(pq) != 0:
            node, cost_node = pq.popitem()
            expanded.append(node)
            if node == problem.end:
                return super().buildPath(prev, problem.end), expanded, pq
            neighbors = problem.adjList[node]
            for next, cost_next in neighbors:
                if next not in expanded:
                    if next not in pq:
                        pq[next] = cost_node + cost_next
                        prev[next] = node
                    elif pq[next] > cost_node + cost_next:
                        pq[next] = cost_node + cost_next
                        prev[next] = node

        return [], expanded, pq
    
class DLS(SearchAlgorithm):
    def forward(self, problem, limit):
        stack = Stack() # stack for DFS
        visited = [False] * problem.numNodes
        expanded = list()
        prev = [-1] * problem.numNodes

        stack.put((problem.start, 0))
        visited[problem.start] = True

        while stack.qsize() != 0:
            node, depth = stack.get()
            expanded.append(node)
            neighbors = problem.adjList[node]
            if depth < limit:
                for next, _ in neighbors:
                    if next == problem.end:
                        prev[next] = node
                        return super().buildPath(prev, problem.end), expanded, stack
                    if visited[next] == False:
                        stack.put((next, depth+1))
                        visited[next] = True
                        prev[next] = node
        return [], expanded, stack
    
class IDS(SearchAlgorithm):
    def __init__(self, MAX_DEPTH_ALLOWED=10):
        super().__init__()
        self.MAX_DEPTH_ALLOWED = MAX_DEPTH_ALLOWED

    def forward(self, problem):
        limit = 0
        while True:
            if limit == self.MAX_DEPTH_ALLOWED:
                break
            result, expanded, stack = DLS().forward(problem, limit)
            if len(result) > 0:
                return result, expanded, stack
            limit += 1
        return [], [], []
    
class GBFS(SearchAlgorithm):
    def forward(self, problem):
        pq = PriorityQueue()
        expanded = list()
        prev = [-1] * problem.numNodes

        pq[problem.start] = problem.heuristic[problem.start]
        while len(pq) != 0:
            node, _ = pq.popitem()
            expanded.append(node)
            if node == problem.end:
                return super().buildPath(prev, problem.end), expanded, pq
            neighbors = problem.adjList[node]
            for next, _ in neighbors:
                if next not in expanded:
                    if next not in pq:
                        pq[next] = problem.heuristic[next]
                        prev[next] = node
        return [], expanded, pq
    
class AStar(SearchAlgorithm):
    def forward(self, problem):
        pq = PriorityQueue()
        expanded = list()
        prev = [-1] * problem.numNodes

        pq[problem.start] = problem.heuristic[problem.start]
        while len(pq) != 0:
            node, cost_node = pq.popitem()
            expanded.append(node)
            if node == problem.end:
                return super().buildPath(prev, problem.end), expanded, pq
            cost_node -= problem.heuristic[node] # cost_node now is the actual cost
            neighbors = problem.adjList[node]
            for next, cost_next in neighbors:
                if next not in expanded:
                    if next not in pq:
                        pq[next] = cost_node + cost_next + problem.heuristic[next]
                        prev[next] = node
                    elif pq[next] > cost_node + cost_next + problem.heuristic[next]:
                        pq[next] = cost_node + cost_next + problem.heuristic[next]
                        prev[next] = node
        return [], expanded, pq