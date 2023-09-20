# Yuchuan Ma
# Sep 18, 2023
# Dartmouth College CS 276 HW1

from collections import deque
class SearchSolution:
    def __init__(self, problem, search_method):
        self.problem_name = str(problem)
        self.search_method = search_method
        self.path = []              # record final path result
        self.nodes_visited = 0      # node visited (accumulated)
        self.path_que = deque()     # for efficient path checking

    def __str__(self):
        string = "----\n"
        string += "{:s}\n"
        string += "attempted with search method {:s}\n"

        if self.path is not None and len(self.path) > 0:

            string += "number of nodes visited: {:d}\n"
            string += "solution length: {:d}\n"
            string += "path: {:s}\n"

            string = string.format(self.problem_name, self.search_method,
                self.nodes_visited, len(self.path), str(self.path))
        else:
            string += "no solution found after visiting {:d} nodes\n"
            string = string.format(self.problem_name, self.search_method, self.nodes_visited)

        return string
