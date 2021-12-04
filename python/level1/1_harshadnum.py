#하샤드 수
#https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    ha = 0
    num = x

    while (num > 0):
        ha += num % 10
        num //= 10

    if (x % ha == 0):
        return True
    else:
        return False