#같은 숫자는 싫어
#https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(0, len(arr)):
        if (len(answer) == 0):
            answer.append(arr[i])
        else:
            if (arr[i - 1] != arr[i]):
                answer.append(arr[i])

    return answer