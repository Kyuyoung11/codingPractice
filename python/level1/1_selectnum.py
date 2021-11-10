#두 개 뽑아서 더하기
#https://programmers.co.kr/learn/courses/30/lessons/68644

import itertools
def solution(numbers):
    answer = []
    com = list(itertools.combinations(numbers,2))
    for i in com:
        answer.append(i[0]+i[1])
    answer = sorted(list(set(answer)))
    return answer