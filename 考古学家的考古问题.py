# start 2024年12月8日 16:17分开始
# end
def dfs(current_content, n, content, visited):
    global res
    if len(current_content) == n:
        res.append(current_content.copy())
        return

    for i in range(n):
        if not visited[i]:
            current_content.append(content[i])
            visited[i] = True
            dfs(current_content, n, content,visited)
            current_content.pop()
            visited[i] = False


res = []


def main():
    global res
    # 接收数量
    n = int(input().strip())

    # 接收内容
    content = input().strip().split()

    # 进行全新的排列组合
    current_content = []
    visited = [False] * n
    dfs(current_content, n, content, visited)
    # print(res)
    s = lambda x: ''.join(x)
    res =  list(map(s,res))
    res = list(set(res))
    res.sort()
    for x in res:
        print(x)


main()