# 求路灯未覆盖的范围的长度

def main():
    N = int(input())
    radiuses = list(map(int, input().strip().split()))

    # 照明区间结果集合
    ans = []
    # 初始化一个长度，表示路灯照不到的区间的长度
    res = 0

    # 计算每个路灯照亮了的区间

    positions = []
    for i in range(N):
        positions.append(100 * i)

    # 遍历位置这里使用索引进行遍历，不能使用for循环进行遍历
    for i in range(len(positions)):
        if i == 0:
            length = [0, radiuses[i]]
        else:
            length = [positions[i] - radiuses[i], positions[i] +
                      radiuses[i]]
        ans.append(length)

    # [20,30] [40,50] [45,55]

    left = ans[0][0]
    right = ans[0][1]
    for i in range(1, N):
        if right < ans[i][0]:
            res += ans[i][0] - right
        right = ans[i][1]

    print(res)


main()
