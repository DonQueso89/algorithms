#!/usr/bin/env python
import argparse
from random import randint as rnd


parser = argparse.ArgumentParser()
parser.add_argument('ints', nargs='+', type=int)


def quicksort(numbers, low, high):
    if low >= high:
        return

    pivot_idx = rnd(low, high)
    pivot = numbers[pivot_idx]
    # partition
    for i in range(low, high + 1):
        n = numbers[i]
        if n <= pivot:
            numbers[i] = pivot
            numbers[pivot_idx] = n
            pivot_idx = i
    print(pivot, numbers)

    quicksort(numbers, low, pivot_idx - 1)  # left
    quicksort(numbers, pivot_idx + 1, high)  # right


if __name__ == '__main__':
    args = parser.parse_args()
    print("Unsorted")
    print(args.ints)
    numbers = args.ints
    quicksort(numbers, 0, len(numbers) - 1)
    print("sorted")
    print(numbers)
