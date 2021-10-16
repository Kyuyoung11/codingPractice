#완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):

    new_par = sorted(participant)
    new_com = sorted(completion)
    for i in range(len(new_com)):
        if (new_par[i] != new_com[i]):
            return new_par[i]
    return new_par[-1]