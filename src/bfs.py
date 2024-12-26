"""
Breadth-first Search (BFS)
--------------------------

Breadth-first search is a graph traversal algorithm that explores all nodes at
the current depth level before moving to nodes at the next depth level. This is
in contrast to depth-first search, which explores the node branch as far as
possible before backtracking and traversing other nodes.

Given the following tree:

       A
     /   \
    B     C
   / \   / \
  D   E F   G

Breadth-first search would visit the nodes in the following order:

  A → B → C → D → E → F → G

A queue is used to keep track of nodes to visit. To initiate the algorithm, the
root node is pushed onto the queue. Then, the first node in the queue is
iteratively removed, checked (if searching for a target), and its children are
pushed onto the queue and labeled as "visited". The algorithm terminates when the
queue is empty and all nodes have been visited.

A set of visited nodes is maintained in order to account for graphs with
cycles, undirected graphs, and graphs where nodes have multiple parents.

Finding the shortest path
-------------------------

Breadth-first search can also be used when finding the shortest path from the
root to a target node. This is done by adding the "parent" node to the current
node, then backtracking from the target node once it is found.

The key thing to understand is that BFS will find the shortest path first (the
one with fewest edges), at which point the algorithm terminates and the
shortest path is reconstructed.
"""

from collections import deque
from typing import Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    """
    A generic node with a value of type 'T'.
    """
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.visited: bool = False
        self.parent: Node[T] | None = None
        self.children: list[Node[T]] = []


def bfs(root: Node[T], output: bool = False) -> None:
    """
    Traverses a graph from 'root' using breadth-first search.

    This function merely traverses the graph. In practical applications, the
    algorithm is used to search for a target.
    """
    # Create queue, enqueue root, mark root as visited.
    queue = deque([root])
    root.visited = True

    while queue:
        curr: Node[T] = queue.popleft()
        if output:
            print(f"Visiting node: {curr.value}")
        for child in curr.children:
            if not child.visited:
                queue.append(child)
                child.visited = True


def bfs_shortest_path(root: Node[T], target: Node[T]) -> list[Node[T]]:
    """
    Traverses a graph from 'root' using breadth-first search and returns the
    shortest path to 'target'.

    Returns an empty list if no path is found.
    """
    # Create queue, enqueue root, mark root as visited
    queue = deque([root])
    root.visited = True

    while queue:
        curr: Node[T] | None = queue.popleft()
        if curr == target:
            path: list[Node[T]] = []
            while curr:
                path.append(curr)
                curr = curr.parent
            # Reverse path to get root→target order
            return path[::-1]

        for child in curr.children:
            if not child.visited:
                queue.append(child)
                child.visited = True
                child.parent = curr

    return []
