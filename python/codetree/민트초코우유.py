from collections import deque
import heapq

N, T = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

'''
음식 문자열을 boolean 배열로 변환
[T, C, M]
'''
def convert_food_string_to_flag(str):
    food = [False, False, False]

    for s in str:
        if s == 'T':
            food[0] = True
        elif s == 'C':
            food[1] = True
        elif s == 'M':
            food[2] = True

    # print(food)

    return food


'''
아침 시간 : 모든 학생 신앙심 1 얻음 
'''
def do_breakfirst(believe_cnt):
    for i in range(N):
        for j in range(N):
            believe_cnt[i][j] += 1

    return believe_cnt


'''
점심 시간 : 대표자 선정
'''
def do_lunch(student, believe_cnt):
    visited = [[False for _ in range(N)] for _ in range(N)]

    # 대표자 순서 맞춰서 구성하기 위해 heapq 사용
    # 1. 음식 조합 개수 (최소)
    # 2. 신앙심 높은 순
    # 3. 행 번호 (최소)
    # 4. 열 번호 (최소)
    presidents = []

    q = deque()
    q.append([0, 0])
    while (q):
        cur_point = q.popleft()
        init_x, init_y = cur_point[0], cur_point[1]
        president, believe_cnt, visited = elect_president(init_x, init_y, believe_cnt, student, visited)
        if (len(president) > 0):
            heapq.heappush(presidents, president)

        for i in range(0, N):
            flag = False
            for j in range(0, N):
                if not visited[i][j]:
                    q.append([i, j])
                    flag = True
                    break
            if flag: break

    heapq.heapify(presidents)

    return presidents, believe_cnt


'''
대표자 선출
1. 그룹 생성
2. 대표자 선정
3. 신앙심 조정
'''
def elect_president(init_x, init_y, believe_cnt, student, visited):
    q = deque()
    q.append([[init_x, init_y], student[init_x][init_y]])  # 위치, 음식
    group = [[believe_cnt[init_x][init_y]*-1, init_x, init_y]]  # 신앙심, 행, 열

    # 1. 그룹 생성
    while (q):
        cur_st = q.popleft()
        cur_x, cur_y, cur_food = cur_st[0][0], cur_st[0][1], cur_st[1]

        visited[cur_x][cur_y] = True

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if not visited[new_x][new_y] and cur_food == student[new_x][new_y]:
                    # print(new_x, new_y)
                    q.append([[new_x, new_y], student[new_x][new_y]])
                    heapq.heappush(group, [believe_cnt[new_x][new_y] * -1, new_x, new_y])
                    visited[new_x][new_y] = True

    # 2. 대표자 선정
    group_1 = heapq.heappop(group)

    max_x, max_y = group_1[1], group_1[2]
    believe_cnt[max_x][max_y] += len(group)
    president = (student[max_x][max_y].count(True), -1 * believe_cnt[max_x][max_y], max_x, max_y)

    # 3. 신앙심 조정
    while (group):
        cur_st = heapq.heappop(group)
        believe_cnt[cur_st[1]][cur_st[2]] -= 1

    return president, believe_cnt, visited


'''
저녁시간
1. 전파
저녁시간부터하면됨 여기까지 1시간걸림
'''
def do_dinner(presidents, student, believe_cnt):
    visited = [[False for _ in range(N)] for _ in range(N)]
    while presidents:
        president = heapq.heappop(presidents)
        # print(president, student[president[2]][president[3]])
        # 전파
        student, believe_cnt, visited = share_believe(president, student, believe_cnt, visited)
    return student, believe_cnt


'''
전파
'''
def share_believe(president, student, believe_cnt, visited):
    # print(president)
    # 방향 정하기
    direct = abs(president[1]) % 4
    init_x, init_y = president[2], president[3]

    if visited[init_x][init_y]:  # 전파 불가능 상태
        # print("전파안됨", init_x, init_y)
        return student, believe_cnt, visited

    believe_cnt[init_x][init_y] = 1

    q = deque()
    q.append([init_x, init_y, abs(president[1]) - 1])
    while (q):
        cur_x, cur_y, cur_cnt = map(int, q.popleft())

        new_x, new_y = cur_x + dx[direct], cur_y + dy[direct]
        if 0 <= new_x < N and 0 <= new_y < N:
            if student[cur_x][cur_y] != student[new_x][new_y]:
                # 강한 전파
                if cur_cnt > believe_cnt[new_x][new_y]:
                    visited[new_x][new_y] = True
                    student[new_x][new_y] = student[cur_x][cur_y][:]  # 동일 음식 신봉
                    cur_cnt -= (believe_cnt[new_x][new_y] + 1)  # 간절함
                    believe_cnt[new_x][new_y] += 1
                    if (cur_cnt > 0):
                        q.append([new_x, new_y, cur_cnt])
                    # print("강한 전파", new_x, new_y, cur_cnt, believe_cnt[new_x][new_y])
                # 약한 전파
                else:
                    for i in range(3):
                        if (student[cur_x][cur_y][i] == True):
                            student[new_x][new_y][i] = True
                    visited[new_x][new_y] = True
                    believe_cnt[new_x][new_y] += cur_cnt
                    # print("약한", new_x, new_y, cur_cnt, believe_cnt[new_x][new_y])
            else:
                # print("같", new_x, new_y, cur_cnt)
                q.append([new_x, new_y, cur_cnt])

    return student, believe_cnt, visited


def print_believe(student, believe_cnt):
    order = [[True, True, True], [True, True, False], [True, False, True], [False, True, True], [False, False, True],
             [False, True, False], [True, False, False]]

    for com in order:
        believe_sum = 0
        for i in range(N):
            for j in range(N):
                if student[i][j] == com:
                    believe_sum += believe_cnt[i][j]

        print(believe_sum, end=' ')


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
for _ in range(T):
    # 아침 시간
    believe_cnt = do_breakfirst(believe_cnt)

    # 점심 시간
    presidents, believe_cnt = do_lunch(student, believe_cnt)
    # print(presidents)

    # 저녁 시간
    student, believe_cnt = do_dinner(presidents, student, believe_cnt)

    # 신앙심 출력
    print_believe(student, believe_cnt)
    print()
