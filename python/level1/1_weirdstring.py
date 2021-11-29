#이상한 문자 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer = []
    n = 1
    for i in s:
        if (i == ' '):
            answer.append(' ')
            n=1
        elif (n==1):
            answer.append(i.upper())
            n=0
        elif (n==0):
            answer.append(i.lower())
            n=1
    return ''.join(answer)