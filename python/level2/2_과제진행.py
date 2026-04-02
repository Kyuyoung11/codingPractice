def calc_time(start, playtime):
    time = start.split(':')
    hh, mm = int(time[0]), int(time[1])

    return hh*60 + mm + int(playtime)

def convert_time(time):
    return str(time//60) + ":" + str(time%60)

def solution(plans):
    answer = []

    # 과제 시간 기준 오름차순 정렬
    plans.sort(key=lambda x:x[1])
    # print(plans)

    plan_stack = [plans.pop(0)]
    # print(plan_stack, plans)


    while(plan_stack and plans):
        # print('b', plan_stack, '//' ,plans)
        # 1. 일정 정보
        # 현재 일정
        cur_plan = plan_stack.pop()
        cur_finish = calc_time(cur_plan[1], cur_plan[2])

        # 다음 일정
        next_plan = plans[0]
        next_start = calc_time(next_plan[1], 0)
        # print(next_plan, cur_finish, next_start)


        # 2-1. 현재 일정 끝나는 시간이 더 늦은 경우
        if(cur_finish > next_start):
            # 일정 중단
            plan_stack.append([cur_plan[0], next_plan[1], cur_finish-next_start])

            # 새 일정 넣음
            plan_stack.append(plans.pop(0))

        else: # 2-2. 현재 일정이 먼저/같이 끝나는 경우
            # 일정 마무리
            answer.append(cur_plan[0])

            # 일정 조정
            if(next_start - cur_finish == 0 or not plan_stack): # 다음 일정을 넣어야하는 경우
                plan_stack.append(plans.pop(0))
            elif(plan_stack): # 안 넣는 경우에는 현재 시간 조정 필요
                plan_stack[-1][1] = convert_time(cur_finish)

                # print('a', plan_stack, '//' ,plans)


    while(plan_stack):
        answer.append(plan_stack.pop()[0])


    return answer