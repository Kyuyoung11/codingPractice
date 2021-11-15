#소수 찾기
#https://programmers.co.kr/learn/courses/30/lessons/12921

import math
def solution(n):
    answer = 0
    if (n < 4): return 1
    answer += 2
    for i in range(4,n+1):
        for j in range(2,math.ceil(math.sqrt(i))+1):
            if (i%j == 0):
                break
        else:
            answer+=1
    return answer