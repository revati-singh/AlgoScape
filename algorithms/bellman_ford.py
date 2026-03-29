import time

def bellman_ford(graph, start):

    start_time = time.perf_counter()

    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0

    nodes = list(graph.nodes())

    for _ in range(len(nodes) - 1):
        for u, v, data in graph.edges(data=True):

            weight = data['weight']

            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

            if distances[v] + weight < distances[u]:
                distances[u] = distances[v] + weight

    end_time = time.perf_counter()

    runtime = end_time - start_time

    return distances, runtime