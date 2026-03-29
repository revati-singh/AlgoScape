import time

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, rank, u, v):

    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


def kruskal(graph):

    start_time = time.perf_counter()

    edges = list(graph.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])

    parent = {}
    rank = {}

    for node in graph.nodes():
        parent[node] = node
        rank[node] = 0

    mst = []

    for u, v, data in edges:

        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, data['weight']))

    end_time = time.perf_counter()

    runtime = end_time - start_time

    return mst, runtime