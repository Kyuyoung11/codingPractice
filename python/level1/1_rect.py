#최소직사각형
#https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    answer = 0
    w = []
    h = []
    for i in sizes:
        if (i[0] > i[1]):
            w.append(i[0])
            h.append(i[1])
        else:
            h.append(i[0])
            w.append(i[1])
    #print(w,h)
    return max(w) * max(h)