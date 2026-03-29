from graph_generator.generate_graph import generate_random_graph
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.kruskal import kruskal
from algorithms.prim import prim
def run_benchmark(node_sizes):

    results = []

    for size in node_sizes:

        graph = generate_random_graph(size, size * 4)

        bfs_total = 0
        dfs_total = 0
        dijkstra_total = 0
        bellman_total = 0
        kruskal_total = 0
        prim_total = 0

        runs = 3

        for _ in range(runs):
            _, bfs_time = bfs(graph, 0)
            _, dfs_time = dfs(graph, 0)
            _, dijkstra_time = dijkstra(graph, 0)
            _, bellman_time = bellman_ford(graph, 0)
            _, kruskal_time = kruskal(graph)
            _, prim_time = prim(graph, 0)


            prim_total += prim_time
            bellman_total += bellman_time
            kruskal_total += kruskal_time
            bfs_total += bfs_time
            dfs_total += dfs_time
            dijkstra_total += dijkstra_time

        results.append({
            "nodes": size,
            "bfs_time": bfs_total / runs,
            "dfs_time": dfs_total / runs,
            "dijkstra_time": dijkstra_total / runs,
            "bellman_time": bellman_total / runs,
            "kruskal_time": kruskal_total / runs,
            "prim_time": prim_total / runs
        })

    return results