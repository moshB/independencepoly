# # # import networkx as nx
# # # import matplotlib.pyplot as plt
# # #
# # # # Create a new graph
# # # G = nx.Graph()
# # #
# # # # Add the nodes and edges for K_97 (complete graph with 97 vertices)
# # # G_K97 = nx.complete_graph(97)
# # # G.add_edges_from(G_K97.edges())
# # #
# # # # Add four disjoint K_3 graphs to G
# # # for i in range(97, 97 + 4 * 3, 3):
# # #     G_K3 = nx.complete_graph([i, i+1, i+2])  # Create a K_3 with vertices i, i+1, i+2
# # #     G.add_edges_from(G_K3.edges())
# # #
# # # # Draw the graph
# # # plt.figure(figsize=(10, 10))
# # # pos = nx.spring_layout(G)  # Layout for visualizing
# # # nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=8, font_color='black', font_weight='bold')
# # #
# # # # Show the graph
# # # plt.show()
# # # import networkx as nx
# # # import matplotlib.pyplot as plt
# # #
# # # def fibonacci_tree(G, node, n, parent=None):
# # #     if n == 1:
# # #         return node
# # #     elif n == 2:
# # #         G.add_edge(parent, node)
# # #         return node
# # #     else:
# # #         left_child = node + 1
# # #         right_child = fibonacci_tree(G, left_child, n - 1, node)
# # #         fibonacci_tree(G, right_child + 1, n - 2, node)
# # #         if parent is not None:
# # #             G.add_edge(parent, node)
# # #         return right_child + 1
# # #
# # # # Create a graph
# # # G = nx.Graph()
# # #
# # # # Start the tree
# # # root = 0
# # # fibonacci_tree(G, root, 6)  # You can adjust the depth of the Fibonacci tree here
# # #
# # # # Draw the graph
# # # pos = nx.spring_layout(G)
# # # nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_color='black')
# # # plt.show()
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# # # Recursive function to generate a Fibonacci tree
# # def fibonacci_tree(G, node, n, pos=None, x=0, y=0, layer=1):
# #     if pos is None:
# #         pos = {}
# #     pos[node] = (x, y)
# #     if n == 1:
# #         return node, pos
# #     elif n == 2:
# #         G.add_edge(node, node + 1)
# #         pos[node + 1] = (x, y - layer)
# #         return node + 1, pos
# #     else:
# #         # Create the left subtree T(n-1)
# #         left_child, pos = fibonacci_tree(G, node + 1, n - 1, pos, x - layer, y - layer, layer / 2)
# #         # Create the right subtree T(n-2)
# #         right_child, pos = fibonacci_tree(G, left_child + 1, n - 2, pos, x + layer, y - layer, layer / 2)
# #         G.add_edge(node, node + 1)
# #         return right_child, pos
# #
# # # Initialize the graph and root node
# # G = nx.Graph()
# # root = 0
# # depth = 6  # Adjust the depth of the Fibonacci tree
# #
# # # Generate the Fibonacci tree
# # _, pos = fibonacci_tree(G, root, depth)
# #
# # # Draw the tree
# # plt.figure(figsize=(10, 8))
# # nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_color='black')
# # plt.show()
#
import networkx as nx
import matplotlib.pyplot as plt
#
# # Recursive function to generate a Fibonacci tree
def fibonacci_tree(G, node, n, parent=None, pos=None, x=0, y=0, layer=1):
    if pos is None:
        pos = {}
    pos[node] = (x, y)
    if parent is not None:
        G.add_edge(parent, node)

    if n == 1:
        return node, pos
    elif n == 2:
        G.add_edge(node, node + 1)
        pos[node + 1] = (x, y - layer)
        return node + 1, pos
    else:
        # Create the left subtree T(n-1)
        left_child, pos = fibonacci_tree(G, node + 1, n - 1, node, pos, x - layer, y - layer, layer / 2)
        # Create the right subtree T(n-2)
        right_child, pos = fibonacci_tree(G, left_child + 1, n - 2, node, pos, x + layer, y - layer, layer / 2)
        return right_child, pos

# Initialize the graph and root node
G = nx.Graph()
root = 0
depth = 5 # Adjust the depth of the Fibonacci tree

# Generate the Fibonacci tree
_, pos = fibonacci_tree(G, root, depth)
print(G)
# Draw the tree
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_color='black')
plt.show()

import networkx as nx
from matplotlib import pyplot as plt


# Recursive function to generate a Fibonacci tree
def fibonacci_tree(G, node, n, parent=None, pos=None, x=0, y=0, layer=1):
    if pos is None:
        pos = {}
    pos[node] = (x, y)
    if parent is not None:
        G.add_edge(parent, node)

    if n == 1:
        return node, pos
    elif n == 2:
        G.add_edge(node, node + 1)
        pos[node + 1] = (x, y - layer)
        return node + 1, pos
    else:
        # Create the left subtree T(n-1)
        left_child, pos = fibonacci_tree(G, node + 1, n - 1, node, pos, x - layer, y - layer, layer / 2)
        # Create the right subtree T(n-2)
        right_child, pos = fibonacci_tree(G, left_child + 1, n - 2, node, pos, x + layer, y - layer, layer / 2)
        return right_child, pos

# Function to convert a graph to an adjacency list
def graph_to_adjacency_list(G):
    adj_list = {node: list(neighbors) for node, neighbors in G.adjacency()}
    return adj_list

# Initialize the graph and root node
G = nx.Graph()
root = 0
depth = 5  # Adjust the depth of the Fibonacci tree

# Generate the Fibonacci tree
_, pos = fibonacci_tree(G, root, depth)

# Get the adjacency list
adj_list = graph_to_adjacency_list(G)
print(adj_list)
ggg={}
for node, neighbors in adj_list.items():
    ggg[node]=neighbors
print(ggg)
# plt.figure(figsizesize=(10, 8))
# nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_color='black')
# plt.show()
