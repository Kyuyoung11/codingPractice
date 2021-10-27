#124 나라의 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    num = ['4','1','2']
    while(n > 0):
        answer = num[n%3] + answer
        n = int((n-1)//3)
    return answer