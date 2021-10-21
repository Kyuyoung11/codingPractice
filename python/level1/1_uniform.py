#체육복
#https://programmers.co.kr/learn/courses/30/lessons/42862

import copy


def solution(n, lost, reserve):
    answer = 0
    temp = copy.deepcopy(lost)
    # print(temp)

    # lost에도 있고 reserve에도 있는 학생 삭제
    for i in range(len(lost)):
        if (lost[i] in reserve):
            temp.remove(lost[i])
            reserve.remove(lost[i])

    lost = copy.deepcopy(temp)
    temp_r = copy.deepcopy(reserve)

    for i in range(len(lost)):

        # 체육복을 빌릴 수 없는 학생 삭제
        if (lost[i] - 1 not in reserve and lost[i] + 1 not in reserve):
            temp.remove(lost[i])
            answer += 1
            continue

        # 체육복을 빌려줄 수 있는 학생 삭제
        if (lost[i] - 1 in temp_r):
            temp_r.remove(lost[i] - 1)
        if (lost[i] + 1 in temp_r):
            temp_r.remove(lost[i] + 1)

    # 체육복을 빌려줄 수 없는 학생을 reserve에서 삭제함
    for i in temp_r:
        reserve.remove(i)

    if (len(reserve) < len(temp)):
        answer += (len(temp) - len(reserve))
    return n - answer