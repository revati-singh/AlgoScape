from performance.benchmark import run_benchmark
from visualization.plot_results import plot_results
from visualization.animate_traversal import animate_bfs, animate_dfs
from visualization.animate_traversal import visualize_mst
from visualization.animate_traversal import visualize_shortest_path
from graph_generator.generate_graph import generate_random_graph
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.kruskal import kruskal
from algorithms.prim import prim


node_sizes = [200, 800, 1500]

results = run_benchmark(node_sizes)

for r in results:
    print("\nGraph Size:", r["nodes"])
    print("BFS Time:", f"{r['bfs_time']:.8f}")
    print("DFS Time:", f"{r['dfs_time']:.8f}")
    print("Dijkstra Time:", f"{r['dijkstra_time']:.8f}")
    print("Bellman-Ford Time:", f"{r['bellman_time']:.8f}")
    print("Kruskal Time:", f"{r['kruskal_time']:.8f}")

plot_results(results)

print("\nChoose algorithm to visualize:")
print("1. BFS")
print("2. DFS")
print("3. Dijkstra")
print("4. Bellman-Ford")
print("5. Kruskal")
print("6. Prim")


choice = input("Enter choice: ")

graph = generate_random_graph(10, 20)

if choice == "1":
    animate_bfs(graph, 0)

elif choice == "2":
    animate_dfs(graph, 0)

elif choice == "3":
    distances, previous = dijkstra(graph, 0)

    target = max(graph.nodes())

    path = []
    node = target

    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()

    visualize_shortest_path(graph, path)

elif choice == "4":
    distances, previous = bellman_ford(graph, 0)

    target = max(graph.nodes())

    path = []
    node = target

    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()

    visualize_shortest_path(graph, path)

elif choice == "5":
    mst, _ = kruskal(graph)
    visualize_mst(graph, mst)

elif choice == "6":
    mst, _ = prim(graph, 0)
    visualize_mst(graph, mst)


else:
    print("Invalid choice")