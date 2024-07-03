from graph import *
from search_algorithm import *

problem = Graph('testcases/input.txt')
problem.toAdjacencyList()
problem.printGraph('adjacency list')

finder = BFS()
print(finder.solve(problem))