#숫자 문자열과 영단어
#https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = ''
    num_text = ''
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in s:
        # print(i)
        if (i.isdigit() == True):
            answer += i
        else:
            num_text += i
            if ((num_text in num) == True):
                answer += str(num.index(num_text))
                num_text = ''

    answer = int(answer)

    return answer