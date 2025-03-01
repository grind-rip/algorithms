"""
Three-way Partition
-------------------

Three-way partition, also known as the Dutch national flag problem, is an
algorithm for partitioning three types of elements (those less than a given
key, those equal to a given key, and those greater than a given key). Three-way
partitioning can be done in linear time.

The method for performing a three-way partition is to have the top partition
grow down from the top of the array, the bottom partition grow up from the
bottom of the array, and keep the middle partition just above the bottom
partition.

  | Bottom | Middle | Top |

To do this, we maintain the indices of three locations:
  1. The top of the bottom partition (i)
  2. The top of the middle partition (j)
  3. The bottom of the top partition (k)

So, for an array A of size n:
  * Elements from A[0...i] not including i are less than the given key.
  * Elements from A[i...j] not including j are equal to the given key.
  * Elements from A[j...k] are yet to be sorted.
  * Elements from A[k+1...n-1] are greater than the given key.

This invariant holds at the end of each loop. If j >= k, the array has been
fully partitioned.

Initial:

  | Bottom | Middle | Top |        i = 0
  ↑                       ↑        j = 0
  i,j                     k        k = n - 1

Final:

  | Bottom | Middle | Top |
           ↑       ↑↑
           i       kj

At each step, examine the element at j, the top of the middle partition. If
it belongs to the top partition (i.e., is greater than the given key), swap it
with the element at k, the bottom of the top partition. If it belongs to the
bottom partition (i.e., is less than the given key), swap it with the element
at i, the top of the bottom partition.
"""


def three_way_partition(arr: list[int], key: int) -> None:
    """
    Three-way partitioning algorithm. `key` is the middle value.
    """
    i, j, k = 0, 0, len(arr) - 1

    while j <= k:
        if arr[j] > key:
            # Swap A[j] with A[k], decrement k. NOTE: Do not increment j, since
            # elements between j and k are yet to be sorted.
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        elif arr[j] < key:
            # Swap A[j] with A[i], increment i and j. NOTE: Here, we *do*
            # increment j, since A[j] is now sorted.
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        else:
            j += 1
