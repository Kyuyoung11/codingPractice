#신규 아이디 추천
#https://programmers.co.kr/learn/courses/30/lessons/72410
import copy


def solution(new_id):
    answer = ''
    # 1단계 : 모든 대문자 -> 소문자
    new_id = list(new_id.lower())
    # print(new_id)

    # new = []
    new = copy.deepcopy(new_id)
    # print(new)
    # 2단계 소문자, 숫자, 빼기, 밑줄, 마침표
    for i in new:
        if (i.islower() != True and i.isdigit() != True and i != '-' and i != '_' and i != '.'):
            new_id.remove(i)
    # print(new_id)

    if (len(new_id) == 0): return "aaa"
    str_id = "".join(new_id)
    # print(str_id)
    # 3단계 .. -> .
    if (".." in str_id):
        dot_index = []
        for i in range(len(new_id) - 1):
            if (new_id[i] == '.' and new_id[i + 1] == '.'):
                dot_index.append(i)
        for index in range(len(dot_index)):
            del new_id[dot_index[index] - index]
    # print(new_id)

    if (new_id[0] == '.'):
        del new_id[0]
    if (len(new_id) == 0): return "aaa"
    if (new_id[-1] == '.'):
        del new_id[-1]
    if (len(new_id) == 0): return "aaa"
    if (len(new_id) >= 16):
        new_id = new_id[:15]
        if (new_id[-1] == '.'):
            del new_id[-1]
    if (len(new_id) <= 2):
        while (len(new_id) < 3):
            new_id.append(new_id[-1])
    # print(new_id)

    answer = "".join(new_id)

    return answer