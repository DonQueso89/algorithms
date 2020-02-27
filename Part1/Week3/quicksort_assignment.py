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
parser.add_argument("infile", type=str)


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

    Partitions in O linear time without allocating memory
    beyond the original arr
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


def quicksort(arr, pivot_func, low=0, high=None, num_cmps=0):
    # pick element in arr
    # rearrange so that:
    # left of pivot < pivot
    # right of arr > pivot
    if high is None:
        high = len(arr)
    if high - low <= 1:
        return num_cmps

    num_cmps += (high - low - 1)
    pivot = pivot_func(arr, low, high)
    pivot = partition(arr, pivot, low, high)

    num_cmps = quicksort(arr, pivot_func, low, pivot, num_cmps)  # recurse left
    return quicksort(arr, pivot_func, pivot + 1, high, num_cmps)  # recurse right


if __name__ == "__main__":
    args = parser.parse_args()
    arr = [int(x) for x in open(args.infile).read().splitlines()]
    _orig = arr[:]
    for pivot_func in [
        lambda a, l, h: l,
        lambda a, l, h: h - 1,
        lambda a, l, h: sorted([
            (a[l], l),
            (a[h-1], h-1),
            (a[l:h][((h - l - 1) // 2) or 1], l + ((h - l - 1) // 2) or 1),
            ],
            key=lambda k: k[0]
        )[1][1]
    ]:
        print(quicksort(arr, pivot_func, 0, len(arr)))
        arr = _orig
        _orig = _orig[:]
