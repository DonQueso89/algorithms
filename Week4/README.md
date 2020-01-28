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

the number of edges does not decrease constantly, but the number of vertices does (edges can decrease faster because of self-loops.

the degree of each vertex is at least k, each vertex defines a cut of at least degree k.
Therefore, k is the lower bound on the number of incident edges on each vertex in G.
Also, for any undirected graph, the sum of the degrees of all vertices is exactly double the number of edges.

Sum(degree(v)) = 2m
Sum(degree(v)) >= kn
therefore
2m  >= kn
or
m >= kn/2

Coming back to the probability of contracting an edge in the set of crossing edges of the minimum cut, we can now set an upper bound:

for the first iteration:
we know that Pr[S1] = k/m 
and since m >= kn/2
we can put an upper bound on Pr[S1]
Pr[S1] <= k/kn/2
or
Pr[S1] <= 2/n

for the second iteration:
Pr[notS1 & notS2] = Pr[notS2 | notS1] * Pr[notS1]

Pr[notS1] >= (1 - 2/n)
Pr[notS2 | notS1] >= (1 - 2 / (n - 1))

this can be extrapolated to any iteration,
for the last iteration:

Pr[notS1 & notS2 ... notSn-2] = Pr[notS1] * Pr[notS2 | notS1] * ... Pr[notSn-2 | notS1 & notS2 .... notSn-3] >= (1 - 2/n) * (1 - 2/n-1) * (1 - 2/n-2) * (1 - 2/n-(n-3))

=
(n-2)/n * (n-3)/(n-1) ... * 2/4 * 1/3

massive cancellation follows:

2/n(n-1) >= 1/n^2

this is a pretty low success probability but it is much better than picking a cut at random (since there are an exponential number of cuts in a graph). 

Repeated trials can turn a low success probability into a low failure probability.

Solution: run the basic algorithm a large number of times and remember the smallest cut found.

the question is then, if we run n trials on G with v vertices what is the chance that every trial Ti fails?
Pr[trial Ti fails] <= (1 - (1/v^2))
therefore:
Pr[all n trials fail] <= (1 - (1/v^2))^n
Pr[the algorithm succeeds at least once] >= 1 - ((1 - (1/v^2)) ^ n)

to answer how big n needs to be, we recall that for all real numbers x
1+x <= e^x

therefore we can say (substituting n with v^2)
Pr[all fail] <= (e^(-1/n^2)) ^ n^2 = 1/e

### Running time

Polynomial in n and m but slow

### Problem set 4

1) how many minimum cuts in  a tree G with n nodes (n - 1 edges)

in a tree, every node except the root can individually form a side of a minum cut, so it is n - 1

2) the number of minimum cuts of every graph is bounded above by n^2 and below by n choose 2 so the probability of hitting a specific min cut (A, B) of G is bounded above by 1/n choose 2 and bounded below by 1/n^2

3) 
plugging in some values for sigma, gives:
if sigma == 1, the chance is 1
if sigma == .5, the chance is .75
if sigma == .65, the chance is .30

the A2 is A1 * sigma if we dont exceed 1 - sigma on either side; 
so the probability is 1 - 2 * (1 - sigma)
or
2 * sigma - 1

4) let sigma be .75
in the worst case, we are looking for the nth statistic and we keep choosing the pivot at the first quartile. In this case we need to recurse log(1/n, .75) times to get to that element
written differently
- log(n) / log(.75)

5) If s and t are on the respective sides of the "real" minimum cut, the subroutine solves the "real" minimum cut problem, but we can not assume this. To know for sure, we need to call the subroutine an additional amount of times to rule out the possibility of being able to find a better mininimum cut outside of the "s and t" minimum cuts.

In other words, we need to ensure that if the algorithm can fail, it needs to fail a significant number of times for us to provide the "real" minimum cut.
