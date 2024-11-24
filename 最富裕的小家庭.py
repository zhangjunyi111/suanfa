# -*- coding:utf-8 -*-
import sys

# 接收成员数量

# 接收每个成员的财富值


# 接收父子关系
#  1 2
#  1 3
#  2 4

# 关键是要梳理出每棵树

# 建立一个字典, 如何表示树的父节点，如何表示树的子节点
import sys
number = int(input())
money =  list(map(int,input().split()))
tree_dict = {}

while True:
    try:
        relation = list(map(int, input().split()))
        parent = relation[0]
        child = relation[1]
        if parent in tree_dict:
            tree_dict[parent].append(child)
        else:
            tree_dict[parent] =[parent,child]
    except:
        break

res = [x for x in tree_dict.values()]
res_money = []
for  member in res:
    res_money.append([money[x-1] for x in member])

sum_every_tree = [sum(x) for x in res_money]

print(sum_every_tree)

print(max(sum_every_tree))