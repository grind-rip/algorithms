"""
Tree Traversal
--------------

Tree traversal is the process of visiting each node in a tree exactly once.
Such traversals are classified by the order in which the nodes are visited.
There are two main tree traversals: depth-first and breadth-first search.
Additionally, depth-first search can be done pre-order, post-order, and
in-order.

The following tree is used for example outputs:

                                       A
                                       ●
                                     /   \
                                   B       C
                                   ●       ●
                                 /   \   /   \
                                D     E F     G
                                ●     ● ●     ●


Depth-first search
------------------
Depth-first search explores a branch of the tree as deeply as possible before
backtracking and moving on to the next branch. Depth-first search can be
implemented iteratively using a stack or recursively, in which case the stack
is implicit via the call stack. No single traversal order (pre-order,
post-order, or in-order) uniquely identifies the structure of a tree.
Therefore, to uniquely serialize a tree, you generally need two traversals (for
example, pre-order and in-order, or post-order and in-order).

Pre-order
---------

A → B → D → E → C → F → G

1. Visit the current node.
2. Recursively traverse the current node's left subtree.
3. Recursively traverse the current node's right subtree.

Pre-order traversal produces an ordering where each parent appears before its
children—this property resembles a topological ordering in graphs.

Post-order
----------

D → E → B → F → G → C → A

1. Recursively traverse the current node's left subtree.
2. Recursively traverse the current node's right subtree.
3. Visit the current node.

Post-order traversal can be useful for obtaining the postfix expression of a
binary expression tree.

In-order
--------

D → B → E → A → F → C → G

1. Recursively traverse the current node's left subtree.
2. Visit the current node.
3. Recursively traverse the current node's right subtree.

In-order traversal is very commonly used on binary search trees because it
returns values from the underlying set in order, according to the comparator
that set up the binary search tree.

NOTE: Pre-, post-, and in-order traversals can all be done in reverse as well.

Breadth-first search
--------------------

A → B → C → D → E → F → G

With breadth-first search (sometimes called level-order traversal), each node
at a given depth (or level) is visited before moving on to the next level.
Breadth-first search is typically implemented iteratively using a queue.
"""

from collections import deque

from src.shared.tree_node import T, TreeNode


def depth_first_search_recursive_pre_order(node: TreeNode[T]) -> list[T]:
    """
    Traverses a tree recursively using depth-first search in pre-order.
    """
    l: list[T] = []

    def dfs(l: list[T], node: TreeNode[T] | None) -> None:
        if not node:
            return
        l.append(node.value)
        dfs(l, node.left)
        dfs(l, node.right)

    dfs(l, node)
    return l


def depth_first_search_iterative_pre_order(node: TreeNode[T]) -> list[T]:
    """
    Traverses a tree iteratively using depth-first search in pre-order.
    """
    l: list[T] = []
    stack: deque[TreeNode] = deque()
    stack.append(node)

    while stack:
        curr = stack.pop()
        l.append(curr.value)
        # A stack is last in, first out (LIFO). Therefore, if we want to visit
        # the left child before the right child, the right child needs to be
        # pushed onto the stack first.
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return l


def depth_first_search_recursive_post_order(node: TreeNode[T]) -> list[T]:
    """
    Traverses a tree recursively using depth-first search in post-order.
    """
    l: list[T] = []

    def dfs(l: list[T], node: TreeNode[T] | None) -> None:
        if not node:
            return
        dfs(l, node.left)
        dfs(l, node.right)
        l.append(node.value)

    dfs(l, node)
    return l


def depth_first_search_iterative_post_order(node: TreeNode[T]) -> list[T]:
    """
    Traverses a tree iteratively using depth-first search in post-order.
    """
    l: list[T] = []
    stack: deque[TreeNode] = deque()
    curr: TreeNode | None = node
    last: TreeNode | None = None

    # With post-order, we only visit a node after the left and right nodes have
    # been visited. To accomplish this, we first go as far left as possible by
    # pushing left nodes onto the stack. This process terminates when a leaf
    # node is reached. We visit this node and pop it from the stack. Next, we
    # need to backtrack in order to visit either the right or root node. To
    # determine what we should do, we keep a reference to the last visited
    # node. If the last visited node was the left node, we start the process
    # from the beginning with the right node as our new root. If the last
    # visited node was the right node, we know that both the left and right
    # nodes have been visited, so we can now visit the root node.
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        peek = stack[-1]
        if peek.right and peek.right != last:
            curr = peek.right
        else:
            l.append(peek.value)
            last = stack.pop()

    return l


def depth_first_search_recursive_in_order(node: TreeNode[T]) -> list[T]:
    """
    Traverses a tree recursively using depth-first search in in-order.
    """
    l: list[T] = []

    def dfs(l: list[T], node: TreeNode[T] | None) -> None:
        if not node:
            return
        dfs(l, node.left)
        l.append(node.value)
        dfs(l, node.right)

    dfs(l, node)
    return l


def depth_first_search_iterative_in_order(node: TreeNode[T]) -> list[T]:
    """
    Traverses a tree iteratively using depth-first search in in-order.
    """
    l: list[T] = []
    stack: deque[TreeNode] = deque()
    curr: TreeNode | None = node

    # With in-order, we visit a node after the left node has been visited, but
    # before the right. To accomplish this, we first go as far left as possible
    # by pushing left nodes onto the stack. This process terminates when a leaf
    # node is reached. We visit this node and pop it from the stack. We repeat
    # the process with the first non-null right node, otherwise we continue
    # popping nodes from the stack.
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        l.append(curr.value)
        curr = curr.right

    return l


def breadth_first_search(node: TreeNode[T]) -> list[T]:
    """
    Traverses a tree using breadth-first search.
    """
    l: list[T] = []
    queue: deque[TreeNode] = deque()
    queue.append(node)

    while queue:
        curr = queue.popleft()
        l.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return l
