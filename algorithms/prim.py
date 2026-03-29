import heapq
import time


def prim(graph, start=0):

    start_time = time.perf_counter()

    visited = set([start])
    edges = []
    mst = []

    for neighbor in graph.neighbors(start):
        weight = graph[start][neighbor]['weight']
        heapq.heappush(edges, (weight, start, neighbor))

    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)
            mst.append((u, v, weight))

            for neighbor in graph.neighbors(v):
                if neighbor not in visited:
                    w = graph[v][neighbor]['weight']
                    heapq.heappush(edges, (w, v, neighbor))

    end_time = time.perf_counter()

    return mst, end_time - start_time