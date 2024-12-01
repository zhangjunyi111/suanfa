directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# 约定第一个入口为person1
person1_can_arrive_place = []
person2_can_arrive_place = []
person1_has_visited = False
person2_has_visited = False


def main():
    global person1_has_visited
    n, m = map(int, input().split())
    my_map = [list(map(int,input().split())) for _ in range(n)]
    visited =[[False for _ in range(m)] for _ in range(n)]
    # 找到俩个人先
    for i in range(n):
        for j in range(m):
            # 如果值等于2代表找到入口
            if my_map[i][j] == 2:
                pos = (i, j)
                if not person1_has_visited:
                    visited[i][j] = True
                    can_arrive_place(pos, n, m, my_map,visited)
                    person1_has_visited = True
                    visited[i][j] = False
                elif person1_has_visited:
                    visited[i][j] = True
                    can_arrive_place(pos, n, m, my_map,visited)
                    visited[i][j] = False
    print(set(person1_can_arrive_place))
    print(set(person2_can_arrive_place))



def can_arrive_place(pos, n, m, my_map,visited):
    # 定义上下左右四个方向
    x = pos[0]
    y = pos[1]
    if my_map[x][y] == 3:
        if not person1_has_visited:
            person1_can_arrive_place.append([x,y])
        elif person1_has_visited:
            person2_can_arrive_place.append([x, y])

    for direction in directions:
        x_new = x + direction[0]
        y_new = y + direction[1]
        # 判断有么有越界，如果越界了就不用进行深度优先遍历
        if 0 <= x_new < n and 0 <= y_new < m and my_map[x_new][y_new] != 1 \
                and not visited[x_new][y_new]:
            visited[x_new][y_new] = True
            pos = (x_new, y_new)
            can_arrive_place(pos, n, m, my_map,visited)
            visited[x_new][y_new] = False


main()