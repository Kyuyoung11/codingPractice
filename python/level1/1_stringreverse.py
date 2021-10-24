#문자열 내림차순으로 배치하기
#https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    answer = ''
    # for i in sorted(s, reverse=True):
    #     answer += i

    new_list = list(s)
    for i in range(len(s)):
        max = new_list[0]
        for i in range(len(new_list)):
            if (max < new_list[i]):
                max = new_list[i]
        answer += max
        new_list.remove(max)

    return answer