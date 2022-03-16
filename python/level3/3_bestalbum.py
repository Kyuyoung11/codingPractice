#베스트앨범
#https://programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres, plays):
    answer = []
    dict = {}
    for i in range(len(genres)):
        if (genres[i] in dict.keys()):
            dict[genres[i]].append(plays[i])
        else:
            dict[genres[i]] = [plays[i]]
    # print(dict)

    dict = sorted(dict.items(), key=lambda x: sum(x[1]), reverse=True)
    # print(dict)
    for i in dict:
        temp = sorted(i[1], reverse=True)
        num = 0
        for j in temp:
            index = plays.index(j)
            answer.append(index)
            plays[index] = 0
            num += 1
            if (num > 1): break
    return answer