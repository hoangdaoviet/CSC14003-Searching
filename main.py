from graph import *
from search_algorithm import *

typePrint = ['adjacency list', 'adjacency matrix']

path = input()

problem = Graph(path)
problem.toAdjacencyList()
problem.printGraph(type=typePrint[0])

print('\nSolutions:')
finder = BFS()
print(f'BFS: {finder.forward(problem)}')
finder = DFS()
print(f'DFS: {finder.forward(problem)}')
finder = UCS()
print(f'UCS: {finder.forward(problem)}')
finder = IDS()
print(f'IDS: {finder.forward(problem)}')
finder = GBFS()
print(f'GBFS: {finder.forward(problem)}')
finder = AStar()
print(f'AStar: {finder.forward(problem)}')