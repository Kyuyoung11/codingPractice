import copy


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_list = [0] * bridge_length
    b_sum = 0
    while (len(truck_weights) > 0):
        answer += 1
        if (bridge_list[-1] != 0): b_sum -= bridge_list[-1]
        bridge_list[1:] = bridge_list[0:len(bridge_list) - 1]
        bridge_list[0] = 0

        if (b_sum + truck_weights[0] <= weight):
            bridge_list[0] = truck_weights[0]
            b_sum += truck_weights[0]
            del truck_weights[0]
        # print(answer, bridge_list)

    #     time_list = []
    #     temp = copy.deepcopy(truck_weights)
    #     for i in truck_weights:
    #         if (b_sum + i <= weight):
    #             b_sum+=i
    #             answer+=1
    #             time_list.append(answer)
    #         else:
    #             b_sum+=i
    #             answer+=bridge_length
    #             time_list.append(answer)

    #         print(i, b_sum, time_list)
    #         for j in range(len(time_list)):
    #             if(answer-bridge_length >= time_list[0]):
    #                 b_sum-=temp[0]
    #                 del temp[0]
    #                 del time_list[0]
    #             else:
    #                 break
    #         print(i, b_sum, time_list)

    return answer + bridge_length