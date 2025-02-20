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


def bst_successor(node: TreeNode[T]) -> TreeNode[T] | None:
    """
    Get the successor of a node in a binary search tree.

    The successor of a node in a binary search tree is the node with the
    smallest key greater than the node's key. This can also be thought of as
    the leftmost node in the node's right subtree. Or, if the node does not
    have a right subtree, the first "zag" in the path from the node to the root
    of the tree. NOTE: The rightmost node in the tree has no successor.

                     ● - node       ● - successor     ●
                      \            / \                 \
                       ●          ●   ●                 ●
                      / \          \                     \
                     ●   ●          ● - node              ● - node
                     ^
                     successor

    1. Leftmost node in the node's right subtree.
    2. First "zag" in the path from the node to the root of the tree.
    3. No successor.
    """
    if node.right:
        return bst_min(node.right)
    prev: TreeNode[T] | None = node.parent
    while prev and node == prev.right:
        node = prev
        prev = prev.parent
    return prev


def bst_predecessor(node: TreeNode[T]) -> TreeNode[T] | None:
    """
    Get the predecessor of a node in a binary search tree.

    The predecessor of a node in a binary search tree is the node with the
    greatest key smaller than the node's key. This can also be thought of as
    the rightmost node in the node's left subtree. Or, if the node does not
    have a left subtree, the first "zig" in the path from the node to the root
    of the tree. NOTE: The leftmost node in the tree has no predecessor.

                     ● - node       ● - predecessor       ●
                    /              / \                   /
                   ●              ●   ●                 ●
                  / \                /                 /
                 ●   ●              ● - node          ● - node
                     ^
                     predecessor

    1. Rightmost node in the node's left subtree.
    2. First "zig" in the path from the node to the root of the tree.
    3. No predecessor.
    """
    if node.left:
        return bst_max(node.left)
    prev: TreeNode[T] | None = node.parent
    while prev and node == prev.left:
        node = prev
        prev = prev.parent
    return prev


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


def bst_delete(root: TreeNode[T] | None, target: T) -> TreeNode | None:
    """
    Delete a node from a binary search tree.

    Deletion is more complicated than insertion, as we must take into account
    three cases:

      1. The node is a leaf.
      2. The node has one child.
      3. The node has two children.

    For case 1, we simply remove the node. For case 2, the node is removed and
    the target's child node is moved up to take its place. This is achieved by
    modifying the target's parent node to point to its child node. For case 3,
    we replace the target with the leftmost node in the target's right subtree
    (also known as the node's successor). For case 3, we consider an additional
    two cases:

      3a. The leftmost node is the target's right child.
      3b. The leftmost node is in the target's right subtree.

    For case 3a, the leftmost node simply replaces the target. For case 3b, the
    leftmost node is replaced by its own right child before replacing the
    target.
    """

    def shift(root: TreeNode[T] | None, u: TreeNode, v: TreeNode | None) -> TreeNode | None:
        """
        Shift node v in the place of node u.
        """
        # If u is the root of the tree (i.e., it has no parent), v becomes the
        # new root of the tree.
        if not u.parent:
            root = v
        # Shift node v in the place of node u by connecting u's parent to v.
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v:
            v.parent = u.parent

        return root

    node = bst_search_recursive(root, target)
    if not node:
        return None

    # Case 1 and 2
    if not node.left:
        return shift(root, node, node.right)
    elif not node.right:
        return shift(root, node, node.left)
    # Case 3
    else:
        successor = bst_successor(node)
        # At this point, a successor for the target node must exist.
        assert successor
        if successor.parent != node:
            root = shift(root, successor, successor.right)
            successor.right = node.right
            successor.right.parent = successor
        root = shift(root, node, successor)
        successor.left = node.left
        successor.left.parent = successor

    return root
