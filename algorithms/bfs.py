import time
from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited_order = []

    start_time = time.perf_counter()

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            visited_order.append(node)

            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)

    end_time = time.perf_counter()

    runtime = end_time - start_time

    return visited_order, runtime