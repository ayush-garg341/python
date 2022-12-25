"""
Iterative implementation of BFS using queue.
"""

from collections import deque


class Graph:
    def __init__(self, edges: list, n: int):

        # Adjacency list representation of graph
        self.adj_list = [[] for _ in range(n)]

        # store the level number as well
        self.level_num = [1 for _ in range(n)]

        # Undirected graph
        for (src, dest) in edges:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)


def BFS_iterative(G: Graph, i: int, discovered: list):

    # create a queue for enqueuing
    q = deque()

    # mark the current vertex as discovered
    discovered[i] = True

    # enqueu the current vertex
    q.append(i)

    while q:
        # dequeue front node and print it
        v = q.popleft()
        print(v, end=" ")

        for adj in G.adj_list[v]:
            if not discovered[adj]:
                # we can check/store the level number of nodes
                discovered[adj] = True
                G.level_num[adj] = G.level_num[v] + 1
                q.append(adj)


if __name__ == "__main__":

    # List of graph edges as per the above diagram
    edges = [
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (5, 9),
        (5, 10),
        (4, 7),
        (4, 8),
        (7, 11),
        (7, 12),
    ]

    # 0, 13, 14 are isolated vertices

    # total number of nodes in the graph (labelled from 0 to 14)
    n = 15

    # build a graph from the given edges
    graph = Graph(edges, n)

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n

    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            # we can check here connected components
            # start BFS traversal from vertex i
            BFS_iterative(graph, i, discovered)

    print("\n")
    for i in range(n):
        print("level num of vertex {} is {}".format(i, graph.level_num[i]))
