def main():
    # 接收用户输入
    numbers = list(map(int, input().split()))
    length = len(numbers)
    # 初始化一个结果数组，存储成功到达最后一个元素所需要的步骤数
    result = []
    # 因为第二个元素只能是由第一个元素，经过length //2的范围进行跳转

    for i in range(1, length // 2):
        index = i
        step = 1
        while index < length:
            if index == length - 1:
                result.append(step)
                break
            index += numbers[index]
            step += 1

    if result:
        result.sort()
        print(result[0])
    else:
        print(-1)


main()