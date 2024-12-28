# 银行插队
# start time:17:25


def main():
    # 构建一个优先级字典,字典的键就是该客户的优先级，字典的值就是该优先级下的客户ID
    customer_priority = dict()

    # 获取事件数量n
    n = int(input())
    for i in range(1, n):
        customer_priority[i] = []
    # 事件分为2种类型，一种是添加到客户优先级字典，一种是获取当前优先级最高的客户ID,通过第一个标志位区分操作类型
    # 通过第二个标志位获取客户编号，通过第三个标志位确定优先级

    for _ in range(n):
        info = input().split()
        option_type = info[0]
        if option_type == 'a':
            customer_num = info[1]
            priority = int(info[2])
            customer_priority[priority].append(customer_num)

        elif option_type == 'p':
            for i in range(1, len(customer_priority.keys())):
                if customer_priority[i]:
                    print(customer_priority[i].pop())
                break


if __name__ == '__main__':
    main()
