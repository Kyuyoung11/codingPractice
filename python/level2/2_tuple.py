#튜플
#https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    my_list = []
    s_list = []
    num = ''
    for i in s:
        if (i.isdigit()):
            # print(num)
            num += i
        elif (i == ',' and len(num) > 0):
            my_list.append(int(num))
            num = ''

        elif (i == '}' and len(num) > 0):
            # print(num)
            my_list.append(int(num))
            num = ''
            if (len(my_list) > 0):
                s_list.append(my_list)
                my_list = []

    s_list = sorted(s_list, key=lambda x: len(x))
    # print(s_list)
    for i in s_list:
        for j in i:
            if (j not in answer):
                answer.append(j)
    return answer