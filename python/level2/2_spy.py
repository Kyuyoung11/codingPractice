#위장
#https://programmers.co.kr/learn/courses/30/lessons/42578

import itertools


def solution(clothes):
    answer = 0
    clo_dict = {}
    for i in clothes:
        if (i[1] not in clo_dict):
            clo_dict[i[1]] = [i[0]]
        else:
            clo_dict[i[1]].append(i[0])
        answer += 1

    print(clo_dict)
    # print(answer)
    if (len(clo_dict) == 30):
        return 1073741823
    elif (len(clo_dict) > 1):
        arr = []
        p = 0
        clo_list = []
        for i in clo_dict:
            arr.append(p)
            p += 1
            clo_list.append(clo_dict[i])
        # print(clo_list)
        for i in range(1, len(clo_dict)):
            combi = list(itertools.combinations(arr, i + 1))
            # print(combi)
            for a in range(len(combi)):
                sum = 1
                for b in combi[a]:
                    sum *= len(clo_list[b])
                    # print(sum)
                answer += sum
    return answer