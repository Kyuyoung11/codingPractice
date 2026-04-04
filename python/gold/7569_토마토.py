from collections import deque

M,N,H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# print(box)


visited = [[[False] * M for _ in range(N)] for _ in range(H)]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]


q = deque()

# 초기 토마토 확인
for x in range(H):
    for y in range(N):
        for z in range(M):
            if box[x][y][z] == 1 and not visited[x][y][z]:
                q.append([x,y,z,0])

day = 0

# 토마토 퍼트리기
while q:
    cur_x, cur_y, cur_z, day = map(int, q.popleft())
    visited[cur_x][cur_y][cur_z] = True

    for i in range(len(dx)):
        nx, ny, nz = cur_x+dx[i], cur_y+dy[i], cur_z+dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
            if box[nx][ny][nz] == 0 and not visited[nx][ny][nz]:
                box[nx][ny][nz] = 1
                q.append([nx,ny,nz,day+1])


for x in range(H):
    for y in range(N):
        for z in range(M):
            if box[x][y][z] == 0:
                print(-1)
                exit()


print(day)

