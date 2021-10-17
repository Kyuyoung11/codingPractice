#3진법 뒤집기
#https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    answer = 0

    jin = []
    while (n > 0):
        jin.append(n % 3)
        n = n // 3
    # print(jin)
    a = 1
    for i in range(len(jin), 0, -1):
        answer += (a * jin[i - 1])
        a *= 3
    return answer