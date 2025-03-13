# 树状结构查询

# 5
# b a
# c a
# d c
# e c
# f d
# c
import sys


def main():
    # 接收父子关系的行数
    relation_N = int(input())



    # 将树的关系存储到字典中，初始化一个存储树的字典

    tree_dict = dict()

    # 循环接收行数，存入字典树中

    for _ in range(relation_N):
        child_node, parent_node = input().split()
        if parent_node not in tree_dict:
            tree_dict[parent_node] = set()
        tree_dict[parent_node].add(child_node)

    # 接收要查询的node
    query_node = input()
    # 记得删除打印语句
    # print(tree_dict)

    # 初始化结果列表，存储结果集合
    result = []

    if query_node not in tree_dict:
        print('查询的节点不在树中')
        sys.exit()

    # 初始化队列
    queue = list(tree_dict[query_node])
    while queue:
        child_node = queue.pop(0)
        result.append(child_node)
        if child_node in tree_dict:
            queue.extend(list(tree_dict[child_node]))

    for node in sorted(result):
        print(node)


main()