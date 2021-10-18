#예산
#https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    new_list = d
    for i in range(len(d)):
        if (sum(new_list) <= budget):
            return len(new_list)
        new_list.remove(max(new_list))
    return answer