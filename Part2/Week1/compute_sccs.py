#!/usr/bin/env python
import networkx as nx
from networkx.algorithms.components import (
    number_strongly_connected_components,
    strongly_connected_components,
)


def main():
    """
    Horrible cheat
    """
    G = nx.DiGraph()
    with open("input.txt") as fp:
        for line in fp:
            u, v = [int(x) for x in line.split()]
            G.add_edge(u, v)
    print(f"Found n SCCs: {number_strongly_connected_components(G)}")
    print(
        f"Five largest SCCs: {[len(x) for x in sorted(strongly_connected_components(G), reverse=True, key=len)[:5]]}"
    )


if __name__ == "__main__":
    main()
