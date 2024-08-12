# A. 퀵 정렬
import sys

input = sys.stdin.readline

def quick_sort(lst, st_idx, en_idx):
    if (st_idx >= en_idx):
        return

    # 1. 첫 번째 값을 기준(pivot) 값으로 설정
    pivot = lst[st_idx]
    pivot_idx = st_idx

    # 2. 기준 값보다 작은 값은 왼쪽, 큰 값은 오른쪽에 배치
    left = st_idx + 1
    right = en_idx
    while left <= right:
        # 2-1. 좌측으로부터 큰 데이터 선택
        while left <= en_idx and lst[left] <= pivot: # 같은거 포함해야 함 --> 무한 루프
            left += 1

        # 2-2. 우측으로부터 작은 데이터 선택
        while st_idx < right and pivot <= lst[right]: # 같은거 포함해야 함 --> 무한 루프
            right -= 1

        # 2-3. 데이터 교환
        if left < right: # 정상적인 상태라면
            lst[left], lst[right] = lst[right], lst[left] # 교환
        else:
            # 작은 것과 pivot 교환 (오름차순이므로)
            lst[right], lst[pivot_idx] = lst[pivot_idx], lst[right]

    # 3. 기준(pivot) 값 위치의 왼쪽 부분과 오른쪽 부분을 위의 과정 반복
    quick_sort(lst, st_idx, right-1) # pivot과 교환한 idx는 right이므로
    quick_sort(lst, right+1, en_idx) # right 기준으로 교환

    return

N = int(input())
arr = [int(input()) for _ in range(N)]

quick_sort(arr, 0, len(arr)-1)

for i in arr:
    print(i)