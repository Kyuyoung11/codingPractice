from collections import deque
import heapq

def solution(N, number):
    answer = 0

    answer_list = []
    num_list = []
    for i in range(1,9):
        num_list.append([int(str(N)*i), i])

    num_q = deque(num_list)

    while num_q:
        cur_num = num_q.popleft()

        if(cur_num[0] == number):
            heapq.heappush(answer_list, cur_num[1])

        for i in range(len(num_list)):
            if(cur_num[1]+num_list[i][1] <= 8):
                num_q.append([cur_num[0]+num_list[i][0], cur_num[1]+num_list[i][1]])
                num_q.append([cur_num[0]-num_list[i][0], cur_num[1]+num_list[i][1]])
                num_q.append([num_list[i][0]-cur_num[0], cur_num[1]+num_list[i][1]])
                num_q.append([cur_num[0]*num_list[i][0], cur_num[1]+num_list[i][1]])
                if(num_list[i][0] != 0):
                    num_q.append([cur_num[0]//num_list[i][0], cur_num[1]+num_list[i][1]])
                if(cur_num[0] != 0):
                    num_q.append([num_list[i][0]//cur_num[0], cur_num[1]+num_list[i][1]])


    if(len(answer_list)==0):
        return -1

    return answer_list[0]