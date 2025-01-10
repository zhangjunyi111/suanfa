import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.height = None
        self.left = None
        self.right = None


def build_Huffman_Tree(values):
    node_list = [Node(value) for value in values]
    while len(node_list) > 1:
        heapq.heapify(node_list)
        left = heapq.heappop(node_list)
        right = heapq.heappop(node_list)
        parent = Node(left.value + right.value)
        parent.left = left
        parent.right = right
        parent.height = max(left.height, right.height)
        heapq.heappush(parent)
