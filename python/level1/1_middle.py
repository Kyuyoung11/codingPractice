#가운데 글자 가져오기
#https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

def solution(s):
    answer = ''

    if (len(s) % 2 == 0):
        answer = s[int(len(s) / 2 - 1)] + s[int(len(s) / 2)]
    else:
        answer = s[int(len(s) / 2)]
    return answer