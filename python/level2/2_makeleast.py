#최솟값 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12941

import heapq
def solution(A,B):
    answer = 0
    heapa = []
    heapb = []
    for i in range(len(A)):
        heapq.heappush(heapa, A[i])
        heapq.heappush(heapb, -B[i])
    #print(heapa, heapb)

    while(len(heapa) > 0):
        a = heapq.heappop(heapa)
        b = -heapq.heappop(heapb)
        answer += (a*b)

    return answer