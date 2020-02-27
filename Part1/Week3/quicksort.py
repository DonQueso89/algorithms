#!/usr/bin/env python
"""
Considerations on pivot choice, which is crucial for the running time.

- Always taking the first element -> 1 recursive call on the right, equivalent to
  series n + (n - 1) + (n - 2) .... + 1, equivalent to n * (n - 1) / 2 -> O(n^2)

- Always magically choosing the median element -> n log n because we can always split the array in 2. Resulting in linear work for each log2n recursive call

- Choosing a random pivot. Generally: A consistent split of 25-75 is good enough to get n log n complexity. The chance of getting this is ~50% for each recursive call.
"""

import argparse
from random import randint


parser = argparse.ArgumentParser()
parser.add_argument("ints", nargs="+", type=int)


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


def quicksort(arr, low=0, high=None):
    # pick element in arr
    # rearrange so that:
    # left of pivot < pivot
    # right of arr > pivot
    if high is None:
        high = len(arr)
    if high - low <= 1:
        return

    pivot = randint(low, high - 1)
    pivot = partition(arr, pivot, low, high)

    quicksort(arr, low, pivot)  # recurse left
    quicksort(arr, pivot + 1, high)  # recurse right


if __name__ == "__main__":
    args = parser.parse_args()
    print(quicksort(args.ints, 0, len(args.ints)))
