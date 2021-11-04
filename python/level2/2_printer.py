#프린터
#https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    list_pri = []
    for i in range(len(priorities)):
        list_pri.append([i, priorities[i]])
    # print(list_pri)

    list_answer = []
    while (len(list_pri) > 1):
        for i in range(1, len(list_pri)):
            if (list_pri[0][1] < list_pri[i][1]):
                list_pri.append(list_pri[0])
                del list_pri[0]
                break
        else:
            list_answer.append(list_pri[0])
            del list_pri[0]

        # print(list_pri)
    # print(list_answer)
    list_answer.append(list_pri[0])
    for i in range(0, len(list_answer)):
        if (list_answer[i][0] == location):
            answer = i + 1

    return answer