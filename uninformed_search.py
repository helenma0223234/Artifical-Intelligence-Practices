# Yuchuan Ma
# Sep 18, 2023
# Dartmouth College CS 276 HW1

from collections import deque
from SearchSolution import SearchSolution

# A SearchNode class to wrap state objects,
#  to keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    """
    Each search node except the root has a parent node
    and all search nodes wrap a state object
    """

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    # print itself only (for printing solution)
    def __str__(self):
        return self.state

def bfs_search(search_problem):
    """
    Find shortest path from start state to goal state of a FoxesProblem class object

    :param search_problem: FoxesProblem
    :type FoxProblem

    :return: solution calss with the shortest path stored in its parameter(s)
    :rtype: SearchSolution
    """
    root = SearchNode(search_problem.start_state, None)
    # que to store next nodes to visit
    que = deque([root])
    # set to keep visited nodes to prevent repeats
    visited = set()
    visited.add(root.state)
    # create solution class for record
    sol = SearchSolution(search_problem, "BFS")

    while que:
        curr = que.popleft()
        sol.nodes_visited += 1
        if search_problem.goal_test(curr.state):
            # start backchaining with helper funct
            return backchain(curr, search_problem, "BFS", sol.nodes_visited)
        else:
            # get all child nodes
            successors = search_problem.get_successors(curr.state)
            for succ in successors:
                if succ not in visited:
                    visited.add(succ)   # remember it
                    que.append(SearchNode(succ, curr))
    return sol


def backchain(end_node, search_problem, search_method, nodes):
    """
    Helper function for BFS, to find the path to the end node

    :param end_node: a node at the end of a path
    :type SearchNode

    :return: solution with final path and accumulated nodes count and other params
    :rtype: SearchSolution
    """
    curr = end_node
    path = [curr.state]
    while curr.parent:
        path.append(curr.parent.state)
        curr = curr.parent
    path.reverse()

    # create new solution object for better printed result
    solution = SearchSolution(search_problem, search_method)
    solution.path = path
    solution.nodes_visited = nodes
    return solution

def dfs_search(search_problem, depth_limit=100, node=None, solution=None, search_method="DFS"):
    """
    Finds a path from start state to goal state of a FoxesProblem class object

    :param search_problem: FoxesProblem
    :type FoxProblem
    :param depth_limit: layers/calls of dfs along this branch of the graph left
    :type int
    :param node: current node being searched
    :type SearchNode
    :param solution: solution of the search problem
    :type SearchSolution

    :return: solution with the found path, or None for no solution found
    :rtype: SearchSolution
    """

    ### base case
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, search_method)

    # update the solution states for current call
    solution.nodes_visited += 1
    solution.path_que.append(node.state)

    if search_problem.goal_test(node.state):
        # if found a path, convert the deque into a list, which is the path
        solution.path = list(solution.path_que)
        return solution
    # if still has tries, run it
    if depth_limit == 0:
        sol = SearchSolution(search_problem, solution.search_method)
        sol.nodes_visited = solution.nodes_visited
        return sol

    ### recursive calls
    successors = search_problem.get_successors(node.state)
    for succ in successors:
        # path check, no repeat visit
        if succ in solution.path_que:
            continue
        # run dfs on child nodes
        else:
            successor = SearchNode(succ, node)
            find = dfs_search(search_problem, depth_limit-1, successor, solution, search_method)
            if len(find.path) > 0:
                find.path = list(find.path_que)     # convert deque into list and store in path
                return find
            else:
                solution.path_que.pop()
    # no solution found
    sol = SearchSolution(search_problem, solution.search_method)
    sol.nodes_visited = solution.nodes_visited
    return sol


def ids_search(search_problem, depth_limit=100):
    """
        Finds a shortest path from start state to goal state of a FoxesProblem class object with iterative DFS

        :param search_problem: FoxesProblem
        :type FoxProblem
        :param depth_limit: max limit the depth of the depth-first search
        :type int

        :return: solution with the found path, or None for no solution found
        :rtype: SearchSolution
        """
    nodes_count = 0
    # run iterations of dfs
    for depth in range(depth_limit):
        find = dfs_search(search_problem, depth, None, SearchSolution(search_problem, "ids"))
        nodes_count += find.nodes_visited
        # check if it finds the solution
        if len(find.path)==0:
            continue
        else:
            # accumulate the nodes count
            find.nodes_visited = nodes_count
            return find
    # no solution found
    sol = SearchSolution(search_problem, "ids")
    sol.nodes_visited = nodes_count
    return sol
