import networkx as nx
import matplotlib.pyplot as plt


def visualize_mst(graph, mst_edges):

    pos = nx.spring_layout(graph)

    # draw full graph
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="lightblue",
        edge_color="gray"
    )

    # highlight mst edges
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=mst_edges,
        edge_color="red",
        width=3
    )

    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title("Minimum Spanning Tree")
    plt.show()