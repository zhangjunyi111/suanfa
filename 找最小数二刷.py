

# 找最小数,移除N位数后，剩下的数最小
# 9876543

def main():
    num = input()
    N = int(input())

    # 应该维护一个单调递减的栈
    stack = []


    # 将num转化一下，转化为一个数字列表
    num = list(map(int,num))

    stack.append(num[0])
    for i in range(1,len(num)):
        while N and stack and   stack[-1] >num[i]:
            stack.pop()
            N-=1
        stack.append(num[i])

    while N :
        stack.pop()
        N -= 1

    print(''.join(list(map(str,stack))).lstrip('0'))

main()