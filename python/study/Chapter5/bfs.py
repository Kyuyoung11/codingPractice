# 탐색 알고리즘 - BFS
#  - BFS - 큐 + 큐자료구조

from collections import deque

def bfs(graph, start, visited) :
    queue = deque([start])

    #현재 노드 방문 처리
    visited[start] = True

    #큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == '__main__':
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    visited = [False] * 9

    bfs(graph, 1, visited)
