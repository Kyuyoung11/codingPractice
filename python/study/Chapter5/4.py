# 미로 탈출
# N X M 크기의 미로가 있다. 처음 위치는 (1,1) 출구는 (N,M)
# 괴물이 있는 부분은 0, 없는 부분은 1로 표시
# 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. (처음칸, 마지막칸 포함)

from collections import deque


def bfs(n, m, graph):
    queue = deque()
    queue.append((0, 0))  # 시작위치 삽입

    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]

    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]

            if (nx < 0 or nx >= n or ny < 0 or ny >= m):  # 불가능한 인덱스
                continue

            if (graph[nx][ny] == 0):  # 괴물
                continue

            if (graph[nx][ny] > 1):  # 이미 방문한 노드(최단거리를 알고있음)
                continue

            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
            # print(nx, ny, graph[nx][ny])

    return graph[n-1][m-1]


if __name__ == '__main__':
    # 입력 받기
    n, m = map(int, input().split())

    # 그래프
    graph = []

    for i in range(n):
        graph.append(list(map(int, input())))


    print(bfs(n, m, graph))
