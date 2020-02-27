import argparse
import random
from attr import dataclass
from typing import Dict, List


parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str)
parser.add_argument('--n_runs', type=int, default=1)


@dataclass
class Edge:
    pk: int
    u: int
    v: int

    def __eq__(self, other):
        return set([self.u, self.v]) == set([other.u, other.v])

    def update(self, old, new):
        if old == self.u:
            self.u == new
        elif old == self.v:
            self.v == new
        else:
            raise Exception("invalid edge state")
        return self


@dataclass(frozen=True, eq=True)
class Vertex:
    label: int
    edges: List[int]


def contract(G: (Dict[int, Vertex], Dict[int, Edge])):
    """Randomly contract G until only two vertices are left

    Parameters:
        G : (Dict[Vertex], Dict[Edge])

    Returns:
        size of cut : int
            The number of edges between the remaining vertices
    """
    V, E = G
    n = len(V)
    while n > 2:
        edge = E.pop(random.choice(list(E.keys())))
        u, v = V.pop(edge.u), V.pop(edge.v)

        uv_edges = []
        for edge_ref in v.edges:
            _edge = E[edge_ref]
            if edge == _edge:
                E.pop(_edge.pk)
            else:
                _edge.update(v.label, u.label)
                uv_edges.append(_edge)

        for edge_ref in u.edges:
            _edge = E[edge_ref]
            if edge == _edge:
                E.pop(_edge.pk)

        uv = Vertex(
            label=u.label,
            edges=uv_edges
        )
        V[u.label] = uv
        n -= 1

    u, v = V
    for edge_ref in u.edges + v.edges:
        edge = E[edge_ref]
        assert set([u.label, v.label]) == set([edge.u, edge.v])

    return len(u.edges) + len(v.edges)


def graph_from_file(infile):
    V, E = {}, {}
    edge_id = 0
    with open(infile) as fp:
        for line in fp:
            payload = [int(x) for x in line.strip().split()]
            u, adjacent = payload[0], payload[1:]
            u_edges = []

            for v in adjacent:
                edge = Edge(
                    pk=edge_id,
                    u=u,
                    v=v,
                )
                u_edges.append(edge)
                edge_id += 1

            V[u] = Vertex(
                label=u,
                edges=[x.pk for x in u_edges],
            )
            E.update({x.pk: x for x in u_edges})
    return (V, E)


def best_of(n_runs, G):
    _min = -1
    while n_runs:
        _min = min(contract(G), _min)
        n_runs -= 1
    return _min


if __name__ == '__main__':
    args = parser.parse_args()

    G = graph_from_file(args.infile)
    print(best_of(args.n_runs, G))
