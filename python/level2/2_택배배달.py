def solution(cap, n, deliveries, pickups):
    answer = 0
    dlvBoxCnt = 0
    pckBoxCnt = 0

    for i in range(n-1, -1, -1):
        dlvBoxCnt += deliveries[i]
        pckBoxCnt += pickups[i]

        while(dlvBoxCnt > 0 or pckBoxCnt > 0):
            dlvBoxCnt -= cap
            pckBoxCnt -= cap
            answer+=(i+1)*2
            # print(dlvBoxCnt, pckBoxCnt, answer, i)


    return answer