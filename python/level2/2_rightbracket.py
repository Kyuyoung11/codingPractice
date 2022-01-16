#괄호 변환
#https://programmers.co.kr/learn/courses/30/lessons/60058#
def right_str(p):
    u = ''
    l_cnt = 0
    r_cnt = 0
    index = -1
    flag = True
    stack = []
    for i in range(len(p)):
        if (p[i] == '('):
            l_cnt += 1
            stack.append(i)
        else:
            r_cnt += 1
            if (len(stack) > 0):
                stack.pop()
            else:
                flag = False
        u += p[i]
        if (l_cnt == r_cnt):
            index = i
            break

    v = p[index + 1:]

    if (flag == False):
        # print("1", u,v)
        temp = '(' + right_str(v) + ')'
        for j in range(1, len(u) - 1):
            if (u[j] == '('):
                temp += ')'
            else:
                temp += '('
        # print(temp)
        return temp
    elif (flag == True and len(v) == 0):
        # print("2", u, v)
        return u
    else:  # flag == True and len(v)>0
        # print("3", u, v)
        u += right_str(v)
        return u


def solution(p):
    if (len(p) == 0): return ''

    return right_str(p)