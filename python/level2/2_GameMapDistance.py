# 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def bfs(maps):

    queue = deque()
    queue.append((0,0))

    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]

    while(queue):
        # 현재 칸
        x, y = queue.popleft()
        # print(x,y)

        #움직일 수 있는 칸 큐 삽입
        for i in range(len(move_x)):

            new_x = x + move_x[i]
            new_y = y + move_y[i]

            # 이동 가능한지 검증
            if can_move(maps, new_x, new_y) == False:
                continue

            # 최단 거리 계산
            maps[new_x][new_y] = maps[x][y] + 1

            # 큐 삽입
            queue.append((new_x, new_y))

            # print(new_x, new_y, maps[new_x][new_y])

    n = len(maps) -1
    m = len(maps[0]) -1

    # 방문하지 못한 경우
    if(maps[n][m] <= 1):
        return -1

    return maps[n][m]


def can_move(maps, x, y):

    # 유효하지 않은 인덱스로 이동하는 경우
    if (x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0])):
        return False

    # 벽이 있는 칸
    if (maps[x][y] == 0):
        return False

    # 이미 방문한 칸
    if (maps[x][y] > 1):
        return False



def solution(maps):
    return bfs(maps)