#기능개발
#https://programmers.co.kr/learn/courses/30/lessons/42586

import math


def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    # print(days)
    count = 1
    now = 0
    for i in range(1, len(days)):
        if (days[now] >= days[i]):
            count += 1
        else:
            answer.append(count)
            now = i
            count = 1

    answer.append(count)
    return answer