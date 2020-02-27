import argparse


parser = argparse.ArgumentParser()
parser.add_argument("infile", type=str)


def merge_and_count(arr):
    arr = [int(x) for x in arr]
    if len(arr) <= 1:
        return arr, 0
    else:
        split = len(arr) // 2
        left, left_invs = merge_and_count(arr[:split])
        right, right_invs = merge_and_count(arr[split:])

        merged = []
        invs = left_invs + right_invs
        while left and right:
            if right[0] < left[0]:
                merged.append(right.pop(0))
                invs += len(left)
            else:
                merged.append(left.pop(0))
        return merged + left + right, invs


def main(arr):
    """
    >>> main([0, 1, 2, 3, 4, 5])
    0
    >>> main([0, 1, 2, 3, 4, 5, 6])
    0
    >>> main([6, 1, 2, 3, 4, 5, 0])
    11
    >>> main([6, 5, 4, 3, 2, 1, 0])
    21
    """
    return merge_and_count(arr)[1]


if __name__ == '__main__':
    print(
        "Num inversions: {:d}".format(
            main(open(parser.parse_args().infile).read().splitlines())
        )
    )
