#멀쩡한 사각형
#https://programmers.co.kr/learn/courses/30/lessons/62048
import math


def solution(w, h):
    answer = w * h
    sum = 0
    temp = 0
    if w == h:
        return answer - w
    elif w == 1 or h == 1:
        return 0

    num = 1
    for i in range(min(w, h), 0, -1):
        if (w % i == 0 and h % i == 0):
            num = i
            break
    if (num == 1):
        sum = w + h - 1
    else:
        sum = (w / num + h / num - 1) * num

    return answer - sum