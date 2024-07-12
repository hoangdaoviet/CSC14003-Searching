from graph import *
from search_algorithm import *
from helper_functions import *

typePrint = ['adjacency list', 'adjacency matrix']

# path = input()
path = 'testcases/input1.txt'

problem = Graph(path)
problem.toAdjacencyList()
problem.printGraph(type=typePrint[0])

finder = BFS()
path, time, memory = finder.solve(problem)
export('BFS', path, time, memory)