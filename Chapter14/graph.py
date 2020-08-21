from Chapter9.priority_queue import AdaptableHeapPriorityQueue, HeapPriorityQueue

class Graph:
    """Representation of a simple graph using an adjacency map."""

    # nested Vertex class
    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            self._element = x
        
        def element(self):
            """Return element associated with this vertex."""
            return self._element
        
        def __hash__(self):     # will allow vertex to be a map/set key
            return hash(id(self))

    # nested Edge class
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            """Do not call constructor directly. Use Graph's insert_edge(u, v, x)."""
            self._origin = u 
            self._destination = v 
            self._element = x
        
        def endpoints(self):
            """Return (u, v) tuple for vertices u and v."""
            return (self._origin, self._destination)
        
        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            return self._destination if v is self._origin else self._origin
        
        def element(self):
            """Return element associated with this edge."""
            return self._element
        
        def __hash__(self):     # will allow edge to be a map/set key
            return hash((self._origin, self._destination))
    

    def __init__(self, directed=False):
        """
        Create an empty graph (undirected, by default).
        Graph is directed if optional paremeter is set to True.
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing
    
    def is_directed(self):
        """
        Return True if this is a directed graph; False if undirected.
        Property is based on the original declaration of the graph, not its contents.
        """
        return self._incoming is not self._outgoing     # directed if maps are distinct
    
    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)
    
    def vertices(self):
        """Return an iteration of all vertives of the graph."""
        return self._outgoing.keys()
    
    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v] for v in self._outgoing))
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2
    
    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values)
        return result 
    
    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        return self._outgoing[u].get[v]     # self._outgoing is a dict
    
    def degree(self, v, outgoing=True):
        """
        Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        """
        Return all (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge 
    
    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {} # need distinct map for incoming edges
        return v
    
    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e 
        self._incoming[v][u] = e 


def DFS(g: Graph, u: Graph.Vertex, discovered: dict):
    """
    Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    `discovered` is a dictionary mapping each vertex to the edge that was used to discover it during the DFS. (u should be "discovered" prior to the call)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):   # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:     # v is an unvisited vertex
            discovered[v] = e       # e is the tree edge that discovered v
            DFS(g, v, discovered)   # recursively explore from v 


# Function to reconstruct a directed path from u to v, given the trace of discovery from a DFS started at u. 
# The function returns an ordered list of vertices on the path.
def construct_path(u: Graph.Vertex, v: Graph.Vertex, discovered: dict):
    path = []
    if v in discovered:
        # we build list from v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]    # find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent 
        path.reverse()              # reorient path from u to v 
    return path 


# Top-level function that returns a DFS forest for an entire graph.
def DFS_complete(g: Graph):
    """
    Perform DFS for entire graph and return forest as a dictionary.
    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None).
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None    # u will be the root of a tree
            DFS(g, u, forest)
    return forest 



# breadth-first search on a graph, starting at a designated vertex s
def BFS(g: Graph, s: Graph.Vertex, discovered: dict):
    """
    Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
    `discovered` is a dictionary mapping each vertex to the edge that was used to discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]             # first level includes only s
    while len(level) > 0:
        next_level = []     # prepare to gather newly found vertices
        for u in level:
            for e in g.incident_edges(u):   # for every outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:     # v is an unvisited vertex
                    discovered[v] = e       # e is the tree edge that discovered v
                    next_level.append(v)    # v will be further considered in next pass
            level = next_level              # relabel 'next' level to become current


# Transitive Closure:
# 传递闭包：通俗的讲就是如果a->b， b->c，那么我们就建立一条a->c的边。
# 将所有能间接相连的点直接相连。 
# Floyd能在O(n^3) 求出一个图的传递闭包。
from copy import deepcopy

def floyd_warshall(g: Graph):
    """Return a new graph that is the transitive closure of g."""
    closure = deepcopy(g)
    verts = list(closure.vertices())    # make indexable list 
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that edge (i, k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge (k, j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        # if (i, j) not yet included, add it to the closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure





def MST_PrimJarnik(g: Graph):
    """
    Compute a minimum spanning tree of weighted graph g.
    Return a list of edges that comprise the MST (in arbitrary order).
    """
    d = {}              # d[v] is bound on distance to tree
    tree = []           # list of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()   # d[v] maps to value (v, e=(u,v))
    pqlocator = {}      # map from vertex to its pq locator

    # for each vertex v of the graph, add an entry to the priority queue,
    # with the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if len(d) == 0:             # the first node
            d[v] = 0                # make it the root
        else:
            d[v] = float('inf')     # positive infinity
        # initialize a priority queue Q with an entry (D[v], (v,None)) for each vertex v,
        # where D[v] is the key in the priority queue, and (v,None) is the associated value.
        pqlocator[v] = pq.add(d[v], (v, None))
    
    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value             # unpack tuple from pq
        del pqlocator[u]            # u is no longer in pq
        if edge is not None:
            tree.append(edge)       # add edge to tree
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:      # thus v not yet in tree
                # see if edge (u,v) better connects v to the growing tree
                wgt = link.element()
                if wgt < d[v]:      # better edge to v?
                    d[v] = wgt      # update the distance 
                    pq.update(pqlocator[v], d[v], (v, link))    # update the pq entry
    return tree 


class Partition:
    """Union-find structure for maintaining disjoint sets."""
    # nested Position class
    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            """Create a new position that is the leader of its own group."""
            self._container = container     # reference to Partition instance
            self._element = e
            self._size = 1
            self._parent = self             # convention for a group leader

        def element(self):
            """Return element stored at this position."""
            return self._element 
    
    # public Partition methods
    def make_group(self, e):
        """Make a new group containing element e, and return its Position."""
        return self.Position(self, e)
    
    def find(self, p):
        """Finds the group containing p and return the position of its leader."""
        if p._parent != p:
            p._parent = self.find(p._parent)    # overwrite p._parent after recursion
        return p._parent 
    
    def union(self, p, q):
        """Merges the groups containing elements p and q (if distinct)."""
        a = self.find(p)
        b = self.find(q)
        if a is not b:
            if a._size > b._size:
                b._parent = a 
                a._size += b._size
            else:
                a._parent = b 
                b._size += a._size 



def MST_Kruskal(g: Graph) -> list:
    """
    Compute a minimum spanning tree of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.
    The elements of the graph's edges are assumed to be weights.
    """
    tree = []       # list of edges in spanning tree
    pq = HeapPriorityQueue()    # entries are edges in G, with weights as key
    forest = Partition()        # keep track fo forest clusters
    position = {}               # map each node to its Partition entry

    for v in g.vertices():
        position[v] = forest.make_group(v)
    
    for e in g.edges():
        pq.add(e.element(), e)  # edge's element is asssumed to be its weight
    
    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)
    return tree

