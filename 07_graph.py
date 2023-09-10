
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbors(self, value):
        self.neighbors.append(value)


class Graph:
    def __init__(self):
        self.nodes_dict = {}

    # Adding a new entry to the dictionary
    def add_node(self, value):
        self.nodes_dict[value] = Node(value)

    # Adding a node:int to the array that is inside the instance Node()
    def add_edge(self, val1, val2):
        self.nodes_dict[val1].add_neighbors(val2)
        self.nodes_dict[val2].add_neighbors(val1)

    def add_all_edges(self, arr_graph):
        for i in range(len(arr_graph)):
            for j in range(i + 1, len(arr_graph)):
                self.add_edge(arr_graph[i], arr_graph[j])


graph = Graph()
arr = [5, 8, 9, 2, 17]

for n in arr:
    graph.add_node(n)

graph.add_edge(8, 5)
graph.add_edge(8, 2)
graph.add_edge(8, 9)
graph.add_edge(9, 2)
graph.add_edge(9, 17)
graph.add_edge(2, 17)

for node in graph.nodes_dict:
    # Dictionary access to the value by key
    val_neighbors = graph.nodes_dict[node]
    print(val_neighbors.value, val_neighbors.neighbors)

print()

graph2 = Graph()

for n in arr:
    graph2.add_node(n)

graph2.add_all_edges(arr)

for node in graph2.nodes_dict:
    # Dictionary access to the value by key
    val_neighbors = graph2.nodes_dict[node]
    print(val_neighbors.value, val_neighbors.neighbors)
