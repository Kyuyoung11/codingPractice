#JadenCase 문자열 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3
def solution(s):
    s = s.lower()
    j_list = s.split(" ")
    for i in range(len(j_list)):
        if (len(j_list[i]) < 2):
            j_list[i] = j_list[i].upper()
            continue
        j_list[i] = j_list[i][0].upper() + j_list[i][1:]
    return " ".join(j_list)