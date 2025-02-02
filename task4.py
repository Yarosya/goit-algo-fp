import uuid
import networkx as nx
import matplotlib.pyplot as plt
import math


class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def create_heap_tree(heap_array):
    if not heap_array:
        return None
    nodes = [HeapNode(val) for val in heap_array]

    nodes[0].color = "lightcoral"

    return nodes


def add_heap_edges(graph, nodes, pos, index=0, x=0, y=0, layer=1):
    if index >= len(nodes):
        return graph

    current_node = nodes[index]
    graph.add_node(current_node.id, color=current_node.color, label=current_node.val)

    left_child_idx = 2 * index + 1
    right_child_idx = 2 * index + 2

    if left_child_idx < len(nodes):
        left_child = nodes[left_child_idx]
        graph.add_edge(current_node.id, left_child.id)
        l = x - 1 / 2 ** layer
        pos[left_child.id] = (l, y - 1)
        add_heap_edges(graph, nodes, pos, left_child_idx, l, y - 1, layer + 1)

    if right_child_idx < len(nodes):
        right_child = nodes[right_child_idx]
        graph.add_edge(current_node.id, right_child.id)
        r = x + 1 / 2 ** layer
        pos[right_child.id] = (r, y - 1)
        add_heap_edges(graph, nodes, pos, right_child_idx, r, y - 1, layer + 1)

    return graph


def draw_heap(heap_array):
    if not heap_array:
        print("Купа порожня")
        return

    nodes = create_heap_tree(heap_array)

    heap_graph = nx.DiGraph()
    pos = {nodes[0].id: (0, 0)}

    heap_graph = add_heap_edges(heap_graph, nodes, pos)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.title("Візуалізація бінарної купи")
    plt.show()



heap_example = [100, 84, 71, 60, 23, 12, 29]
draw_heap(heap_example)