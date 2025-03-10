class Edge:
    def __init__(self, u, v, cost, pre):
        self.u = u
        self.v = v
        self.cost = cost
        self.pre = pre


parent = [i for i in range(N + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])


def union(x, y):
    if find(x) != find(y):
        parent[find(x)] = find(y)


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    edges = []
    for _ in range(M):
        x, y, z, p = map(int, input().split())
        edges.append(Edge(x, y, z, p))

    edges.sort(key=lambda edge: edge.cost)
    cost = 0
    for edge in edges:
        # 如果边的俩个端点不在同一个集合中，那么就将这条边添加到最小生成树中
        if find(edge.u) != find(edge.v):
            cost += edge.cost
            union(edge.u, edge.v)

    for i in range(2, N + 1):
        if find(i) != find(1):
            print(-1)
            break
        else:
            print(cost)
