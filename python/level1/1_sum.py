#두 정수 사이의 합
#https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    answer = 0
    if (a<b):
        x = a
        y = b
    else :
        x = b
        y = a
    for i in range(x,(y+1),1):
        answer += i
    return answer