# 두 배열의 원소 교체



def get_min_index(array):

    index = 0
    min_value = array[0]

    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
            index = i

    return index

def get_max_index(array):

    index = 0
    max_value = array[0]

    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
            index = i

    return index


if __name__ == '__main__':
    n, k = map(int, input().split(" "))

    array_a = list(map(int, input().split(" ")))
    array_b = list(map(int, input().split(" ")))

    for i in range(k):
        min_index = get_min_index(array_a)
        max_index = get_max_index(array_b)

        print(min_index, max_index)

        array_a[min_index], array_b[max_index] = array_b[max_index], array_a[min_index]

    print(sum(array_a))

