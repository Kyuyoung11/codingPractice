#오픈채팅방
#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    do = []  # 2차원 배열
    # Enter, Leave, Change
    # id
    people = {}  # id, name

    for i in record:
        msg = i.split(" ")
        if (msg[0] == "Enter"):
            do.append([msg[0], msg[1]])
            people[msg[1]] = msg[2]
        elif (msg[0] == "Leave"):
            do.append([msg[0], msg[1]])
        else:
            people[msg[1]] = msg[2]
    for i in range(0, len(do)):
        if (do[i][0] == "Enter"):
            answer.append(people[do[i][1]] + "님이 들어왔습니다.")
        elif (do[i][0] == "Leave"):
            answer.append(people[do[i][1]] + "님이 나갔습니다.")
    return answer