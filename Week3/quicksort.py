import argparse
from random import randint


parser = argparse.ArgumentParser()
parser.add_argument('ints', nargs='+', type=int)


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


if __name__ == '__main__':
    args = parser.parse_args()
    print(quicksort(args.ints, 0, len(args.ints)))
