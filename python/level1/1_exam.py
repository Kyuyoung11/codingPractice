#모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_count = [0] * 3

    for i in range(len(answers)):
        if (person1[i % len(person1)] == answers[i]):
            answer_count[0] += 1
        if (person2[i % len(person2)] == answers[i]):
            answer_count[1] += 1
        if (person3[i % len(person3)] == answers[i]):
            answer_count[2] += 1
    max_num = max(answer_count)
    for i in range(len(answer_count)):
        if (max_num == answer_count[i]):
            answer.append(i + 1)

    return answer