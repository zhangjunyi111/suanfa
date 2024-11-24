import sys

# 窗口数量
N = int(input())
# 行数
rows = int(input())
# 队列数组
queuelist = []
queuelist.append(list(map(int,input().split())))

# 定义一个结果矩阵，用来存放输出结果
matrix = [0] * (N * rows)
matrix_index = 0
# 将队列添加进入到列表里面

# 将对列中的数据分配给每个窗口
while matrix_index < len(matrix):
    queue_index = 0
    didRemovequeue = False
    # 如果queuelist为空
    if not queuelist:
        pass
    # 如果queuelist[queue_index]为空，则把queuelist[queue_index]对列删除掉

    if not queuelist[queue_index]:
        queuelist.pop(queue_index)
        # 如果这里删除的是最后一个队列
        if not queuelist:
            break
        didRemovequeue = True
        queue_index %= len(queuelist)

    if not didRemovequeue and queuelist:
        queue_index += 1






# 按顺序分配