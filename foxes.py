# Yuchuan Ma
# Sep 18, 2023
# Dartmouth College CS 276 HW1

from FoxProblem import FoxProblem
from uninformed_search import bfs_search, dfs_search, ids_search

# Run the searches.
#  Each of the search algorithms return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.

## simple test
problem331 = FoxProblem((3, 3, 1))
print(bfs_search(problem331))
print(dfs_search(problem331))
print(ids_search(problem331))

## no solution test
problem551 = FoxProblem((5, 5, 1))
print(bfs_search(problem551))
print(dfs_search(problem551))
print(ids_search(problem551))

## more fox than chicken test
problem651 = FoxProblem((6, 5, 1))
print(bfs_search(problem651))
print(dfs_search(problem651))
print(ids_search(problem651))

## more chickens than fox test
problem14151 = FoxProblem((14, 15, 1))
print(bfs_search(problem14151))
print(dfs_search(problem14151))
print(ids_search(problem14151))

problem781 = FoxProblem((7, 8, 1))
print(bfs_search(problem781))
print(dfs_search(problem781))
print(ids_search(problem781))

## bigger boats test
problem3313 = FoxProblem((3, 3, 1), boat_size=3)
print(bfs_search(problem3313))
print(dfs_search(problem3313))
print(ids_search(problem3313))

problem8814 = FoxProblem((8, 8, 1), boat_size=4)
print(bfs_search(problem8814))
print(dfs_search(problem8814))
print(ids_search(problem8814))