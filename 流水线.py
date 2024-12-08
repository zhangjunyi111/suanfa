# 3 5
# 8 4 3 2 10

def main():
    # 先写好输入输出
    # m为流水线的数量
    # n为任务的数量
    m, n = map(int, input().strip().split())
    task_list = list(map(int, input().split()))

    # 对任务列表的时间进行排序
    task_list.sort()

    # m条流水线，取m个任务

    # 初始化消耗的时间为0
    cost_time = 0

    # 正在执行的任务列表的大小最大为3，初始化的时候为空
    current_execute_task_list = []
    while task_list:
        # 从任务列表中去取任务，当当前任务的任务列表中的任务数量小于3时，就从task_list中取任务，放到当前任务列表中
        while len(current_execute_task_list) != m:
            if not task_list:
                break
            task = task_list.pop(0)
            current_execute_task_list.append(task)

        # 处理当前任务列表中的任务
        # 找出耗时最小的任务的耗时
        current_execute_task_list.sort()
        min_task_time = current_execute_task_list[0]

        # 更新消耗的时间
        cost_time += min_task_time

        # 更新任务列表的时间，经过一轮执行，耗时最小的任务执行完毕，其他任务的时间也更新掉
        current_execute_task_list = [x - min_task_time for x in
                                     current_execute_task_list]

        # 移除已经执行完成的任务
        current_execute_task_list = [x for x in current_execute_task_list if
                                     x != 0]

    # 当while循环执行完毕后，意味着task_list为空，处理current_execute_task_list中的任务

    cost_time += max(current_execute_task_list)

    print(cost_time)

main()