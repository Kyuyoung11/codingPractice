#피보나치 수
#https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    n1 = 1
    n2 = 0
    temp = 1
    if (n < 2):
        return n
    for i in range(n - 1):
        n1 = n2 + temp
        n2 = temp
        temp = n1
        answer = n1

    return answer % 1234567