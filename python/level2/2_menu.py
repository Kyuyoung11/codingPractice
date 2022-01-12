#메뉴 리뉴얼
#https://programmers.co.kr/learn/courses/30/lessons/72411
mport itertools


def solution(orders, course):
    answer = []
    orders = sorted(orders, key=len)
    total_list = sorted(list(set("".join(orders))))

    for i in course:
        com_list = list(itertools.combinations(total_list, i))
        element = []
        max_cnt = 0
        index = 0
        temp_list = list(filter(lambda x: len(x) >= i, orders))
        # print(temp_list)
        for j in com_list:
            in_cnt = 0
            for a in temp_list:
                for b in j:
                    if (b not in a): break
                else:
                    in_cnt += 1
            if (in_cnt > 1):
                if (max_cnt < in_cnt):
                    max_cnt = in_cnt
                    element = ["".join(j)]
                elif (max_cnt == in_cnt):
                    element.append("".join(j))
        # print(element)

        for j in element:
            answer.append(j)

    return sorted(answer)