#크레인 인형뽑기 게임
#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(0, len(board)):
            if (board[j][i - 1] != 0):
                if (len(basket) == 0):
                    basket.append(board[j][i - 1])
                else:
                    top = basket[-1]
                    if (top == board[j][i - 1]):
                        basket.pop()
                        answer += 2
                    else:
                        basket.append(board[j][i - 1])
                board[j][i - 1] = 0
                break

    return answer