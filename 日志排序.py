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
    for log in logs:
        tmp = log.split(":")
        tmp = tmp[:2] + tmp[2].split('.')
        tmp_new = []
        for element in tmp:
            element = element.strip('0')
            tmp_new.append(element)
        logs_has_processed.append(tmp_new)
        logs_has_processed.sort(key=lambda x: (x[0], x[1],
                                                              x[2], x[3]))
    print(logs_has_processed[-1])

    # 去掉前面的0

    # 比较时分秒

    # 输出


main()
