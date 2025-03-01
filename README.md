# algorithms

A collection of algorithms

---

## [Binary Search](./src/binary_search.py)
Binary search is an efficient algorithm for finding a target value in a sorted array.

## [Breadth-first Search (BFS)](./src/breadth_first_search.py)
Breadth-first search is a graph traversal algorithm that explores all nodes at the current depth level before moving to nodes at the next depth level.

## [Cycle Detection](./src/cycle_detection.py)
Cycle detection or cycle finding is the algorithmic problem of finding a cycle in a sequence of iterated function values.

## [Depth-first Search (DFS)](./src/depth_first_search.py)
Depth-first search is a graph traversal algorithm that explores as deep as possible along each branch before backtracking and traversing other nodes.

## [Heapsort](./src/heapsort.py)
Heapsort is a sorting algorithm that first reorganizes an input array into a heap, then repeatedly removes the largest node from that heap, placing it at the end of the array.

## [k-way Merge](./src/k_way_merge.py)
The k-way merge algorithm is a sequence merge algorithm that takes in k sorted lists, typically greater than two, and merges them into a single sorted list. It can be efficiently solved in O(nlog k) time using a heap, where n is the total number of elements for all k lists.

## [kth Smallest (Largest)](./src/kth_smallest.py)
The kth smallest (or largest) problem can be efficiently solved using a max-heap (or min-heap). Maintaining a heap of size k, the kth smallest value is always the root of the max-heap. To retrieve all k smallest elements, simply return the sorted heap.

## [Levenshtein Distance](./src/levenshtein_distance.py)
Levenshtein distance is a string metric for measuring the difference between two sequences. The Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other.

## [Longest Common Subsequence (LCS)](./src/longest_common_subsequence.py)
The longest common subsequence is the longest subsequence that is common to two or more sequences. It can be found using a dynamic programming approach.

## [Longest Increasing Subsequence (LIS)](./src/longest_increasing_subsequence.py)
The longest increasing subsequence is the longest sequence of numbers from an array where each number is greater than the previous one. It can be found using a dynamic programming approach.

## [Maximum Subarray](./src/maximum_subarray.py)
The maximum subarray problem is the task of finding a contiguous subarray with the largest sum, within a given one-dimensional array A[1...n] of numbers. It can be solved in O(n) time and O(1) space.

## [Merge Sort](./src/merge_sort.py)
Merge sort is the quintessential divide-and-conquer sorting algorithm. It follows the premise that an array of one element is considered sorted. Furthermore, it is trivial to sort two sorted arrays.

## [Quickselect](./src/quickselect.py)
Quickselect (also known as Hoare's selection algorithm) is a selection algorithm to find the kth smallest (or largest) element in an unordered list of n elements.

## [Quicksort](./src/quicksort.py)
Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

## [Tree Operations](./src/tree_traversal.py)
Common tree operations involve searching, inserting, and deleting nodes in the tree. For binary trees, these operations require simple pointer manipulation. For binary search trees, however, the invariant-the key of each internal node must be greater than all the keys in the node's left subtree and less than all the keys in the node's right subtree-must be maintained, making the operations slightly more involved.

## [Three-way Partition](./src/three_way_partition.py)
Three-way partition, also known as the Dutch national flag problem, is an algorithm for partitioning three types of elements (those less than a given key, those equal to a given key, and those greater than a given key). Three-way partitioning can be done in linear time.

## [Tree Traversal](./src/tree_traversal.py)
Tree traversal is the process of visiting each node in a tree exactly once. Such traversals are classified by the order in which the nodes are visited. There are two main tree traversals: depth-first and breadth-first search. Additionally, depth-first search can be done pre-order, post-order, and in-order.
