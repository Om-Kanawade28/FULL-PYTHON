# Graph:

# A graph is a non-linear data structure that consists of a set of vertices (nodes) connected by edges. It's a versatile data structure used to represent relationships and connections between objects.

# Key Concepts:

# - **Vertex (Node):** A basic building block of a graph, representing an object or entity.
# - **Edge:** A connection between two vertices, representing a relationship or link between them.
# - **Directed Graph:** Edges have a direction, indicating a one-way relationship between vertices.
# - **Undirected Graph:** Edges have no direction, indicating a two-way relationship between vertices.
# - **Weighted Graph:** Edges have associated weights, representing the cost or distance of the connection.
# - **Adjacency List:** A representation of a graph where each vertex has a list of its adjacent vertices.
# - **Adjacency Matrix:** A representation of a graph where each cell in a matrix indicates the presence or absence of an edge between two vertices.

# Types of Graphs:

# - **Simple Graph:** A graph with no loops (edges connecting a vertex to itself) or multiple edges between the same pair of vertices.
# - **Multigraph:** A graph that allows multiple edges between the same pair of vertices.
# - **Complete Graph:** A graph where every vertex is connected to every other vertex.
# - **Tree:** A connected graph with no cycles.
# - **Cycle:** A path in a graph that starts and ends at the same vertex.

# Advantages of Graphs:

# - **Representing Relationships:** Graphs are ideal for representing relationships between objects, such as social networks, transportation systems, and computer networks.
# - **Modeling Complex Systems:** Graphs can model complex systems, such as electrical circuits, chemical reactions, and biological networks.
# - **Solving Optimization Problems:** Graphs are used in solving optimization problems, such as finding the shortest path between two points or the minimum spanning tree of a network.

# Disadvantages of Graphs:

# - **Complexity:** Implementing and manipulating graphs can be complex, especially for large graphs.
# - **Memory Usage:** Graphs can require significant memory, especially for dense graphs with many edges.

# Implementation:

# Here's a simple Python implementation of a graph using an adjacency list:

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)  # For undirected graphs

    def print_graph(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")

# Usage:

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')

graph.print_graph()

# Output:
# A: ['B', 'C']
# B: ['A', 'C']
# C: ['A', 'B']

# Applications:

# - **Social Networks:**  Representing connections between users.
# - **Transportation Networks:**  Modeling roads, railways, and air routes.
# - **Computer Networks:**  Representing connections between devices.
# - **Web Graphs:**  Representing websites and hyperlinks.
# - **Recommendation Systems:**  Used in recommending products or content based on user preferences.
# - **Route Planning:**  Finding the shortest path between two locations.
# - **Network Flow:**  Optimizing the flow of resources through a network.

# Advanced Concepts:

# - **Graph Traversal:**  Visiting all vertices in a graph in a specific order (e.g., depth-first search, breadth-first search).
# - **Shortest Path Algorithms:**  Finding the shortest path between two vertices (e.g., Dijkstra's algorithm, Bellman-Ford algorithm).
# - **Minimum Spanning Tree Algorithms:**  Finding a tree that connects all vertices with the minimum total edge weight (e.g., Kruskal's algorithm, Prim's algorithm).
# - **Graph Coloring:**  Assigning colors to vertices so that no adjacent vertices have the same color.

# Graphs are a powerful data structure with numerous applications in computer science. Understanding their concepts and implementation is essential for solving problems related to relationships, networks