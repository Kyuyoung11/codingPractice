#[카카오 인턴] 키패드 누르기
#https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    now_left = '*'
    now_right = '#'
    # keypads = [["1","2","3"],
    #          ["4","5","6"],
    #          ["7","8","9"],
    #          ["*","0","#"]]
    keypads = {
        "1": [0, 0],
        "2": [0, 1],
        "3": [0, 2],
        "4": [1, 0],
        "5": [1, 1],
        "6": [1, 2],
        "7": [2, 0],
        "8": [2, 1],
        "9": [2, 2],
        "*": [3, 0],
        "0": [3, 1],
        "#": [3, 2]
    }

    for i in numbers:
        if (i == 1 or i == 4 or i == 7):
            answer += 'L'
            now_left = str(i)
        elif (i == 3 or i == 6 or i == 9):
            answer += 'R'
            now_right = str(i)
        else:
            # print(now_left, now_right)
            dis_left = (abs(keypads[now_left][0] - keypads[str(i)][0]) +
                        abs(keypads[now_left][1] - keypads[str(i)][1]))

            dis_right = (abs(keypads[now_right][0] - keypads[str(i)][0]) +
                         abs(keypads[now_right][1] - keypads[str(i)][1]))
            if (dis_left < dis_right):
                answer += 'L'
                now_left = str(i)
            elif (dis_left > dis_right):
                answer += 'R'
                now_right = str(i)
            else:
                if (hand == "right"):
                    answer += 'R'
                    now_right = str(i)
                else:
                    answer += 'L'
                    now_left = str(i)

    return answer