import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
class Node:
    def __init__(self, key, color="#CCCCCC"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / (2 ** layer), y - 1)
            add_edges(graph, node.left, pos, x=x - 1 / (2 ** layer), y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / (2 ** layer), y - 1)
            add_edges(graph, node.right, pos, x=x + 1 / (2 ** layer), y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, highlight_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    if highlight_nodes:
        for node_id, color in highlight_nodes.items():
            tree.nodes[node_id]['color'] = color

    colors = [tree.nodes[node]['color'] for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color='white')
    plt.show()

def generate_colors(n):
    colors = []
    for i in range(n):
        shade = hex(50 + int(205 * (i / max(1, n - 1))))[2:].zfill(2)
        color = f"#{shade}{96:02X}{240:02X}"
        colors.append(color)
    return colors

def dfs(root):
    stack = [root]
    visited = []
    colors = generate_colors(10)
    color_map = {}

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            color_map[node.id] = colors[len(visited) - 1]
            draw_tree(root, highlight_nodes=color_map)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def bfs(root):
    queue = deque([root])
    visited = []
    colors = generate_colors(10)
    color_map = {}

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            color_map[node.id] = colors[len(visited) - 1]
            draw_tree(root, highlight_nodes=color_map)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs(root)
bfs(root)
