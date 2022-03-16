#입국심사
#https://programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    answer = 0
    times = sorted(times)
    start = 0
    end = times[-1] * n
    mid = 0
    # print(start, end)
    while (start <= end):
        mid = (start + end) // 2
        people = 0
        for t in times:
            people += mid // t
            if (people >= n):
                break
        if (people < n):
            start = mid + 1
        elif (people >= n):
            answer = mid
            end = mid - 1

        # print(mid, people)

    return answer