#  -*-  coding: utf-8  -*-
from collections import deque


# 广度优先遍历队列中的内容
def bfs(launches_start_time, dq):
    # 创建一个visited数组，表示被访问过了没有
    visited = [False] * launches_total_number
    while dq:
        start_time, launche_num = dq.popleft()
        if not visited[launche_num]:
            visited[launche_num] = True
            neighbers = [(launche_num - 1) % launches_total_number, (launche_num
                                                                     + 1) % launches_total_number]

        # 更新启动时间
            for neighber in neighbers:
                if not visited[neighber]:
                    if launches_start_time[neighber] > start_time + 1:
                        launches_start_time[neighber] = start_time + 1
                    dq.append((start_time + 1, neighber))

        else:
            continue

    # 遍历启动时刻表，找到最大的启动时间，输出该时间的列表

    max_start_time = 0
    res = []
    for i in range(len(launches_start_time)):
        if launches_start_time[i] > max_start_time:
            max_start_time = launches_start_time[i]
            res = [i]
        elif launches_start_time[i] == max_start_time:
            res.append(i)
    print(len(res))
    print( ' '.join(list(map(str, res))))


if __name__ == '__main__':
    # 接收引擎总数和 需要手动启动的引擎数量

    launches_total_number, need_start_by_hand_number = list(map(int,
                                                                input().split()))

    # 定义一个引擎启动的时间列表，表示引擎在什么时候启动
    # 初始化该引擎的列表
    launches_start_time = [float('inf')] * launches_total_number

    # 循环接收需要手动启动的引擎和启动的时刻
    dq = deque()

    for i in range(need_start_by_hand_number):
        start_time, launche_num = list(map(int, input().split()))
        launches_start_time[launche_num] = start_time
        dq.append((start_time, launche_num))
    bfs(launches_start_time, dq)
