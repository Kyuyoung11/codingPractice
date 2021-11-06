#모음 사전
#https://programmers.co.kr/learn/courses/30/lessons/84512
def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    add = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        index = alpha.index(word[i])
        answer += index * add[i]

    answer += len(word)
    return answer