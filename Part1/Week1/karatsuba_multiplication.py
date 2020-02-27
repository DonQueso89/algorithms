#!/usr/bin/env python
import argparse


parser = argparse.ArgumentParser(description="Karatsuba integer multiplication")
parser.add_argument("a", type=int)
parser.add_argument("b", type=int)


def main(x, y):
    """
    xy = 10^n ac + 10^(n/2)(ad + bc) + bd
    where n = len(y)
    """
    ny = len(str(y))
    nx = len(str(y))
    a = x - (x % nx // 2)
    b = x - a
    c = y - (y % ny // 2)
    d = y - c

    first_term = a * c
    second_term = b * d
    third_term = ((a + b) * (c + d)) - (first_term + second_term)

    return first_term + second_term + third_term


if __name__ == '__main__':
    args = parser.parse_args()
    a, b = args.a, args.b
    result = main(a, b)
    print("Karatsuba says: {:d}\nReality says: {:d}".format(result, a * b))
