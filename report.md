# CS276 HW1: Foxes and Chickens
Yuchuan (Helen) Ma, 2024 Fall @ Dartmouth

## Initial discussion and introduction
- Minimal state representations: (3,3,1) - 3 foxes, 3 chickens and boat on the left side
- upper bound on the number of states: 4\*4*2
- or more general: No. of foxes * No. of chickens * side of boat (left or right)
- diagram of state and state transition of (3,3,1)

## Building the model
- FoxProblem is the class for the model
- It's default start state is (3,3,1) with a boat size of 2
- One can change the boat size by specifying it when initializing the class
  - I expanded the problem to make it more general in this aspect
- The `get_successor` method is implemented to generate next states for multiple foxes and chickens with boats in various sizes
  - It determines how many chickens and foxes on the particular side currently with the boat can be transported to the other side
  - then loop through these options in a permutated way, with edge cases checks and checking if the state is safe through helper function `is_safe_state`
- `is_safe_state` checks if a given state is valid:
  - at any given time total number of each should be > 0 and < totals
  - at any given time, if there is any chicken on a side of the river, there has to more chicken than foxes on that side

## SearchSolution class
- a wrapper class that keeps records of the problem, search method, path (start state to goal state)
- a deque is added for faster path-tracking DFS (explained in that section)

## BFS
- the code follows a general structure of standard BFS algorithm, like one you see in CS1 class
- it is implemented along with backtracking/backchaining
  - each node is wrapped in a wrapper class `SearchNode` and has a parent node
  - once we found the end node you can backtrack to the root
  - since it's the first time seeing the end state node, this path is to the shortest path

## Memoizing depth-first search
Q: Does memoizing dfs save significant memory with respect to breadth-first search? Why or why not?
- No, it still memorizes all states visited, like BFS does, so the only difference is that BFS needs additionally memories for a queue to remember the next layers of nodes to visit

## Path-checking depth-first search
- the code checks bases cases including 1) if the current code is the goal state, or 2)  has the current recusion depth exceeds the limit, if passes the checks, then it continues to recurse on child nodes / next states
  - for a specific dfs function call, it increments `nodes_visited` and add its self to the "visiting path" (which is kept with the `SearchSolution` object)
  - if reaches the depth limit, it returns the solution object with empty path, with the `node_visited` count
  - it makes subsequent recursion calls among the next possible states (from list returned by the search problem's `get_successor` function):
    - if the particular state is already visited, skip it
    - the successful solution will be returned back up through the recursion stack
      - and then the current recursion function returns the successful state.
    - if the subsequent recursion doesn't find an answer, but that subsequent call added its self/its node to the "visiting path", so I popped that node off as "backtracking"
      - I used deque for the data structure for the "visiting path" for faster look ups of repeated nodes and deleting the last element for backtracking
- Note: the `nodes_visited` of the final returned `SearchSolution` object is updated and accumulated throughout the recursion calls. It got updated when making every new recursion calls.
- Q: Does path-checking depth-first search save significant memory with respect to breadth-first search?
  - Yes it saves more memory since it is only memorizing the current path (i.e. the path from the root to the current node that is called) while BFS is memorizing all the nodes that are visited. The memory advantage, however, is less so, when the graph/tree is very unbalanced, like a singly linked list, then all nodes will be on the path for DFS call as well as BFS's visited node set. The memory cost becomes similiar.
  - an example of a graph where path-checking dfs takes much more run-time than breadth-first search
    - a path checking dfs search would run from the node to the leaf (as the yellow indicated), while a bfs would be able to reach the goal state by visiting all nodes on the first layer
    - if the graph is very imbalanced and long chains of child nodes, bfs could be faster in cases like this

## Iterative deepening search
- the code iterates a range of depths, and call path-checking dfs with the designated depth limit
- guarantees to return the shortest path since it's eliminating options from low to high, and "forces" normal dfs to reach more nodes within the limit of layers
- I ran a seperate variable `nodes_count` to count nodes visited each iteration and at last return the accumulated sum
- Q: On a graph, would it make sense to use path-checking dfs, or would you prefer memoizing dfs in your iterative deepening search?
  - I would go with path-checking. If the graph has a lot of branches (each node has many children), let's say every node in the graph has n children (e.g. n>=10), ids starts to search thru them (first layer: 10, second layer: 10 * 10 and so on...) Path-checking makes more sense since the number of nodes being recorded is the length of the path (which is at most the current iteration depth) and memoirzing dfs would have used memory to remember all nodes (10+10*10+more)
  - path-checking might takes more time depends on the implementation, since you need to backtrack (delete invalid node options) as well which could be O(n) if you are using a list, while memoizing uses a set and average to O(1) for checking repeats and no need to delete anything

## Discussion question: Lossy chickens and foxes
What if, in the service of their community, some chickens were willing to be made into lunch? Let us design a problem where no more than E chickens could be eaten, where E is some constant.
- state definition: (No. fox, No. chicken, boat on which side of the river, E) where the boat's side is either 1 or 0 (right or left), and E is the number of chickens that still can be eaten to have a valid state(or game)
- upper bond of this new state definition: (No. fox+1) * (No. chicken+1) * 2 * (E+1)
- the current solution needs to be changed in following ways:
  - `FoxProblem` class initiation, it's start and end goal states and `goal_test` needs to be updated accordingly with the new state variable E
  - the `get_successor` needs to be updated with new possible actions, including looping new successor states that has `e` where 0 <= e <= E
  - the rest should be similiar
- my thought is that the `get_successor` for lossy chicken and foxes is similiar to my current implementation, with the varying boat size
  - I bounded the number of animals on the boat by 1 to boat size
  - with E it would be bounded to 1 to E (numbers of chicken could still be eaten, so 0 means it's invalid)