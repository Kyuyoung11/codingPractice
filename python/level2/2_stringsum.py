#문자열 압축
#https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = 0
    length = []
    length.append(len(s))
    word_len = int(len(s) / 2)
    # word_len = 3

    while (word_len > 0):
        p = 0
        pp = 0
        i = 0
        total = len(s)
        while (len(s) - pp > word_len):
            # for i in range(len(s)-word_len+1):

            # print(p, pp)
            new_word = s[pp:pp + word_len]
            # print("new :", new_word)

            a = pp + word_len
            b = pp + word_len * 2
            count = 0
            while (new_word == s[a:b]):
                new_word = s[a:b]
                a += word_len
                b += word_len
                count += 1

            if (count > 0):
                p += (word_len * (count + 1))
                total -= (word_len) * count - 1
                count += 1
                while (int(count / 10) > 0):
                    total += 1
                    count /= 10
            else:
                i += word_len
            pp = i + p
        length.append(total)
        word_len -= 1
    print(length)
    return min(length)