#소수 찾기
#https://programmers.co.kr/learn/courses/30/lessons/42839
import itertools
import math


def solution(numbers):
    answer = 0
    num_list = []
    for i in range(1, len(numbers) + 1):
        temp = list(itertools.permutations(list(numbers), i))
        for j in temp:
            num = int("".join(j))
            if (num not in num_list and num > 1):
                num_list.append(num)
    # print(num_list)

    for i in num_list:
        for j in range(math.ceil(math.sqrt(i)), i):
            if (i % j == 0):
                # print(i,j)
                break
        else:
            answer += 1
    return answer