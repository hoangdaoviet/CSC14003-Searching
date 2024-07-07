import timeit
from queue import PriorityQueue

class SearchAlgorithm:
    def __init__(self):
        pass
    
    def solve(self, problem):
        start = timeit.default_timer()
        result = self.forward(problem)
        end = timeit.default_timer()
        return result[0], end - start

    def forward(self, problem):
        raise NotImplementedError
    
class BFS(SearchAlgorithm):
    def forward(self, problem):
        start = problem.start
        queue = list()
        queue.append(start)

        visited = [False] * problem.numNodes
        visited[start] = True
        prev = [-1] * problem.numNodes
        foundEnd = False

        while len(queue)!=0 and not foundEnd:
            node = queue.pop(0)
            neighbors = problem.adjList[node]
            for next in neighbors:
                if next[0]==problem.end:
                    prev[next[0]] = node
                    foundEnd = True
                    break
                if visited[next[0]]==False:
                    queue.append(next[0])
                    visited[next[0]] = True
                    prev[next[0]] = node
            
        trace = problem.end
        path = list()
        while trace != -1:
            path.append(trace)
            trace = prev[trace]
        path.reverse()
        return path, queue, visited, prev

class DFS(SearchAlgorithm):
    def forward(self, problem):
        start = problem.start
        stack = list()
        stack.append(start)

        visited = [False] * problem.numNodes
        visited[start] = True
        prev = [-1] * problem.numNodes
        foundEnd = False

        while len(stack) != 0 and not foundEnd:
            node = stack.pop()
            neighbors = problem.adjList[node]
            for next in neighbors:
                if next[0]==problem.end:
                    prev[next[0]] = node
                    foundEnd = True
                    break
                if visited[next[0]]==False:
                    stack.append(next[0])
                    visited[next[0]] = True
                    prev[next[0]] = node
        
        trace = problem.end
        path = list()
        while trace != -1:
            path.append(trace)
            trace = prev[trace]
        path.reverse()
        return path, stack, visited, prev
    
class UCS(SearchAlgorithm):
    def forward(self, problem):
        start = problem.start
        pq = PriorityQueue()