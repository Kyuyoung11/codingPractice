from collections import deque

N, T = map(int, input().split())
dx, dy = [-1,1,0,0], [0,0,-1,1]

'''
음식 문자열을 boolean 배열로 변환
[T, C, M]
'''
def convert_food_string_to_flag(str):
    food = [False, False, False]

    for s in str:
        if s == 'T': food[0] = True
        elif s == 'C': food[1] = True
        elif s == 'M': food[2] = True

    # print(food)

    return food

'''
대표자 선출
1. 대표자 선정
2. 신앙심 조정
'''
def elect_president(init_x, init_y, believe_cnt, student, visited):

    q = deque()
    q.append([[init_x,init_y], student[init_x][init_y]])# 위치, 음식
    max_believe = [[init_x, init_y], believe_cnt[init_x][init_y]]
    group_cnt = 1

    while(q):
        cur_st = q.popleft()
        cur_x, cur_y, cur_food = cur_st[0][0], cur_st[0][1], cur_st[1]

        visited[cur_x][cur_y] = True

        for i in range(len(dx)):
            new_x, new_y = cur_x+dx[i], cur_y+dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if not visited[new_x][new_y] and cur_food == student[new_x][new_y]:
                    # print(new_x, new_y)
                    q.append([[new_x, new_y], student[new_x][new_y]])
                    group_cnt += 1

                    visited[new_x][new_y] = True
                    if(max_believe[1] < believe_cnt[new_x][new_y]):
                        believe_cnt[max_believe[0][0]][max_believe[0][1]] -=1
                        max_believe = [[new_x, new_y], believe_cnt[new_x][new_y]]
                    else:
                        believe_cnt[new_x][new_y] -=1

    president = []

    if(group_cnt > 1):
        believe_cnt[max_believe[0][0]][max_believe[0][1]] += (group_cnt-1)
        president = [max_believe[0], student[init_x][init_y]]

    return president, believe_cnt, visited

'''
아침 시간 : 모든 학생 신앙심 1 얻음 
'''
def do_breakfirst(believe_cnt):
    for i in range(N):
        for j in range(N):
            believe_cnt[i][j]+=1

    return believe_cnt

'''
점심 시간 : 대표자 선정
'''
def do_lunch(student, believe_cnt):
    visited = [[False for _ in range(N)] for _ in range(N)]

    presidents = []

    q = deque()
    q.append([0,0])
    while(q):
        cur_point = q.popleft()
        init_x, init_y = cur_point[0], cur_point[1]
        president, believe_cnt, visited = elect_president(init_x, init_y, believe_cnt, student, visited)
        if (len(president) > 0):
            presidents.append(president)

        for i in range(cur_point[0], N):
            for j in range(cur_point[1], N):
                if not visited[i][j]:
                    q.append([i,j])


    print(presidents)

    return presidents, believe_cnt


'''
저녁시간
1. 대표자 순서 정하기
2. 전파
저녁시간부터하면됨 여기까지 1시간걸림
'''
def do_dinner():




# 학생 음식 초기값 설정
student = [[[False, False, False] for _ in range(N)] for _ in range(N)]
for i in range(N):
    class_line = input()
    for j in range(len(class_line)):
        student[i][j] = convert_food_string_to_flag(class_line[j])

# 신앙심
believe_cnt = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    class_line = input().split()
    for j in range(len(class_line)):
        believe_cnt[i][j] = int(class_line[j])


# 진행
# for _ in range(T):
#아침 시간
believe_cnt = do_breakfirst(believe_cnt)

# 점심 시간
presidents, believe_cnt = do_lunch(student, believe_cnt)

#저녁 시간


