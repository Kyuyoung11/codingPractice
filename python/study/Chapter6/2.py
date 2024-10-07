# 내림차순으로 정렬해보기
# 첫줄은 수열에 속해 있는 수 N
# 두번째줄부터는 자연수



def sort_number(array):
    return sorted(array, reverse=True)


if __name__ == '__main__':
    # 입력 받기

    count = int(input())


    array = []
    for i in range(count):
        array.append(int(input()))


    print(sort_number(array))