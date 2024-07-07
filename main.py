from graph import *
from search_algorithm import *

problem = Graph('testcases/input3.txt')
problem.toAdjacencyList()
problem.printGraph('adjacency list')

print('\nSolutions:')
finder = BFS()
print(f'BFS: {finder.solve(problem)}')
finder = DFS()
print(f'DFS: {finder.solve(problem)}')
finder = UCS()
print(f'UCS: {finder.solve(problem)}')