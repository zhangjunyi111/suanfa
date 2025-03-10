class UnionFind:
    """
    UnionFind用于实现并查集的数据结构
    """
    def __init__(self, n):
        """

        :param n:   # 参数n表示节点的数量
        """
        # parent表示每个节点的父节点，初始状态下每个节点的父节点都是他自己，表示每个节点都是一个
        # 独立的集合
        self.parent = list(range(n))
        # rank列表表示每个集合的秩，或者高度所有集合的秩都初始化为0，秩用于优化合并操作，确保合并后的树尽可能平衡
        self.rank = [0] * n

    def find(self, u):
        """

        :param u:表示要查找的节点
        :return:
        """
        # 检查u的父节点是不是自己，如果不是，继续查找
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # 路径压缩
        #     返回集合u的代表元素
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        # 检查u和v是否属于同一个结合，如果他们的根节点不同，则不是同一个集合，进行合并
        if root_u != root_v:
            # 按秩合并
            if self.rank[root_u] > self.rank[root_v]:
                # 将v的根节点的父节点设置为u
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                # 将u的根节点的父节点设置为v
                self.parent[root_u] = root_v
            else:
                # u所在集合的秩等于v所在集合的秩，将一个集合合并到另一个集合，将目标集合的秩+1
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(n, edges):
    """

    :param n: n表示途中的节点
    :param edges: edges表示图中的边
    :return:
    """
    # 初始化并查集
    # UnionFind用于管理图的联通性
    uf = UnionFind(n)
    # 按边权排序
    edges.sort(key=lambda x: x[2])
    # mst用于存储最小生成树的边
    mst = []
    # mst_Weight用于生成最小生成树的总权重
    mst_weight = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v))
            mst_weight += weight

    return mst, mst_weight


# 示例
n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]