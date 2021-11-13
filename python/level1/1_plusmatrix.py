#행렬의 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        list = []
        for j in range(len(arr1[i])):
            num = arr1[i][j] + arr2[i][j]
            list.append(num)
        answer.append(list)
    return answer