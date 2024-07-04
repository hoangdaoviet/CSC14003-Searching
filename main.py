from graph import *
from search_algorithm import *

problem = Graph('testcases/input2.txt')
problem.toAdjacencyList()
problem.printGraph('adjacency list')

finder = DFS()
print(finder.solve(problem))

finder = BFS()
print(finder.solve(problem))