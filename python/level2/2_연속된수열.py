#https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=python3

def solution(sequence, k):
    answer = []
    answerSum=0


    end = len(sequence)-1
    element = len(sequence)-1

    # 1. 뒤에부터 가능한 수열 탐색 (가장 짧은 수열)
    while(answerSum!=k):
        # print(answerSum, end, element)
        if(answerSum > k) :
            answerSum-=sequence[end]
            end-=1
        else:
            answerSum+=sequence[element]
            element-=1

    element+=1
    # print(element, end)

    # 2. 길이가 같은 수열 중 앞쪽에서 가능한지 확인
    while(element > 0):
        if(sequence[end]==sequence[element-1]):
            element-=1
            end-=1
        else:
            break


    answer.append(element)
    answer.append(end)
    return answer