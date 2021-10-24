#약수의 합
#https://programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = 0
    for i in range (0, n):
        if (n % (i+1) == 0):
            answer += (i+1)
    return answer