#K번째수
#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []

    for a in range(len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        new_list = sorted(array[i - 1:j])
        print(new_list)

        answer.append(new_list[k - 1])

    return answer