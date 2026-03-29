import customtkinter as ctk
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

# -------------------------------
# GRAPH DRAW MODE VARIABLES
# -------------------------------

draw_graph = nx.Graph()
positions = {}
node_counter = 0
selected_node = None


# -------------------------------
# ALGORITHM INFO
# -------------------------------

algorithm_info = {

"BFS":"""
Breadth First Search
Time Complexity: O(V + E)
Traversal algorithm exploring level by level.
""",

"DFS":"""
Depth First Search
Time Complexity: O(V + E)
Explores graph deeply before backtracking.
""",

"Dijkstra":"""
Dijkstra Algorithm
Time Complexity: O(E log V)
Finds shortest path in weighted graphs.
""",

"Bellman-Ford":"""
Bellman-Ford Algorithm
Time Complexity: O(VE)
Works even with negative weights.
""",

"Prim":"""
Prim's Algorithm
Time Complexity: O(E log V)
Constructs Minimum Spanning Tree.
""",

"Kruskal":"""
Kruskal's Algorithm
Time Complexity: O(E log E)
Sorts edges to build Minimum Spanning Tree.
"""
}


# -------------------------------
# GRAPH GENERATOR
# -------------------------------

def generate_graph():

    nodes = int(nodes_entry.get())
    density = density_slider.get()

    max_edges = nodes*(nodes-1)//2
    edges = int(max_edges*density)

    G = nx.gnm_random_graph(nodes, edges)

    for (u,v) in G.edges():
        G[u][v]['weight'] = random.randint(1,10)

    stats_label.configure(
        text=f"Graph Stats → Nodes:{nodes} | Edges:{edges}"
    )

    return G


# -------------------------------
# BFS VISUALIZATION
# -------------------------------

def animate_bfs(G,start):

    visited=set()
    queue=[start]
    pos=nx.spring_layout(G)

    while queue:

        node=queue.pop(0)

        if node not in visited:

            visited.add(node)

            plt.clf()

            nx.draw(
                G,pos,
                with_labels=True,
                node_color=[
                    "orange" if n==node else "skyblue"
                    for n in G.nodes()
                ]
            )

            labels=nx.get_edge_attributes(G,'weight')
            nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

            plt.pause(0.8)

            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)

    plt.show()


# -------------------------------
# DFS VISUALIZATION
# -------------------------------

def animate_dfs(G,start):

    visited=set()
    stack=[start]
    pos=nx.spring_layout(G)

    while stack:

        node=stack.pop()

        if node not in visited:

            visited.add(node)

            plt.clf()

            nx.draw(
                G,pos,
                with_labels=True,
                node_color=[
                    "orange" if n==node else "skyblue"
                    for n in G.nodes()
                ]
            )

            labels=nx.get_edge_attributes(G,'weight')
            nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

            plt.pause(0.8)

            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)

    plt.show()


# -------------------------------
# DIJKSTRA
# -------------------------------

def dijkstra(G,start):

    dist={node:float('inf') for node in G.nodes()}
    prev={node:None for node in G.nodes()}

    dist[start]=0
    Q=list(G.nodes())

    while Q:

        u=min(Q,key=lambda node:dist[node])
        Q.remove(u)

        for v in G.neighbors(u):

            alt=dist[u]+G[u][v]['weight']

            if alt<dist[v]:
                dist[v]=alt
                prev[v]=u

    end=list(G.nodes())[-1]

    path=[]
    while end is not None:
        path.insert(0,end)
        end=prev[end]

    return path


# -------------------------------
# BELLMAN FORD
# -------------------------------

def bellman_ford(G,start):

    dist={node:float('inf') for node in G.nodes()}
    prev={node:None for node in G.nodes()}

    dist[start]=0

    for _ in range(len(G.nodes())-1):

        for u,v,data in G.edges(data=True):

            w=data['weight']

            if dist[u]+w<dist[v]:

                dist[v]=dist[u]+w
                prev[v]=u

    end=list(G.nodes())[-1]

    path=[]
    while end is not None:
        path.insert(0,end)
        end=prev[end]

    return path


# -------------------------------
# MST VISUALIZATION
# -------------------------------

def visualize_mst(G,edges):

    pos=nx.spring_layout(G)

    nx.draw(G,pos,with_labels=True,node_color="skyblue")

    nx.draw_networkx_edges(
        G,pos,
        edgelist=[(u,v) for u,v,w in edges],
        width=3,
        edge_color="red"
    )

    labels=nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    plt.show()


def visualize_path(G,path):

    pos=nx.spring_layout(G)

    edges=list(zip(path,path[1:]))

    nx.draw(G,pos,with_labels=True,node_color="skyblue")

    nx.draw_networkx_edges(
        G,pos,
        edgelist=edges,
        width=3,
        edge_color="green"
    )

    labels=nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    plt.show()


# -------------------------------
# MST ALGORITHMS
# -------------------------------

def prim(G):

    mst=nx.minimum_spanning_tree(G,algorithm="prim")

    edges=[]

    for u,v,data in mst.edges(data=True):
        edges.append((u,v,data['weight']))

    return edges


def kruskal(G):

    mst=nx.minimum_spanning_tree(G,algorithm="kruskal")

    edges=[]

    for u,v,data in mst.edges(data=True):
        edges.append((u,v,data['weight']))

    return edges


# -------------------------------
# BENCHMARK
# -------------------------------

def benchmark():

    G=generate_graph()

    algos={
    "Dijkstra":lambda:dijkstra(G,0),
    "Bellman-Ford":lambda:bellman_ford(G,0),
    "Prim":lambda:prim(G),
    "Kruskal":lambda:kruskal(G)
    }

    times=[]

    for name,algo in algos.items():

        start=time.time()
        algo()
        end=time.time()

        times.append(end-start)

    plt.bar(algos.keys(),times)
    plt.title("Algorithm Runtime Comparison")
    plt.ylabel("Time (seconds)")
    plt.show()


# -------------------------------
# DRAW GRAPH MODE
# -------------------------------

def draw_graph_mode():

    global draw_graph,positions,node_counter,selected_node

    draw_graph=nx.Graph()
    positions={}
    node_counter=0
    selected_node=None

    fig,ax=plt.subplots()

    def on_click(event):

        global node_counter,selected_node

        if event.xdata is None or event.ydata is None:
            return

        x=event.xdata
        y=event.ydata

        for node,(nxp,nyp) in positions.items():

            if (x-nxp)**2+(y-nyp)**2<0.02:

                if selected_node is None:
                    selected_node=node
                else:

                    weight=random.randint(1,10)

                    draw_graph.add_edge(
                        selected_node,node,weight=weight
                    )

                    selected_node=None

                redraw()
                return

        draw_graph.add_node(node_counter)
        positions[node_counter]=(x,y)
        node_counter+=1

        redraw()

    def redraw():

        ax.clear()

        nx.draw(
            draw_graph,
            positions,
            with_labels=True,
            node_color="skyblue",
            ax=ax
        )

        labels=nx.get_edge_attributes(draw_graph,'weight')
        nx.draw_networkx_edge_labels(
            draw_graph,
            positions,
            edge_labels=labels,
            ax=ax
        )

        plt.draw()

    fig.canvas.mpl_connect(
        'button_press_event',
        on_click
    )

    plt.title("Click to add nodes. Click two nodes to connect.")
    plt.show()


# -------------------------------
# RUN SELECTED ALGORITHM
# -------------------------------

def run_algorithm():

    algo=algo_menu.get()

    G=generate_graph()

    start_time=time.time()

    if algo=="BFS":
        animate_bfs(G,0)

    elif algo=="DFS":
        animate_dfs(G,0)

    elif algo=="Dijkstra":
        visualize_path(G,dijkstra(G,0))

    elif algo=="Bellman-Ford":
        visualize_path(G,bellman_ford(G,0))

    elif algo=="Prim":
        visualize_mst(G,prim(G))

    elif algo=="Kruskal":
        visualize_mst(G,kruskal(G))

    end_time=time.time()

    runtime=round(end_time-start_time,5)

    stats_label.configure(
        text=f"Execution Time: {runtime} sec"
    )


# -------------------------------
# UPDATE INFO PANEL
# -------------------------------

def update_info(choice):

    info_box.delete("1.0","end")
    info_box.insert("end",algorithm_info[choice])


# -------------------------------
# GUI
# -------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("900x650")

app.title("AlgoScape — Graph Algorithm Visualizer")

title=ctk.CTkLabel(
app,
text="AlgoScape",
font=("Arial",40,"bold")
)

title.pack(pady=10)

subtitle=ctk.CTkLabel(
app,
text="Interactive Graph Algorithm Visualizer & Performance Analyzer",
font=("Arial",16)
)

subtitle.pack(pady=5)

frame=ctk.CTkFrame(app)
frame.pack(pady=20,padx=20,fill="both",expand=True)

info_label=ctk.CTkLabel(
frame,
text="Algorithm Information",
font=("Arial",18,"bold")
)

info_label.pack(pady=10)

info_box=ctk.CTkTextbox(
frame,
width=500,
height=200
)

info_box.pack(pady=10)

nodes_label=ctk.CTkLabel(frame,text="Number of Nodes")
nodes_label.pack(pady=5)

nodes_entry=ctk.CTkEntry(frame)
nodes_entry.insert(0,"10")
nodes_entry.pack(pady=5)

density_label=ctk.CTkLabel(frame,text="Graph Density")
density_label.pack(pady=10)

density_slider=ctk.CTkSlider(frame,from_=0.1,to=1.0)
density_slider.set(0.3)
density_slider.pack(pady=10)

algo_menu=ctk.CTkOptionMenu(
frame,
values=[
"BFS","DFS","Dijkstra",
"Bellman-Ford","Prim","Kruskal"
],
command=update_info
)

algo_menu.pack(pady=10)

run_button=ctk.CTkButton(
frame,
text="Run Visualization",
command=run_algorithm
)

run_button.pack(pady=10)

benchmark_button=ctk.CTkButton(
frame,
text="Compare Algorithm Performance",
command=benchmark
)

benchmark_button.pack(pady=10)

draw_button=ctk.CTkButton(
frame,
text="Draw Your Own Graph",
command=draw_graph_mode
)

draw_button.pack(pady=10)

stats_label=ctk.CTkLabel(
app,
text="Graph Stats → Nodes:- | Edges:-"
)

stats_label.pack(pady=10)

update_info("BFS")

app.mainloop()