# 2 2
# 1 0
# 1 1
# 定义深度优先遍历的算法
def dfs(x, y):

    # 在确定x和y在边界范围内的情况下，再去访问arr或者visited数组
    # 退出深度优先遍历的情况
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] == True or arr[x][
        y] == 0:
        return 0
    count = 1
    visited[x][y] = True
    count += dfs(x, y + 1)
    count += dfs(x, y - 1)
    count += dfs(x + 1, y)
    count += dfs(x - 1, y)
    return count


# 接收矩阵的行和列
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]


# 局域网的数量算法实现
# 此算法的关键是要将四个方向的值加起来

# 定义一个ans表示局域网数量的最大值,注意n和m别弄反了
def main(n, m):
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(dfs(i, j), ans)
    print(ans)


main(n, m)
