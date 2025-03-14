# 接收操作序列
operate_list = input().split()

# 初始化state,左右前后上下
state = [0, 1, 2, 3, 4, 5, 6]


# 定义旋转函数

def rotate(state, a, b, c, d):
    tmp = state[d]
    state[d] = state[c]
    state[c] = state[b]
    state[b] = state[a]
    state[a] = tmp


for x in operate_list:
    if x == 'L':
        rotate(state, 6, 2, 1, 5)

    elif x == 'R':
        rotate(state, 1, 5, 2, 6)

    elif x == 'F':
        rotate(state, 5, 3, 6, 4)

    elif x == 'B':
        rotate(state, 4, 6, 3, 5)

    elif x == 'A':
        rotate(state, 1, 3, 2, 4)
    elif x == 'C':
        rotate(state, 4, 2, 3, 1)


print(state)