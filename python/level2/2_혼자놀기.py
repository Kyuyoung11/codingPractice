from itertools import combinations

def open_box(cards, visited, num):

    # print("open_box", cards, visited, num)

    #이미 열었던 박스이면 중단
    if(visited[num] == True):
        return visited

    #방문 표시
    visited[num] = True

    #열기
    return open_box(cards, visited, cards[num]-1)

def solution(cards):
    answer = 0

    comList = list(combinations(cards,2))

    for com in comList:
        visited = [False] * len(cards)

        box1Visited = open_box(cards, visited, com[0]-1)
        box1Cnt = box1Visited.count(True)

        box2Visited = open_box(cards, box1Visited, com[1]-1)
        box2Cnt = box2Visited.count(True) - box1Cnt

        if(answer < box1Cnt*box2Cnt):
            answer = box1Cnt*box2Cnt


    return answer