# @ 문제 분석
# 1. Index 범위 바깥을 다루는 문제니, Out of Bounds 처리를 중심으로 잘 두어야겠다
# 2. Q의 범위가 200,000이므로, O(QlogQ) 미만의 시간복잡도를 가지도록 코드를 설계해야겠다
# 3. -만 붙여주는 작업을 진행하므로, Ai와 관련된 모든 값에 대해 -만 붙여주면 되겠다
# 4. 해당 방식을 고려했을 때, Q에 대해 O(1)로 짤 수 있을 것이다

# @ 설계
# 1. 문제에서 곱을 저장하는 array 구현
# 1-1. [1]*N array 생성
# 1-2. 곱을 저장 (ex. A1 이라면, arr[1] & arr[2] & arr[3] & arr[4] 에 곱을 저장
# 꼭 out of bounds 신경 쓸 것
# 1-3. query마다 들어오는 index에 대해 -를 붙인 다음,
# 기존에 구한 누적합에 x2하여 계산 (기존 값을 제거해야 하므로)

# @ 구현
# index를 초과하면 out of bounds가 나므로, -를 활용하여 index 계산

# @ 검증
# 1. N이 작을 때 -> 4부터이므로, 알고리즘 상 오류는 나지 않음
# 2. Ai의 값이 클 때 -> 최댓값은 10,000이므로, 큰 문제 없음
# 3. Ai의 값이 0일 때 -> 알고리즘 상 큰 문제 없음
# 4. N & Q가 최대일 때 시간복잡도
# --> 구현 1 : arr 처리 - O(N)
# --> 구현 2 : 합 계산 - O(N)
# --> 구현 3 : list index 처리는 O(1)이므로, O(Q)

N, Q = map(int, input().split())

arr = [1]*N

temp_lst = list(map(int, input().split()))
query = list(map(int, input().split()))

# 1. index에 따른 array 저장
# out of bounds가 나지 않게 하기 위해, -로 index를 처리
for i in range(N):
    arr[i-3] *= temp_lst[i]
    arr[i-2] *= temp_lst[i]
    arr[i-1] *= temp_lst[i]
    arr[i] *= temp_lst[i]

# 2. 누적합 저장
S = sum(arr)

# 3. i번째 index와 관련있는 값을 -로 바꾼 후, S에 index와 관련있는 값만 더하여 계산
for q in query:
    arr[q-4] = -arr[q-4]
    arr[q-3] = -arr[q-3]
    arr[q-2] = -arr[q-2]
    arr[q-1] = -arr[q-1]

    S += 2*(arr[q-4] + arr[q-3] + arr[q-2] + arr[q-1])
    print(S)