# Graphs and contraction algorithm

## Graphs

a graph consists of a set of vertices V and edges E (each edge is a pair of vertices)

two flavors:
    - Edges are directed (ordered pairs a.k.a. arcs)
    - Edges are undirected

a cut of a graph is a partition of V into two sets A and B
the crossing edges of cut A, B are those with:

- one endpoint in each of (A, B) (undirected)
- tail in A, head in B (directed)


## Minimum cut problem

Problem in the domain of graph partitioning

practical applications: 
- minimum cuts may be used to represent weaknesses in a network (bottlenecks)
- disrupting road networks in the least connected areas
- community detection in social networks (areas that are densely connected amongst themselves but weakly toward the rest of the world)
- image segmentation; each pixel is a vertex and using minimum cuts to see whether pixels are coming from the same object

Given a set of vertices V and undirected edges E
A minimum cut is a cut of V such that the number of crossing edges is minimal.

given a connected undirected graph with n vertices and no parallel edges

min. edges = n - 1
max. edges = n choose 2

dense graphs lean toward n^2 edges
sparse graphs lean toward n edges


## Representing graphs

most common; adjacency matrix:

- undirected graphs A = nxn matrix where n is number of vertices where Aij = 1 has an ij edge
- for parallel edges, the matrix can have any number >= 1 for all the edges ij

space complexity is quadratic in n

adjacency lists

- list of vertices
- list of edges
- each edge points to its vertices
- each vertex points to its edges

space complexity is m + n, linear in n 

choice of representation depends on:
- density of graph
- operations that should be possible on the graph (e.g.: adjacency lists are good for searching a graph)

## The contraction algorithm

- shows that random sampling can be very effective for fundamental graph problems

### Pseudo code

while > 2 vertices remaining
    - pick a remaining edge uniformly at random
    - do the contraction (fuse the two u, v vertices into one vertex)
    - remove self-loops created by the contraction
    - leave parallel edges
return cut represented by final two vertices

NOTE: this does not always return the minimum cut! so we need to know how often it gets
the minimum cut.

## Analysis

- Fix a graph G = (V, E)
- Fix a minimum cut (A, B), no other permutation is acceptable

- let k = the number of crossing edges (A, B) in the minimum cut 
- these edges are the set F

- iff the algorithm only contracts edges in A and B, (i.e.: never contracts an edge in F) we get the minimum cut.
- on the other side, if the algorithm contracts an edge in F, then a node from A and B will be on the same side of the cut, so it will not be the minimum cut

therefore p(output is minimum cut (A,  B)) = p(algo never contracts edge in F)

in other words: compute p(succes on iter i & success on iter i + 1 & succes on iter n)

the chance that a crossing edge is chosen in the 1st iteration (as function of number vertices  n, number edges  m and number crossing edges k) == k/m
