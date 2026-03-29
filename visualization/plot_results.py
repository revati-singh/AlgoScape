import matplotlib.pyplot as plt

def plot_results(results):

    nodes = [r["nodes"] for r in results]

    bfs_times = [r["bfs_time"] for r in results]
    dfs_times = [r["dfs_time"] for r in results]
    dijkstra_times = [r["dijkstra_time"] for r in results]
    bellman_times = [r["bellman_time"] for r in results]
    kruskal_times = [r["kruskal_time"] for r in results]
    prim_times = [r["prim_time"] for r in results]

    plt.figure( figsize=(10, 6) )
    marker='o'

    plt.plot(nodes, bfs_times, marker='o', label="BFS")
    plt.plot(nodes, dfs_times, marker='o', label="DFS")
    plt.plot(nodes, dijkstra_times, marker='o', label="Dijkstra")
    plt.plot(nodes, bellman_times, marker='o', label="Bellman-Ford")
    plt.plot(nodes, kruskal_times, marker='o', label="Kruskal")
    plt.plot(nodes, prim_times, marker='o', label="Prim")

    plt.xlabel("Number of Nodes")
    plt.ylabel("Runtime (seconds)")
    plt.title("Graph Algorithm Performance Comparison")

    plt.legend()
    plt.savefig("algorithm_performance.png")
    plt.grid(True)

    plt.show()