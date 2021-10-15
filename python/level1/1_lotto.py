#로또의 최고 순위와 최저 순위
#https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    count = 0
    zero = 0
    for i in lottos:
        if (i in win_nums):
            count += 1
        if (i == 0):
            zero += 1
    if (count + zero == 0):
        answer.append(6)
    else:
        answer.append(7 - count - zero)
    if (count == 0):
        answer.append(6)
    else:
        answer.append(7 - count)

    return answer
