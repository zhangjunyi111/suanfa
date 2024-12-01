def get_min_num(num, k):
    stack = []

    for i in num:
        while stack and k > 0 and stack[-1] > i:
            stack.pop()
            k -= 1
        stack.append(i)

    # 说明没有删除够
    if k > 0:
        stack = stack[:-k]

    # 如果删除完了,还没有遍历完，stack会循环执行append操作，而不参与while循环
    print(''.join(list(map(str, stack))).strip('0'))


def main():
    num = list(input())
    k = int(input())
    get_min_num(num,k)


main()