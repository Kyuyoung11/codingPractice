import heapq

N, D = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(D+1)]
distance = [INF]*(D+1)

# 거리 1로 초기화
for i in range(D):
    graph[i].append((i+1, 1))


for _ in range(N):
    start, end, d = map(int, input().split())
    if(end > D): continue
    graph[start].append((end, d))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)


        if dist > distance[now]:
            continue

        for linked_node in graph[now]:
            cost = dist + linked_node[1]
            if cost < distance[linked_node[0]]:
                distance[linked_node[0]] = cost
                heapq.heappush(q,(cost,linked_node[0]))

dijkstra(0)
print(distance[D])