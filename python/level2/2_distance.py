#거리두기 확인하기

def solution(places):
    answer = []
    for i in range(len(places)):
        peo = []
        par = []
        emp = []
        for a in range(len(places[i])):
            for b in range(len(places[i][a])):
                if (places[i][a][b] == 'P'):
                    peo.append([a, b])
        print(peo)
        if len(peo) < 2:
            print("1")
            answer.append(1)
            continue

        break_flag = False
        for a in range(len(peo) - 1):
            for b in range(a + 1, len(peo)):
                dis = abs(peo[b][0] - peo[a][0]) + abs(peo[b][1] - peo[a][1])
                if dis == 2:

                    min_row = peo[a][1]
                    double = False
                    if (peo[a][1] > peo[b][1]):
                        double = True
                        min_row = peo[b][1]

                    if (abs(peo[b][0] - peo[a][0]) > 0):
                        # print(places[i][peo[a][0]+1][peo[a][1]])
                        if (places[i][peo[a][0] + 1][peo[a][1]] == 'O'):
                            print("2")
                            answer.append(0)
                            break_flag = True
                            break

                    if (abs(peo[b][1] - peo[a][1]) > 0):
                        # print("hi", places[i][peo[a][0]][min_row+1])
                        if (places[i][peo[a][0]][min_row + 1] == 'O'):
                            print("3")
                            answer.append(0)
                            break_flag = True
                            break
                        if (double == True):
                            if (places[i][peo[a][0]][peo[a][1] - 1] == 'O'):
                                print("3.5")
                                answer.append(0)
                                break_flag = True
                                break

                elif dis == 1:
                    print("4")
                    break_flag = True
                    answer.append(0)
                    break

            if break_flag == True:
                break

        if (break_flag == False):
            print("5")
            answer.append(1)
        print("----------------------")

    return answer