#N개의 최소공배수
#https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    answer = 0
    if (len(arr) == 1): return arr[0]
    arr.sort()

    first = arr[0]
    second = arr[1]
    num = second
    for i in range(1, len(arr)):
        # print(first, second)
        num = second
        while (True):
            if (num % first == 0):
                if (i == len(arr) - 1): return num
                if (num > arr[i + 1]):
                    first = arr[i + 1]
                    second = num
                else:
                    first = num
                    second = arr[i + 1]
                break
            else:
                num += second
        # print(num)

    return num