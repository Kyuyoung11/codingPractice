#성적이 낮은 순서로 학생 출력하기



def setting(student):
    return student[1]

def sort_students(students) :
    return sorted(students, key=setting)

if __name__ == '__main__':

    # 1. 첫번째 줄 = 학생 수
    count = int(input())


    # 2. 학생이름 학생점수
    students = []
    for i in range(count):
        name, score = input().split(" ")
        students.append([name, int(score)])


    for student in sort_students(students):
        print(student[0], end= ' ')


