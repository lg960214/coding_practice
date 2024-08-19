# @ 문제 분석
#
# 1. 문제 조건
# - 앞, 뒤에서만 제거
# - 2 종류 이하로만
# - 과일의 개수는 N (200,000)
# - 과일의 종류는 9가지
#
# A. Deque 활용
#  - 앞, 뒤에서만 제거 --> 재귀로 짜야 하는데, 2^200,000이므로 불합격
#
# B. Two Pointer 활용
#  - 연속된 부분집합이니 Two pointer 활용 가능

#  1. left를 옮길 때
#    - 종류가 3종류 이상일 때
#    -
#  2. right를 옮길 때
#    - 종류가 2종류 이하일 때
#
#  + 종류가 9종류 미만이니, DAT로 해결


N = int(input())

arr = list(map(int, input().split()))
DAT = [0]*10
DAT[arr[0]] += 1

left = 0
right = 0

kind = 1
max_ = 1

while left < N and right < N:

    # if sum > thr:
    #     left += 1
    #     sum -= left
    # else:
    #     right += 1
    #     sum += right

    if kind > 2:
        DAT[arr[left]] -= 1
        if DAT[arr[left]] == 0:
            kind -= 1
        left += 1
    else:
        if right < N-1:
            right += 1
            if DAT[arr[right]] == 0:
                kind += 1
            DAT[arr[right]] += 1

            if kind <= 2:
                max_ = max(max_, right-left+1)
        else:
            break

print(max_)