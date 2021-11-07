#올바른 괄호
#https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    mystack = []
    for i in s:
        if (i == '('):
            mystack.append(i)
        else:
            if (len(mystack) > 0):
                j = mystack.pop()

            else:
                return False
    if (len(mystack) > 0):
        return False

    return True