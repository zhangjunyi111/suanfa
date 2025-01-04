class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)


UNVISITED, VISITING, VISITED = 0, 1, 2


# cyclic:环的，循环的、周期的
def has_cycle(graph):
    visited = {node: UNVISITED for node in graph}
    for node in graph:
        if visited[node] == UNVISITED:
            detect_cycle(graph, node, visited)


# 判断是否有环的工具
def detect_cycle(graph, v, visited):
    visited[v] = VISITING
    for neighber in graph.get(v, []):
        if visited[neighber] == UNVISITED:
            if detect_cycle(graph, v, visited):
                return True
        elif visited[neighber] == VISITED:
            return True
    visited[v] = VISITED
    return False


def find_start_and_end_nodes(edges,graph):
    '''
    :param nodes:
    :return:
    '''
    in_degree = {}
    out_degree = {}
    nodes = set()

    for i in range(0, len(edges), 2):
        start, end = edges[i], edges[i + 1]
        in_degree.get(end, 0) + 1
        out_degree.get(start, 0) + 1
        nodes.add(start)
        nodes.add(end)

    has_cycle(graph)
    start_node = -1
    end_node = []
    for node in nodes:
        if node not in in_degree:
            start_node = node

        if node not in out_degree:
            end_node.append(node)

    return [start_node] + end_node


if __name__ == '__main__':
    g = Graph()
    pairs = int(input())
    edges = list(map(int, input().split()))
    for i in range(0,len(edges),2):
        g.add_edge(edges[i],edges[i+1])
    res = find_start_and_end_nodes(edges,g.graph)
    print(res)



