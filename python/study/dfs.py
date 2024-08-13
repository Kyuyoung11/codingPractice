#그래프에서 각 노드가 연결된 형태를 기록
# 1.인접 행렬 - 2차원 배열로 표현
def example_matrix() :
    INF = 987654321 # 무한의 비용 선언
    graph = [
        [0,7,5],
        [7,0,INF],
        [5,INF,0]
    ]

# 2. 인접 리스트 방식
def example_list() :
    graph = [[] for _ in range(3)]

    ## 노드 0에 연결된 노드 정보 저장 (노드, 거리)
    graph[0].append((1,7))
    graph[0].append((2,5))

    ## 노드 1에 연결된 노드 정보 저장(노드, 거리)
    graph[1].append((0,7))


    ## 노드 2에 연결된 노드 정보 저장(노드, 거리)
    graph[2].append((0,5))



#------------------------------------------------------#
# 특정 노드와 연결된 모든 인접 노드를 순회해야하는 경우 => 인접 리스트 방식을 사용해야 메모리 공간의 낭비가 적음
# 노드 순회 시, 스택으로 방문 처리를 표시하는 것이 일반적임
#  1) 스택에 삽입하고 방문 처리
#  2) 인접 노드를 스택에 삽입하고 방문 처리
#  3) 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄

def dfs(graph, v, visited):
    # 1. 노드 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 2. 연결노드 방문 처리
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


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

    dfs(graph, 1, visited)


