import networkx as nx
import random


def generate_random_graph(nodes, edges):
    """
    Generate a random weighted graph
    """

    G = nx.Graph()

    # Add nodes
    for i in range(nodes):
        G.add_node(i)

    # Add random edges
    for _ in range(edges):
        u = random.randint(0, nodes - 1)
        v = random.randint(0, nodes - 1)

        if u != v and not G.has_edge(u, v):
            weight = random.randint(1, 10)
            G.add_edge(u, v, weight=weight)

    return G


if __name__ == "__main__":

    graph = generate_random_graph(10, 15)
   

    print("Nodes:", graph.nodes())
    print("Edges:", graph.edges(data=True))