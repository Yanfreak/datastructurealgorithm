# R-14.7
# directed 
# self.graph[u-1][v-1] = x
# undirected: + self.graph[v-1][u-1] = x



# R-14.11
# a. adjacency list;    b. adjacency matrix;    c. adjacency matrix


# R-14.12
class GraphMatrix:

    adj = []

    def __init__(self, v):
        self.v = v
        self.adj = [ [0] * v for i in range(v) ]
    
    def insert_edge(self, u, v):
        self.adj[u-1][v-1] = 1
        self.adj[v-1][u-1] = 1
    
    def DFS(self, u, discovered: dict):
        discovered[u] = True 
        for i in range(self.v):
            if (self.adj[u][i] == 1 and (not discovered[i])):
                self.DFS(i, discovered)
# for loop -- n, n vertices -> v * for loops. Thus, O(n^2)


# R-14.14
# basically, a line

# R-14.15
# a star


# R-14.16
# b. [1, 2, 3, 4, 6, 5, 7, 8]; c. [1, 2, 3, 4, 6, 5, 7, 8]

# R-14.19
# n(n-1)/2

# R-14.27
# 1-8, 8-2-6-7, 8-5, 5-3, 5-4
# 
# 
# C-14.56
# def weighted_transitive_closure
# then def compute_eccentricity
# max(eccentricity(v))
# 
# 
# C-14.57
# def compact
# 
# 
# C-14.58
# check shortest_paths_floyd_warshall  