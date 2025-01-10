import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.height = 0
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.value == other.value:
            return self.height < other.height
        return self.value < other.value


def build_Huffman_Tree(values):
    node_list = [Node(value) for value in values]
    while len(node_list) > 1:
        heapq.heapify(node_list)
        left = heapq.heappop(node_list)
        right = heapq.heappop(node_list)
        parent = Node(left.value + right.value)
        parent.left = left
        parent.right = right
        parent.height = max(left.height, right.height) + 1
        heapq.heappush(node_list, parent)
    return node_list[0]


# 中序遍历哈夫曼树
result = []


def inorder_traversal(root):
    global result
    if not root:
        return
    # 中序遍历的顺序是左子树，根节点，右子树
    inorder_traversal(root.left)
    result.append(root.value)
    inorder_traversal(root.right)


if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split()))
    root = build_Huffman_Tree(values)
    inorder_traversal(root)
    # print(result)
    print(' '.join(list(map(str, result))))
