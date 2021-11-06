#주식가격
#https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = []

    for i in range(0, len(prices)):
        now = prices[i]
        answer.append(0)
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if (prices[j] < now):
                break

    return answer