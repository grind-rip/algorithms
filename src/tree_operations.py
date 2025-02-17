"""
Tree Operations
---------------

Common tree operations involve searching, inserting, and deleting nodes in the
tree. For binary trees, these operations require simple pointer manipulation.
For binary search trees, however, the invariant-the key of each internal node
must be greater than all the keys in the node's left subtree and less than all
the keys in the node's right subtree-must be maintained, making the operations
slightly more involved.

Common operations
-----------------
For binary trees:
* Enumerate all the nodes in the tree (traversal).
* Calculate the size of the tree.
* Calculate the height of the tree.
* Search for a node.
* Insert a node.
* Delete a node.
* Find the lowest common ancestor of two nodes.

For binary search trees:
* Validate the binary search tree.
* Get the min node.
* Get the max node.
"""

from collections import deque

from src.shared.tree_node import T, TreeNode


def depth_first_search(root: TreeNode[T]) -> list[T]:
    """
    Enumerate all the nodes in the tree (depth-first traversal).
    """
    l: list[T] = []

    def dfs(root: TreeNode[T] | None) -> None:
        if not root:
            return None
        l.append(root.value)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return l


def breadth_first_search(root: TreeNode[T]) -> list[T]:
    """
    Enumerate all the nodes in the tree (breadth-first traversal).
    """
    l: list[T] = []
    queue: deque[TreeNode[T]] = deque([root])

    while queue:
        curr: TreeNode[T] = queue.popleft()
        l.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return l


def tree_size(root: TreeNode[T] | None) -> int:
    """
    Calculate the size of the tree.
    """
    if not root:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


def tree_height(root: TreeNode[T] | None) -> int:
    """
    Calculate the height of the tree.
    """
    if not root:
        return -1
    lh = tree_height(root.left)
    rh = tree_height(root.right)
    return 1 + max(lh, rh)


def bst_search_recursive(root: TreeNode[T] | None, target: T) -> TreeNode[T] | None:
    """
    Return the node with key 'target' in a binary search tree, otherwise return
    None (recursive).
    """
    if not root:
        return None

    if root.value > target:
        return bst_search_recursive(root.left, target)
    if root.value < target:
        return bst_search_recursive(root.right, target)

    return root


def bst_search_iterative(root: TreeNode[T] | None, target: T) -> TreeNode[T] | None:
    """
    Return the node with key 'target' in a binary search tree, otherwise return
    None (iterative).
    """
    while root:
        if root.value > target:
            root = root.left
        elif root.value < target:
            root = root.right
        else:
            return root
    return None


def bst_min(root: TreeNode[T]) -> TreeNode[T]:
    """
    Get the min node in a binary search tree.
    """
    while root.left:
        root = root.left
    return root


def bst_max(root: TreeNode[T]) -> TreeNode[T]:
    """
    Get the max node in a binary search tree.
    """
    while root.right:
        root = root.right
    return root


def bst_insert_recursive(root: TreeNode[T] | None, target: T) -> TreeNode[T]:
    """
    Insert a node into a binary search tree (recursive).

    In order to preserve the binary search tree property, nodes are always
    inserted as leaf nodes.

    If `target` already exists in the tree, the tree is left unchanged.

    Returns the inserted node.
    """
    if not root:
        return TreeNode(value=target)

    if root.value == target:
        return root
    elif root.value > target:
        node = bst_insert_recursive(root.left, target)
        if not root.left:
            root.left = node
        return node
    else:
        node = bst_insert_recursive(root.right, target)
        if not root.right:
            root.right = node
        return node


def bst_insert_iterative(root: TreeNode[T] | None, target: T) -> TreeNode[T]:
    """
    Insert a node into a binary search tree (iterative).

    In order to preserve the binary search tree property, nodes are always
    inserted as leaf nodes.

    If `target` already exists in the tree, the tree is left unchanged.

    Returns the inserted node.
    """
    # A pointer to the previous node is maintained and the node is inserted
    # accordingly.
    prev: TreeNode[T] | None = None
    curr: TreeNode[T] | None = root

    while curr:
        prev = curr
        if curr.value > target:
            curr = curr.left
        elif curr.value < target:
            curr = curr.right
        else:
            return curr

    node = TreeNode(value=target)
    if not prev:
        return node
    elif prev.value > target:
        prev.left = node
    else:
        prev.right = node

    return node
