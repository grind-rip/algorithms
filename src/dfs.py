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

Depth-first search would visit the nodes in the following order:

  A → B → D → E → C → F → G

A stack is used to keep track of the nodes discovered so far along a specified
branch which helps in backtracking of the graph, however, this algorithm can
also be implemented using recursion, in which case, the stack is implicit. To
initiate the algorithm, the root node (when using recursion, this is an
arbitrary node in the graph), is explored by recursively calling DFS on its
children.

When using a stack, the root node is pushed onto the stack. Then, the first
node in the stack is iteratively removed (popped), checked (if searching for a
target), and its children are pushed onto the stack and labeled as "visited".
The algorithm terminates when the stack is empty and all nodes have been
visited.

  NOTE: A stack follows LIFO (Last In, First Out).

It should be noted that when using a stack, the node is marked as visited when
it is removed from the stack.
"""

from collections import deque

from .shared.node import Node, T


def dfs(root: Node[T], output: bool = False) -> None:
    """
    Traverses a graph from 'root' using depth-first search.

    This function merely traverses the graph. In practical applications, the
    algorithm is used to search for a target.
    """
    # Mark root as visited.
    root.visited = True

    for child in root.children:
        if output:
            print(f"Visiting node: {child.value}")
        if not child.visited:
            dfs(root=child, output=output)


def dfs_stack(root: Node[T], output: bool = False) -> None:
    """
    Traverses a graph from 'root' using depth-first search using a stack.

    This function merely traverses the graph. In practical applications, the
    algorithm is used to search for a target.
    """
    # Create stack, push root.
    stack = deque([root])

    while stack:
        curr: Node[T] = stack.pop()
        if output:
            print(f"Visiting node: {curr.value}")
        if not curr.visited:
            curr.visited = True
            for child in curr.children:
                stack.append(child)
