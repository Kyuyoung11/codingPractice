#더 맵게
#https://programmers.co.kr/learn/courses/30/lessons/42626

# 효율성 -> heapq 사용해야함
import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for value in scoville:
        heapq.heappush(heap, value)

    while (True):

        # 가장 작은 값이 pop됨
        # 가장 큰 값 pop 하려면 넣을때부터 음수로 처리하면됨 (-value)
        first = heapq.heappop(heap)
        if (first >= K):
            break
        if (len(heap) < 1): return -1
        second = heapq.heappop(heap)
        num = first + (second * 2)
        heapq.heappush(heap, num)
        answer += 1

    return answer