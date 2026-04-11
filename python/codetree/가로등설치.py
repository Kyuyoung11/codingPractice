# 풀이중
import heapq

Q = int(input())
N, M = 0, 0

def check_village_status(commands, num):

    lights = []  # -먼 인접 가로등 거리, 위치, 고유번호, 가까운 인접

    for i in range(M):
        index = i + 3
        right_dist = abs(commands[index - 1] - commands[index]) if i > 0 else 0
        left_dist = abs(commands[index + 1] - commands[index]) if i < M - 1 else 0

        heapq.heappush(lights, [-1 * max(right_dist, left_dist), commands[3 + i], num, min(right_dist, left_dist)])
        num+=1

    return lights, num


def modify_light_after_adding(light, new_light_location):
    light[0] = max(abs(light[1] - new_light_location), light[3]) * -1
    light[3] = min(abs(light[1] - new_light_location), light[3])

    return light


def add_light(lights):
    # print("add")
    # 인접한 가로등 사이의 거리가 가장 먼 곳
    light_left = heapq.heappop(lights)
    light_right = heapq.heappop(lights)

    new_light_location = abs(light_left[1] + light_right[1]) // 2

    heapq.heappush(lights, modify_light_after_adding(light_left, new_light_location))
    heapq.heappush(lights, modify_light_after_adding(light_right, new_light_location))

    new_light = [abs(light_right[1] - new_light_location) * -1, new_light_location, len(lights) + 1,
                 abs(light_left[1] - new_light_location)]
    heapq.heappush(lights, new_light)

    return lights


def modify_light_after_removing(other_light, remove_light, is_left):
    if remove_light[0] == other_light[0]:
        if remove_light[3] == 0:
            other_light[0] = other_light[3] * -1
            other_light[3] = 0
        else:
            other_light[0] -= remove_light[3]
    else:
        other_light[0] = max(other_light[0] * -1, other_light[3] + (remove_light[0] * -1)) * -1
        if remove_light[3] == 0:
            other_light[3] = 0
        else:
            other_light[3] = min(other_light[0] * -1, other_light[3] + (remove_light[0 if is_left else 3] * -1))

    return other_light


def remove_light(lights, light_num):
    new_lights = sorted(lights[:], key=lambda light: light[1])

    target_index = 0
    for i in range(len(new_lights)):
        if new_lights[i][2] == light_num:
            target_index = i
            break

    target_light = new_lights[target_index]
    lights.remove(target_light)

    if target_index > 0:
        target_light_left = new_lights[target_index - 1]
        lights.remove(target_light_left)
        heapq.heappush(lights, modify_light_after_removing(target_light_left, target_light, True))

    if target_index < len(new_lights) - 1:
        target_light_right = new_lights[target_index + 1]
        lights.remove(target_light_right)
        heapq.heappush(lights, modify_light_after_removing(target_light_right, target_light, False))

    heapq.heapify(lights)
    # print(lights, target_light)
    return lights


# 최소 전력 계산
def calc_min_power(lights, N):
    max_light = heapq.heappop(lights)
    max_dist = max_light[0] * -1

    heapq.heappush(lights, max_light)

    # 0~ 좌표 min
    start_to_min = min(light[1] for light in lights) * 2

    # 좌표 max ~ N
    max_to_end = (N - max(light[1] for light in lights)) * 2

    # print("calc", max_dist, start_to_min, max_to_end)
    print(max(max_dist, start_to_min, max_to_end))

    return lights


num = 1
lights = []
# 명령
for _ in range(Q):
# for _ in range(5):
    commands = list(map(int, input().split()))
    # print(commands)

    # 마을 상태 확인
    if commands[0] == 100:
        N, M = commands[1], commands[2]
        lights, num = check_village_status(commands, num)
    # 가로등 추가
    elif commands[0] == 200:
        lights = add_light(lights)
        num+=1
    # 가로등 제거
    elif commands[0] == 300:
        lights = remove_light(lights, commands[1])
    # 최소 전력 계산
    elif commands[0] == 400:
        lights = calc_min_power(lights, N)
