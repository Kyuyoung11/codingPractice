def make_graph(node_cnt, edge_cnt):
    graph = [[0] * (node_cnt+1) for _ in range(node_cnt + 1)]
    # 그래프 만들기
    for _ in range(edge_cnt):
        node1, node2 = map(int, input().split())

        graph[node1][node2] = 1
        graph[node2][node1] = 1

    return graph


def dfs(graph, visited, node):
    if visited[node]:
        return

    visited[node] = True
    print(node, end=" ")

    for i in range(1, len(graph)):
        if graph[node][i] == 1:
            dfs(graph, visited, i)


def bfs(graph, visited, node):
    queue = deque()
    queue.append(node)

    while queue:
        cur_node = queue.popleft()
        visited[cur_node] = True
        print(cur_node, end=" ")

        for i in range(1, len(graph)):
            if graph[cur_node][i] != 1 or visited[i] or i in queue:
                continue

            queue.append(i)


from collections import deque

node_cnt, edge_cnt, start = map(int, input().split())
# print(node_cnt, edge_cnt, start)

# 그래프 생성
graph = make_graph(node_cnt, edge_cnt)

# dfs
visited = [False for _ in range(node_cnt + 1)]
dfs(graph, visited, start)
print()

# bfs
visited = [False for _ in range(node_cnt + 1)]
bfs(graph, visited, start)
