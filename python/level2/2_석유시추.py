from collections import deque

def bfs(land, i, j, visited, oil_cnt):
    dx =[0,0,1,-1]
    dy =[1,-1,0,0]
    n, m = len(land), len(land[0])
    oil_range = set()

    queue = deque()
    queue.append((i,j))

    visited[i][j]=True
    oil_range.add(j)
    area = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 공간 벗어난 경우
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue


            if(land[nx][ny] == 1 and visited[nx][ny] == False):
                queue.append((nx,ny))
                visited[nx][ny] = True
                oil_range.add(ny)
                area+=1

    for c in oil_range:
        oil_cnt[c]+=area

    return area, visited, oil_cnt


def solution(land):
    answer = 0
    n,m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_cnt = [0] * m


    for j in range(m):
        for i in range(n):
            if(land[i][j]==1 and visited[i][j]==False):
                area, visited, oil_cnt = bfs(land, i, j, visited, oil_cnt)



    return max(oil_cnt)