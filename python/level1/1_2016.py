#2016년
#https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    answer = ''
    day_arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 , 31]
    day_sum = sum(day_arr[:a-1]) + b
    # print(sum(day_arr[:a-1]))
    day = day_sum % 7
    print(day_sum)
    if (day == 1): answer = 'FRI'
    elif (day ==2): answer = 'SAT'
    elif (day == 3): answer = 'SUN'
    elif (day == 4): answer = 'MON'
    elif (day ==5): answer = 'TUE'
    elif (day ==6): answer = 'WED'
    else : answer = 'THU'
    return answer