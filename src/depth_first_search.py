"""
Depth-first Search (DFS)
------------------------

Depth-first search is a graph traversal algorithm that explores as deep as
possible along each branch before backtracking and traversing other nodes. This
is in contrast to breadth-first search, which explores all nodes at the current
depth level before moving to nodes at the next depth level.

Given the following tree:

       A
     /   \
    B     C
   / \   / \
  D   E F   G

Depth-first search (recursive) would visit the nodes in the following order:

  A → B → D → E → C → F → G

Depth-first search (stack) would visit the nodes in the following order:

  A → C → G → F → B → E → D

These two variations of DFS visit the neighbors of each vertex in the opposite
order.

A stack is used to keep track of the nodes discovered so far along a specified
branch which helps in backtracking of the graph, however, this algorithm can
also be implemented using recursion, in which case, the stack is implicit. To
initiate the algorithm, the root node (when using recursion, this is an
arbitrary node in the graph), is explored by recursively calling DFS on its
children.

When using a stack, the root node is pushed onto the stack. Then, the first
node in the stack is iteratively removed (popped), checked (if searching for a
target), labeled as "visited", and its children are pushed onto the stack. The
algorithm terminates when the stack is empty and all nodes have been visited.

  NOTE: A stack follows LIFO (Last In, First Out).

It should be noted that when using a stack, the node is marked as visited when
it is removed from the stack.

A set of visited nodes is maintained in order to account for graphs with
cycles, undirected graphs, and graphs where nodes have multiple parents. Trees
are acyclic, therefore a set of visited nodes is not necessary.
"""

from collections import deque

from src.shared.nodes import Node, T


def depth_first_search_recursive(root: Node[T]) -> list[T]:
    """
    Traverses a graph from `root` using depth-first search.

    This function merely traverses the graph. In practical applications, the
    algorithm is used to search for a target.
    """
    l: list[T] = [root.value]
    visited: set[Node[T]] = {root}

    def dfs(l: list[T], visited: set[Node[T]], root: Node[T] | None) -> None:
        if not root:
            return
        for child in root.children:
            if child not in visited:
                l.append(child.value)
                visited.add(child)
                dfs(l, visited, child)

    dfs(l, visited, root)
    return l


def depth_first_search_iterative(root: Node[T]) -> list[T]:
    """
    Traverses a graph from `root` using depth-first search using a stack.

    This function merely traverses the graph. In practical applications, the
    algorithm is used to search for a target.
    """
    # Create stack, push root.
    l: list[T] = []
    stack = deque([root])
    visited: set[Node[T]] = set()

    while stack:
        curr: Node[T] = stack.pop()
        l.append(curr.value)
        if curr not in visited:
            visited.add(curr)
            for child in curr.children:
                stack.append(child)

    return l
