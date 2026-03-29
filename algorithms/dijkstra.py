import time
import heapq


def dijkstra(graph, start):
    start_time = time.perf_counter()

    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    end_time = time.perf_counter()
    runtime = end_time - start_time

    return distances, runtime