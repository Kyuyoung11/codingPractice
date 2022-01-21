#[1차] 뉴스 클러스터링
#https://programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    answer = 0
    str1 = list(str1.lower())
    str2 = list(str2.lower())
    # print(str1, str2)

    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        element = [str1[i], str1[i + 1]]
        if (str1[i].isalpha() and str1[i + 1].isalpha()):
            str1_list.append(element)
    for i in range(len(str2) - 1):
        if (str2[i].isalpha() and str2[i + 1].isalpha()):
            str2_list.append([str2[i], str2[i + 1]])
    # print(str1_list)
    # print(str2_list)
    union = len(str1_list)
    inter = 0

    for i in str2_list:
        # print(str1_list)
        if (i in str1_list):
            inter += 1
            str1_list.remove(i)
        else:
            union += 1
    # print(union, inter)
    if (inter == 0 and union == 0): return 65536
    return int(inter / union * 65536)