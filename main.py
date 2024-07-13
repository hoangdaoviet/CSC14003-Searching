from graph import *
from search_algorithm import *
from helper_functions import *
import importlib

typePrint = ['adjacency list', 'adjacency matrix']

print('The input file must be put inside the folder "input".')
filename = input('Enter the path to the input file: ')

problem = Graph('input/' + filename)
problem.toAdjacencyList()

algorithms = {
    'BFS': 'BFS',
    'DFS': 'DFS',
    'UCS': 'UCS',
    'IDS': 'IDS',
    'GBFS': 'GBFS',
    'A*': 'AStar',
    'Hill-climbing': 'SimpleHillClimbing',
    }

for key in algorithms:
    module = importlib.import_module('search_algorithm')
    class_ = getattr(module, algorithms[key])
    instance = class_()
    path, time, memory = instance.solve(problem)
    exportToFile(key, path, time, memory, 'output/' + filename)

print('The output file is saved in the folder "output".')