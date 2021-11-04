#가장 큰 수
#https://programmers.co.kr/learn/courses/30/lessons/42746


import itertools


def solution(numbers):
    num_str = [str(num) for num in numbers]
    # print(num_str[0]*4)
    num_str.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # print(num_str)

    if num_str[0] != '0':
        answer = "".join(num_str)
        return answer
    else:
        return "0"


    return answer

