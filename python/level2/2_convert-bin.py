#이진 변환 반복하기
#https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3
def solution(s):
    answer = []
    zero_cnt = 0
    num = 0
    cnt = 0

    while (len(s) > 1):
        num = s.count('1')
        zero_cnt += s.count('0')
        s = str(bin(num))[2:]
        # print(s)
        cnt += 1

    answer.append(cnt)
    answer.append(zero_cnt)

    return answer