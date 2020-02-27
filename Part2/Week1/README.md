# General
## Overview

* general strategy for searching graphs without doing redundant work
* two most important strategies: BFS, DFS
* BFS in more detail (shortest paths, connected components )
* DFS in more detail (sequence tasks in a way that respects precedent constraints)
* description and analysis of algo for computing Strongly Connected Components (SCC's)

## Homework

* graph representations
* graph search

# Notes
## Graph search

### Motivations
* check if a network is connected (can get from any A to any B)
* social/movie networks (Bacon number, min number of hops  to get to Kevin Bacon)
* questions about connectivity
* driving directions

* more generic: a path is just a sequence of decisions taking one from some state to some other  state. E.g: solving a Sudoku puzzle through a graph of nodes where each node is a partially solved puzzle and we want to solve it without breaking the Sudoku rules.

### Generic graph search

Goals:
* Find everything that is findable from a given vertex.
* Dont explore anything twice

Generic method:

* Remember per node if we have already explored it (territory conquered)
* Mark s explored
* Choose an edge with u and v unexplored
* Mark v explored

Formal claim: All nodes that have been marked explored can be reached from the starting node s


### DFS vs BFS

Two different instantiations with different properties and different applications:

- we can always go to  many different unexplored nodes from the explored nodes, the pattern in choosing the next node to explore determines the instantiation of the algorithm

E.g.: BFS explores the graph in layers
- shortest paths
- SCC's
E.g.: DFS is more aggresive and plunges as deeply as possible only backtracking when absolutely necessary (mazes):
- compute topological ordering of directed acyclic graph
- compute  connected components in directed graphs

###  BFS

- uses queue, allows to push and pop to resp. front and back in constant time.
pseudo

* all nodes initially unexplored
* init Q with S
* while Q != empty:
    * pop node from Q call it v
    * for each edge (v, w)
    * if w unexplored
        * mark w explored
        * push w onto Q

At the end, if v is explored, there is a path from s to v

Runtime of main loop is O(n reachable from s + m reachable from s)

### BFS application to shortest path

* Add each iter, assign dist(v) = w + 1 if w is unexplored
* At the end , dist(v) = i, where v is in the ith layer

Note that the instantiation of the graph search must be BFS in order to get the shortest path.
This is for example not the case for connected components.

### BFS and undirected connectivity

let G = (V, E) be an undirected graph
Connected components = the pieces of G
Formal definition: equivalence classes, must satisfy three properties
* reflexivity: (everything is related to itself, the empty path from a node to itself is always  there)
* symmetry: (if u and v are connected, v and u are connected)
* transitivity: u and v are related and v and w are related so u and w are related.

Applications:

- Compute all connected components
- Clustering

pseudocode 
* mark all nodes unexplored
* label nodes 1 to n
* for i 1  to n 
    * if i not yet explored (in some previous BFS)
        * run BFS(G, i), which explores exactly the connected component of i
        * since it visits every node, it finds the connected component for every node i 


### DFS (aggressive cousin of BFS)

* nice for maze solvers
* topological ordering of a directed graph

* uses a LIFO stack in stead of a Queue (visits the nodes in reverse order of exploring them)

pseudocode (recursive)

function signature DFS(G, v)

* let G = (V, E) with start vertex s
* mark s explored
* for every edge (s, v)
    * if v unexplored
    * DFS(G,  v)


### Topological ordering of directed acyclic graph

* ordering of the vertices of the graph so that all of the directed edges of the graph only go forward in the ordering.
* graph must be acyclic, if G has a directed cycle, there is no topological ordering because there must be a point where the node goes "backward"

**Straightforward solution**

* every directed acyclic graph has at least one sink vertex: a vertex that has no outgoing arcs (directed edge)
* if this was not the case, it would not be acyclic (pigeon hole principle), i.e.: there would be a directed cycle
* the final position in the ordering must be the sink vertex

pseudocode
- let v be a a sink vertex of  G
- set label(v) = n (the final position)
- recurse on G - {v}

observation:
- getting rid of stuff in a directed acyclic graph can not  produce cycles

### Strongly connected components

- regions where we can get from any vertex to any other vertex (can be the whole graph)
- SCCs of a directed graph G are the equivalence classes of the relation u -> v, v -> u (reflexivity, symmetry, transitivity)
- a modified version of DFS is appropriate because:
    - it finds everything findable through a directed path
    - it only finds an SCC if it is (coincidentally) initiated from the correct node
    - this means that it can get a union of SCCs (provides no info about SCCs)
    - therefore a preprocessing step is needed

### Kosarajus two-pass algorithm (DFS with preprocessing step to get SCCs)

Essentially two passes of DFS
runtime O(m+n)

pseudocode

- let Grev = G with all arcs reversed
- run DFS on Grev (can also just run DFS on G in reversed order)
- this run computes an ordering of the nodes that allows the second pass to compute the SCCs
- run DFS on G
- go through vertices in decreasing order of the "finishing time" f(v) of the first DFS run
- SCCs become groups of nodes with the same leader


DFS-loop
- let t = 0, (n nodes processed so far)
- let s = null (the most recent vertex from which a DFS was initiated, computes leaders in second run)
- assume nodes are labelled 1 to n
    - for n down to 0
    - if i not yet explored
        - let s = i
        - DFS(G, i)

DFS
- mark i as explored
- set leader(i) := node s
- for each arc(i, j) in G:
    - if j not yet explored
    - DFS(G, j)

- t++
- set f(i) = t
