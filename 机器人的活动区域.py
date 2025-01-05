# 定义好深度优先遍历的函数
import sys


def dfs(matrix, i, j,visited):
    range = 1
    # 初始化一个方向列表
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    pass
    for dir in directions:
        x = i + dir[0]
        y = j + dir[1]
        if 0 <= x < m and 0 <= y < n and abs(matrix[x][y]-matrix[i][j]) <= 1 \
                and not visited[x][y]:
            visited[x][y] = True
            range += dfs(matrix, x, y,visited)
            visited[x][y] = False
    return range


# 接收区域的长度和宽度，并接收每个网格上的数字
m = 0
n = 0
matrix = []
max_range = 0
for line in sys.stdin:
    if not m and not n:
        m, n = map(int, line.split())

    else:
        # 不能直接添加map对象
        matrix.append(list(map(int, line.split())))
        if len(matrix) == m:
            break

# 遍历网格的每一个位置，进行深度优先遍历，寻找最大的活动范围

for i in range(m):
    for j in range(n):
        visited =[[False for _ in range(n)] for _ in range(m)]
        visited[i][j] = True
        activite_range = dfs(matrix, i, j,visited)
        visited[i][j] = False
        max_range = max(activite_range, max_range)

print(max_range)