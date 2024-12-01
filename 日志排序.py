def main():
    # 初始化日志存放列表
    logs = []
    # 处理后的日志列表
    logs_has_processed = []
    # 接收日志
    m = int(input().strip())
    for i in range(m):
        logs.append(input().strip())
    # 按照H:M:S分割
    for i in range(len(logs)):
        tmp = logs[i].split(":")
        tmp = tmp[:2] + tmp[2].split('.')
        tmp_new = []
        for element in tmp:
            element = element.strip('0')
            tmp_new.append(element)
        logs_has_processed.append((tmp_new, i))
        logs_has_processed.sort(key=lambda x: (int(x[0][0]), int(x[0][1]),
                                               int(x[0][2]), int(x[0][3]) if
                                               x[0][3] else 0))
    print_sequence = [i[1] for i in logs_has_processed]
    # 输出
    # 输出的时候按照print_sequence顺序输出
    for index in print_sequence:
        print(logs[index])


main()
