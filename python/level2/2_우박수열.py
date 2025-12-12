def get_CollatzNum(k):

    # print("get_CollatzNum", k)

    #1이 되면 중단
    if(k==1):
        return k

    #짝수
    if(k%2==0):
        return k//2

    #홀수
    return k*3+1

def guess_Collatz(k):

    # print("guess_Collatz(k)", k)

    cnt=0
    pointList=[[cnt, k]]
    rainNum = k

    while(rainNum>1):
        rainNum = get_CollatzNum(rainNum)
        cnt+=1
        pointList.append([cnt, rainNum])

    return pointList

def cal_range(pointList, rng):

    # print("cal_range", pointList, rng)

    a = rng[0]
    b = pointList[-1][0] + rng[1]

    if(a > b):
        return -1.0


    area = 0
    while(a<b):
        # 1. 좌표
        y1 = pointList[a][1]
        y2 = pointList[a+1][1]

        # 2. 사다리꼴 넓이 - 윗변(a) + 아랫변(b) × 높이(h) ÷ 2
        area+=(y1 + y2) / 2
        a+=1

    return area

def solution(k, ranges):
    answer = []
    pointList = guess_Collatz(k)

    for rng in ranges:
        answer.append(cal_range(pointList, rng))

    return answer