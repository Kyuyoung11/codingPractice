#실패율
#https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    count = [0] * N
    stop = [0] * N

    for j in stages:
        for i in range(1, N + 1):
            if (i >= j):
                count[i - 1] += 1
                stop[i - 1] += 1
                break
            else:
                count[i - 1] += 1
    # print(count, stop)

    fail = []
    for i in range(len(count)):
        if (count[i] == 0):
            fail.append(0)
        else:
            fail.append(stop[i] / count[i])

    new_dict = dict(zip(range(len(fail)), fail))
    # print(new_dict)

    rank = sorted(new_dict.items(), key=lambda item: item[1], reverse=True)

    # print(rank)

    for i in range(len(rank)):
        answer.append(rank[i][0] + 1)

    # for i in range(len(fail)):
    #     max_index = fail.index(max(fail))
    #     answer.append(max_index+1)
    #     fail[max_index] = -1

    return answer