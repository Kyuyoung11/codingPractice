#https://school.programmers.co.kr/learn/courses/30/lessons/340212

def calculate_time(diffs, times, level):
    time_sum = 0
    for i in range(len(diffs)):
        add_time = 0
        if(diffs[i] - level > 0):
            add_time = (times[i] + times[i-1]) * (diffs[i] - level)
        time_sum += add_time + times[i]
    return time_sum

def solution(diffs, times, limit):
    answer = 0

    min_level = 0
    max_level = max(diffs)

    while(max_level - min_level > 1):
        mid_level = (min_level+max_level)//2
        time_sum = calculate_time(diffs,times, mid_level)

        if(time_sum > limit):
            min_level = mid_level
        else:
            max_level = mid_level

    # print(min_level, max_level)

    return max_level