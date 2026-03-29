import time


def dfs(graph, start):
    visited = set()
    stack = [start]

    visited_order = []

    start_time = time.perf_counter()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            visited_order.append(node)

            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)

    end_time = time.perf_counter()

    runtime = end_time - start_time

    return visited_order, runtime