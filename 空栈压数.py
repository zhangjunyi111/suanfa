# 用列表定义个空栈，栈顶就是列表的最后一个元素
stack = []

input_sequence = list(map(int, input().split()))

stack.append(input_sequence[0])
index = len(stack) - 1

for current_number in input_sequence[1:]:
    _sum = current_number
    while index >= 0 and _sum > 0:
        _sum -= stack[index]
        index -= 1
        if _sum == 0:
            # 模拟出栈操作
            stack = stack[: index]

            # 模拟双倍进栈操作
            new_number = current_number * 2
            stack.append(new_number)

    if _sum < 0:
        stack.append(current_number)

    if len(stack) ==0:
        stack.append(current_number)

print(stack)