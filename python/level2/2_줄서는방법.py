def fact(num):
    n = 1
    for i in range (num):
        n *= i+1
    return n

def solution(n, k):
    nList = [i for i in range(1,n+1)]
    answer = []

    while(len(nList)>0):
        # print(k, n)
        if(k==1):
            answer.append(nList[0])
            nList.pop(0)
            continue
        factNum = fact(n-1)
        index = (k-1)//factNum
        # print(k, n, factNum, index)
        answer.append(nList[index])
        nList.pop(index)
        k%= factNum
        n-=1

    return answer