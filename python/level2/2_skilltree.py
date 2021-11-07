#스킬트리
def solution(skill, skill_trees):
    answer = 0
    for i in range(0, len(skill_trees)):
        skill_index = []
        for j in range(0, len(skill)):
            if (skill[j] in skill_trees[i]):
                skill_index.append(skill_trees[i].index(skill[j]))
            else:
                skill_index.append(50)
        is_skill = 1
        print(skill_index)

        if (len(skill_index) > 0):
            min = skill_index[0]
            for i in range(1, len(skill_index)):
                if (min > skill_index[i]):
                    is_skill = 0
                    break

        if (is_skill == 1):
            answer += 1
        print("---")

    return answer