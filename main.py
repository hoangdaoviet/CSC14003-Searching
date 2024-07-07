from graph import *
from search_algorithm import *

typePrint = ['adjacency list', 'adjacency matrix']

path = input()

problem = Graph(path)
problem.toAdjacencyList()
problem.printGraph(type=typePrint[0])

print('\nSolutions:')
finder = BFS()
print(f'BFS: {finder.solve(problem)}')
finder = DFS()
print(f'DFS: {finder.solve(problem)}')
finder = UCS()
print(f'UCS: {finder.solve(problem)}')
finder = IDS()
print(f'IDS: {finder.solve(problem)}')
finder = GBFS()
print(f'GBFS: {finder.solve(problem)}')
finder = AStar()
print(f'AStar: {finder.solve(problem)}')