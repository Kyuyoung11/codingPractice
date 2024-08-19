# 음료수 얼려 먹기
# N X M 크기의 얼음틀이 있다. 구멍 뚫려있으면 0, 칸막이는 1로 표시
# 뚫려있는 부분 상하좌우 붙여있으면 연결되어 있는 것으로 간주

# 얼음틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오



def dfs(graph, visited, n, m):


    # 아이스크림 영역 찾기
    result = 0
    for i in range(n):
        for j in range(m):
            if move_oneblock(graph, visited, i, j): #찾은 경우
                result += 1

    return result







def move_oneblock(graph, visited, n, m):

    # 이동 불가능한 index에 위치한 경우
    if (n < 0 or n >= len(graph)  or m < 0 or m >= len(graph[0]) ) : return False

    #이미 방문한 노드이면 return
    if(visited[n][m] or graph[n][m] == 1) : return False


    # 방문 표시
    visited[n][m] = True
    # print("visit : ", n, " ", m, " --> ", graph[n][m], " ", visited[n][m])


    # 이동
    # 1. 상
    move_oneblock(graph, visited, n-1, m)
    # 2. 하
    move_oneblock(graph, visited, n+1, m)
    # 3. 좌
    move_oneblock(graph, visited, n, m-1)
    # 4. 우
    move_oneblock(graph, visited, n, m+1)

    return True







if __name__ == '__main__':

    # 입력 받기
    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    visited = [[False] * m for _ in range(n)]

    print(dfs(graph, visited, n,m))



