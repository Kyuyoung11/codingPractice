#상호 평가
#https://programmers.co.kr/learn/courses/30/lessons/83201
def solution(scores):
    answer = ''

    for i in range(len(scores[0])):
        max = scores[i][i]
        min = scores[i][i]
        count_max = 0
        count_min = 0
        length = len(scores)
        sum = 0

        for j in range(len(scores)):
            sum += scores[j][i]
            if (max <= scores[j][i]):
                max = scores[j][i]
                count_max += 1
            if (min >= scores[j][i]):
                min = scores[j][i]
                count_min += 1

        if (max == scores[i][i] and count_max == 1):
            sum -= scores[i][i]
            scores[i][i] == 0
            length -= 1
        if (min == scores[i][i] and count_min == 1):
            sum -= scores[i][i]
            scores[i][i] == 0
            length -= 1

        avg = sum / length
        print(avg)

        if (avg >= 90):
            answer += 'A'
        elif (avg >= 80):
            answer += 'B'
        elif (avg >= 70):
            answer += 'C'
        elif (avg >= 50):
            answer += 'D'
        else:
            answer += 'F'
    return answer