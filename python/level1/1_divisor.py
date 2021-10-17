#약수의 개수와 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = 0
    cnt = [0] * (right - left + 1)
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if (i % j == 0):
                cnt[i - left] += 1
    for i in range(len(cnt)):
        if (cnt[i] % 2 == 0):
            answer += (left + i)
        else:
            answer -= (left + i)

    return answer