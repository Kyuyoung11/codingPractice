#문자열 다루기 기본
#https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    answer = True
    if (len(s) == 4 or len(s) == 6):
        # 검색 -> try catch 문
        try:
            int(s)
            answer = True
        except ValueError:
            answer = False
    else:
        answer = False

    return answer