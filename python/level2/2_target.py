#타겟 넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165


def solution(numbers, target):
    answer = 0
    num = 1
    for i in range(len(numbers)):
        num *= 2
    num -= 1

    while (num > -1):
        sum = 0
        bit = list(bin(num))[2:]
        while (len(bit) < len(numbers)):
            bit.insert(0, '0')
        for i in range(len(bit)):
            if (bit[i] == '0'):
                sum -= numbers[i]
            else:
                sum += numbers[i]
        if (sum == target):
            answer += 1
        num -= 1

    return answer