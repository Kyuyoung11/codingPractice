#최대공약수와 최소공배수
#https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    a = min(n, m)
    b = max(n, m)

    for i in range(a, 0, -1):
        if (n % i == 0 and m % i == 0):
            answer.append(i)
            break

    num = b
    for i in range(b, a * b):
        if (num % a == 0 and num % b == 0):
            answer.append(num)
            break
        num += b

    return answer