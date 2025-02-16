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
labeled as "visited" and pushed onto the queue. The algorithm terminates when
the queue is empty and all nodes have been visited.

  NOTE: A queue follows FIFO (First In, First Out).

It should be noted that when using a queue, the node is marked as visited when
it is added to the queue.

A set of visited nodes is maintained in order to account for graphs with
cycles, undirected graphs, and graphs where nodes have multiple parents. Trees
are acyclic, therefore a set of visited nodes is not necessary.

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

from src.shared.nodes import Node, T


def breadth_first_search(root: Node[T]) -> list[T]:
    """
    Traverses a graph from `root` using breadth-first search.

    This function merely traverses the graph. In practical applications, the
    algorithm is used to search for a target.
    """
    # Create queue, enqueue root, and add root to `visited`.
    l: list[T] = []
    queue = deque([root])
    visited: set[Node[T]] = {root}

    while queue:
        curr: Node[T] = queue.popleft()
        l.append(curr.value)
        for child in curr.children:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return l


def shortest_path(root: Node[T], target: Node[T]) -> list[T]:
    """
    Traverses a graph from `root` using breadth-first search and returns the
    shortest path to `target`.

    Returns an empty list if no path is found.
    """
    # Create queue, enqueue root, mark root as visited.
    queue = deque([root])
    visited: set[Node[T]] = {root}

    def shortest_path(target: Node[T]) -> list[T]:
        path: list[T] = []
        curr: Node[T] | None = target
        while curr:
            path.append(curr.value)
            curr = curr.parent
        # Reverse path to get root → target order.
        return path[::-1]

    while queue:
        curr: Node[T] = queue.popleft()
        if curr == target:
            return shortest_path(curr)
        for child in curr.children:
            if child not in visited:
                child.parent = curr
                visited.add(child)
                queue.append(child)

    return []


def shortest_path_parent_pointers(root: Node[T], target: Node[T]) -> list[T]:
    """
    Traverses a graph from `root` using breadth-first search and returns the
    shortest path to `target`.

    Returns an empty list if no path is found.

    NOTE: If the node structure does not have a `parent` property, you can use
    a hash map of parent pointers to construct the shortest path.
    """
    # Create queue, enqueue root, mark root as visited.
    queue = deque([root])
    visited: set[Node[T]] = {root}
    parents: dict[Node, Node | None] = {root: None}  # child -> parent

    def shortest_path_parent_pointers(target: Node[T]) -> list[T]:
        path: list[T] = []
        curr: Node[T] | None = target
        while curr:
            path.append(curr.value)
            curr = parents[curr]
        # Reverse path to get root → target order.
        return path[::-1]

    while queue:
        curr: Node[T] = queue.popleft()
        if curr == target:
            return shortest_path_parent_pointers(curr)
        for child in curr.children:
            if child not in visited:
                parents[child] = curr
                visited.add(child)
                queue.append(child)

    return []
