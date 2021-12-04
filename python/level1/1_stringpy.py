# 문자열 내 p와 y의 개수
#https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    answer = True
    s = s.lower()
    p_cnt = 0
    y_cnt = 0
    for i in s:
        if (i == 'p'):
            p_cnt += 1
        elif (i == 'y'):
            y_cnt += 1
    if (p_cnt == y_cnt): return True
    else: return False

    return True