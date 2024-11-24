import math

# 接收输入的数字和行数
nums, rows = map(int, input().split())

# 计算列数
cols = math.ceil(nums / rows)

# 初始化螺旋矩阵
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
left, right, top, bottom = 0, cols - 1, 0, rows - 1
num = 1

while num <= nums:
    for i in range(left, right + 1):
        if num <= nums:
            matrix[top][i] = num
            num += 1

    top += 1
    for i in range(top, bottom+1):
        if num <= nums:
            matrix[i][right] = num
            num += 1

    right -= 1

    for i in range(right, left - 1, -1):
        if num <= nums:
            matrix[bottom][i] = num
            num += 1


    bottom -= 1

    for i in range(bottom, top - 1, -1):
        if num <= nums:
            matrix[i][left] = num
            num += 1

    left += 1

for row in matrix:
    print(' '.join(["*" if x == 0 else str(x) for x in row]))






