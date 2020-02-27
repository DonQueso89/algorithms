#!/usr/bin/env python
import argparse


parser = argparse.ArgumentParser(description="Merge sort")
parser.add_argument("intlist", type=int, nargs="+")


def main(intlist):
    if len(intlist) == 1:
        return intlist

    n = len(intlist)
    # sort
    left, right = main(intlist[:n // 2]), main(intlist[n // 2:])
    # merge
    merged = []
    left_elem, right_elem = left.pop(0), right.pop(0)
    while True:
        if left_elem <= right_elem:
            merged.append(left_elem)
            if not left:
                merged.append(right_elem)
                break
            left_elem = left.pop(0)
        else:
            merged.append(right_elem)
            if not right:
                merged.append(left_elem)
                break
            right_elem = right.pop(0)
    return merged + left + right


if __name__ == '__main__':
    args = parser.parse_args()
    result = main(args.intlist)
    print("Merge sort says: {}".format(str(result)))
    assert sorted(args.intlist) == result
