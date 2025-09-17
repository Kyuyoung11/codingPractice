import math

def find_divide_number(targetNumber):

    if(targetNumber==1):
        return 0

    num = 1
    max = math.floor(math.sqrt(targetNumber))

    for i in range(2, max+1):

        if(targetNumber % i == 0):
            num = i
            if(targetNumber/i <= 10000000):
                return targetNumber/i
    return num


def solution(begin, end):
    answer =[]

    for i in range(begin,end+1,1) :
        answer.append(find_divide_number(i))

    return answer