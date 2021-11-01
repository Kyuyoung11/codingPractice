#실패율
#https://programmers.co.kr/learn/courses/30/lessons/42889
import numpy as np
def solution(N, stages):
    answer = []
    stop = [0] * N
    np_count = np.array([0] * N)

    for j in stages:
        np_count[:j] += 1
    for i in range(1, N + 1):
        stop[i - 1] = stages.count(i)
    print(np_count, stop)

    fail = {}
    for i in range(len(np_count)):
        if (np_count[i] == 0):
            fail[i + 1] = 0
        else:
            fail[i + 1] = stop[i] / np_count[i]
    print(fail)

    return sorted(fail, key=lambda x: fail[x], reverse=True)