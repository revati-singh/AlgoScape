import matplotlib.pyplot as plt
import networkx as nx
import time

def animate_bfs(graph, start):

    visited = set()
    queue = [start]

    pos = nx.spring_layout(graph)

    while queue:

        node = queue.pop(0)
        visited.add(node)

        plt.clf()

        color_map = []
        for n in graph.nodes():
            if n in visited:
                color_map.append("green")
            else:
                color_map.append("lightblue")

        nx.draw(graph, pos, node_color=color_map, with_labels=True)

        plt.title("BFS Traversal Animation")

        plt.pause(0.8)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                queue.append(neighbor)

    plt.show()
def animate_dfs(graph, start):

    visited = set()
    stack = [start]

    pos = nx.spring_layout(graph)

    while stack:

        node = stack.pop()

        if node not in visited:
            visited.add(node)

        plt.clf()

        color_map = []
        for n in graph.nodes():
            if n in visited:
                color_map.append("orange")
            else:
                color_map.append("lightblue")

        nx.draw(graph, pos, node_color=color_map, with_labels=True)

        plt.title("DFS Traversal Animation")

        plt.pause(0.8)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                stack.append(neighbor)

    plt.show() 

def visualize_mst(graph, mst_edges):

    pos = nx.spring_layout(graph)

    plt.figure()

    # draw original graph
    nx.draw(graph, pos, with_labels=True, node_color="lightblue")

    # edges in MST
    mst_edge_list = [(u, v) for u, v, w in mst_edges]

    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=mst_edge_list,
        edge_color="red",
        width=3
    )

    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title("Minimum Spanning Tree")
    plt.show()   

def visualize_shortest_path(graph, path):

    import matplotlib.pyplot as plt
    import networkx as nx

    pos = nx.spring_layout(graph)

    plt.figure()

    # draw full graph
    nx.draw(graph, pos, with_labels=True, node_color="lightblue")

    # convert path nodes → edges
    path_edges = list(zip(path, path[1:]))

    # highlight path
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=path_edges,
        edge_color="red",
        width=3
    )

    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title("Shortest Path Visualization")
    plt.show()