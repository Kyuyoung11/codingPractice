#[카카오 인턴] 수식 최대화
#https://programmers.co.kr/learn/courses/30/lessons/67257
import copy


def solution(expression):
    answer = []
    num_list = []
    cal_list = []
    cal_pri = ["+-*", "-*+", "*-+", "+*-", "-+*", "*+-"]
    num = ''
    for i in expression:
        if (i.isdigit()):
            num += i
        else:
            num_list.append(int(num))
            cal_list.append(i)
            num = ''
    num_list.append(int(num))
    for cal in cal_pri:
        temp = copy.deepcopy(num_list)
        temp_cal = copy.deepcopy(cal_list)
        for i in cal:
            while (temp_cal.count(i) > 0):
                index = temp_cal.index(i)
                if (i == '+'):
                    temp[index] = temp[index] + temp[index + 1]
                elif (i == '-'):
                    temp[index] = temp[index] - temp[index + 1]
                else:
                    temp[index] = temp[index] * temp[index + 1]
                temp_cal.remove(i)
                del temp[index + 1]
            # print(cal, temp)
        answer.append(abs(temp[0]))

    return max(answer)