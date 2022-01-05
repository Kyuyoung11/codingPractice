#짝지어 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    answer = 0
    s_stack = []
    for i in range(len(s)):
        if (len(s_stack) > 0):
            if (s_stack[-1] == s[i]):
                s_stack.pop()
            else:
                s_stack.append(s[i])
        else:
            s_stack.append(s[i])

    if (len(s_stack) == 0):
        return 1

    return answer