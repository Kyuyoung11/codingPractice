#다리를 지나는 트럭
#https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_list = [] #bridge 어디에 있는지 인덱스 값으로 저장
    in_bridge = [] #bridge에 있는 truck_weight 저장
    b_sum = 0



    while (len(truck_weights) > 0):
        answer += 1

        #bridge_list 모든 값 +1 해줌
        for i in range(len(bridge_list)):
            bridge_list[i] += 1

        if (len(bridge_list) > 0):
            #가장 앞에 있는 트럭이 bridge를 지났으면 배열에서 삭제
            if (bridge_list[0] >= bridge_length):
                b_sum -= in_bridge[0]
                del in_bridge[0]
                del bridge_list[0]

        #현재 다리 위에 있는 트럭 무게 합보다 다음 트럭 무게가 적으면 다리에 올림
        if (b_sum + truck_weights[0] <= weight):
            bridge_list.append(0)
            in_bridge.append(truck_weights[0])
            b_sum += truck_weights[0]
            del truck_weights[0]

        # print(answer, bridge_list, in_bridge)

    return answer + bridge_length