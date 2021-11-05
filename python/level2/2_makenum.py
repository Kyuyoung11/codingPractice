#큰 수 만들기
#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    count = 0
    while (k - count > 0):
        if (len(number) - (k - count) == 1):
            answer += max(number)
            return answer
        else:
            max_index = 0
            if (number[max_index] != "9"):
                for i in range(1, (k - count) + 1):
                    if (number[i] == "9"):
                        max_index = i
                        break
                    if (number[max_index] < number[i]):
                        max_index = i

            count += max_index
            answer += number[max_index]
            if (len(number) != max_index):
                number = number[max_index + 1:]
            else:
                number = ''
                break
        # print(answer + number)

    if (len(number) > 0):
        answer += number

    return answer