res = []


class Edges:
    def __init__(self, edges):
        self.edges = edges
        self.edge_dict = dict()

    def create_edge_dict(self):
        for edge in self.edges:
            if edge not in self.edge_dict:
                self.edge_dict[edge] = 0
            self.edge_dict[edge] += 1

    def deleteEdge(self, Edge):
        self.edge_dict[Edge] -= 1

    def getEdge(self, Edge):
        return self.edge_dict[Edge]


def main():
    global res
    # 初始化一个used数组
    test_cases = int(input())
    input_data = []

    # 初始化一个边的集合，该集合初始化时为空
    edges = []
    for _ in range(test_cases):
        input_data.append(list(map(int, input().split())))
    for test_case in input_data:
        used = [False] * len(test_case)
        my_edge = Edges(test_case)
        my_edge.create_edge_dict()
        get_right_triangle_number(test_case, used, edges, my_edge)
        print(len(res))
        # print(res)
        res = []


def get_right_triangle_number(arr, used, edges, my_edge):
    global res
    # global res2
    # 首先计算传进来的数据能组成哪些三角形组合
    # 再从这些组合中排除不能构成直角三角形的情况
    if len(edges) == 3:
        edges_sorted = sorted(edges)
        a = edges_sorted[0]
        b = edges_sorted[1]
        c = edges_sorted[2]
        if [a, b, c] in res:
            return
        if a ** 2 + b ** 2 == c ** 2:
            if my_edge.getEdge(a) and my_edge.getEdge(b) and my_edge.getEdge(c):
                res.append([a, b, c].copy())
                for edge in [a, b, c]:
                    my_edge.deleteEdge(edge)
        return

    for i in range(len(arr)):
        if not used[i]:
            edges.append(arr[i])
            used[i] = True
            get_right_triangle_number(arr, used, edges,my_edge)
            used[i] = False
            edges.pop()


main()
