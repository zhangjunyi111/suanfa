# 698 ->986
def main():
    priority_list =input().split(',')
    # 初始化一个打印数组
    print_sequence = []
    # 构建一个task_list
    task_list = [(i, int(priority_list[i])) for i in range(len(priority_list))]

    # 对task_list 进行排序
    task_list.sort(key=lambda x: -x[1])
    current_task = 0
    while current_task < len(task_list):
        for i in range(len(task_list)):
            if task_list[i][0] == current_task:
                print_sequence.append(i)
                break
        current_task +=1

    print(' '.join(list(map(str,print_sequence))))


main()