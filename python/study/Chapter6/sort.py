###############
# Chapter6. 정렬
###############




## 1. 선택 정렬
##  - 느림 O(n^2)
##  - 가장 작은 데이터를 앞으로 보내는 방법
##  - 가장 작은 데이터를 앞에서부터 swap

### swap 소스
array = [3, 5]
array[0], array[1] = array[1], array[0]


## 2. 삽입 정렬
##  - 느림 O(n^2)
##  - index 해당하는 데이터가 검증된 배열에서 오름차순으로 정렬되도록 삽입하는 방식
##  - index 해당하는 데이터를 검증된 배열 뒤에서부터 순회하며 맞는 위치까지 swap


## 3. 퀵 정렬
##  - 많이 사용함
##  - 임의의 기준을 '피벗'으로 사용하여, 작은 수 / 큰 수를 분할한다.
##  - O(NlogN)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    pivot = array[0] # 피벗을 첫번째 원소로 잡음
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)




# 파이썬의 정렬 라이브러리
## sorted()
##  - 기본 정렬 라이브러리, 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만듦

## .sort()
##  - 리스트 변수 하나일 때 사용 가능

