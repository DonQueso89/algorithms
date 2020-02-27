import random
from typing import List


choose_pivot = random.randint


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, pivot, low, high):
    """
    invariant: arr[0] == pivot
    [p: < p | > p | ? ]

    i delineates split between < p and > p
    j delineates what we've seen

    Partitions in O linear time
    """
    e = arr[pivot]
    # preprocess
    if pivot != low:
        swap(arr, low, pivot)

    i = low + 1
    j = low + 1
    while j < high:
        if arr[j] < e:
            swap(arr, i, j)
            i += 1  # allocate extra space in [ < p ]
        j += 1

    # swap pivot with last elem in [ < p ]
    swap(arr, low, i - 1)
    return i - 1


def _rselect(A: List, low: int, high: int, i: int) -> int:
    """Find the ith order statistic in A.

    This is essentially a modified version of Quicksort in which we only recurse to
    the side where the ith order statistic is located until the index of the pivot
    equals the one that we're looking for.

    Since the expected running time of this algorithm is heavily influenced by the
    choice of pivot (can get up to n**2 if we're very unlucky, a possible optimisation
    is the median of medians.

    Parameters
    ----------
        A : List
        low : int
            the current lower bound
        high : int
            the current upper bound
        i : int
            the order of the search statistic - 1

    Returns
    -------
        The value of the ith order statistic

    Examples
    --------
    >>> _rselect(list(range(11)), 0, 11, 2)
    2
    >>> _rselect(list(range(10)), 0, 10, 4)
    4
    >>> _rselect([0], 0, 1, 0)
    0
    >>> _rselect([445, 356, 703, 453], 0, 4, 1)
    445
    """
    if high - low == 1:
        return A[i]

    pivot = choose_pivot(low, high - 1)  # inclusive
    pivot = partition(A, pivot, low, high)

    if pivot == i:
        return A[pivot]
    if i < pivot:
        return _rselect(A, low,  pivot, i)
    if i > pivot:
        return _rselect(A, pivot + 1, high, i)


def rselect(A, i):
    return _rselect(A, 0, len(A), i - 1)
