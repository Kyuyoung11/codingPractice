#행렬 테두리 회전하기
#https://programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    answer = []
    array = []
    for i in range(rows):
        list = []
        for j in range(columns):
            list.append(columns * i + j + 1)
        array.append(list)
    # print(array)

    for i in range(len(queries)):
        stack = []
        x_min = queries[i][0] - 1
        x_max = queries[i][2] - 1
        y_min = queries[i][1] - 1
        y_max = queries[i][3] - 1
        min = array[x_min][y_min]
        for j in range(y_min, y_max + 1):
            temp = array[x_min][j]
            if (len(stack) == 0):
                stack.append(temp)
                continue
            if (temp < min): min = temp
            num = stack.pop()
            array[x_min][j] = num
            stack.append(temp)
        for j in range(x_min, x_max + 1):
            if (j == x_min): continue
            temp = array[j][y_max]
            if (len(stack) == 0):
                stack.append(temp)
                continue
            if (temp < min): min = temp
            num = stack.pop()
            array[j][y_max] = num
            stack.append(temp)
        for j in range(y_max, y_min - 1, -1):
            if (j == y_max): continue
            temp = array[x_max][j]
            if (len(stack) == 0):
                stack.append(temp)
                continue
            if (temp < min): min = temp
            num = stack.pop()
            array[x_max][j] = num
            stack.append(temp)
        for j in range(x_max, x_min - 1, -1):
            if (j == x_max): continue
            temp = array[j][y_min]
            if (len(stack) == 0):
                stack.append(temp)
                continue
            if (temp < min): min = temp
            num = stack.pop()
            array[j][y_min] = num
            stack.append(temp)
        # print(min, array)
        answer.append(min)

    return answer