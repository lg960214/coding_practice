# @ 문제 분석

# [1] 문제 조건
#  - 마법사 상어 마법 : 파이어볼, 토네이도, 파이어스톰, 물복사버그, 비바라기
#  - 1 ~ N 까지의 array 범위 / 서로 이어짐
#  - 8방 탐색
#  - 비구름은 4곳에 위치
#
# [2] 시간복잡도
# NxM = 5000, M = 100
# 문제 조건과 같이 고려했을 때, 시간초과 날 일은 없을 듯 하다

# 시간이 오래 걸린 원인
# 예제 입력 1의 답을,  예제 출력 2인 줄 알고 계속 고민

from collections import deque


def move_idx(x, y, d, s):
    nx = x + dx[d]*s
    ny = y + dy[d]*s
    return nx % N, ny % N


dx = [0, -1, -1, -1, 0, 1, 1, 1]  # 8방 탐색 순서
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cross_idx = [1, 3, 5, 7]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
next_q = deque()

q.append((N - 1, 0))  # 초기 조건
q.append((N - 1, 1))  # 초기 조건
q.append((N - 2, 0))  # 초기 조건
q.append((N - 2, 1))  # 초기 조건

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1  # 방향 인덱스 맞추기
    cloud_set = set()

    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    while q:
        target = q.popleft()
        nx, ny = move_idx(target[0], target[1], d, s)
        # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        arr[nx][ny] += 1
        next_q.append((nx, ny))
        cloud_set.add((nx, ny))

    # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
    while next_q:
        target = next_q.popleft()
        # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼
        cnt = 0
        for idx in cross_idx:
            nx = target[0] + dx[idx]
            ny = target[1] + dy[idx]
            # 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if arr[nx][ny] > 0:
                cnt += 1
        # (r, c)에 있는 바구니의 물이 양이 증가한다.
        arr[target[0]][target[1]] += cnt

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    for i in range(N):
        for j in range(N):
            # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
            if arr[i][j] < 2: continue
            if (i, j) in cloud_set: continue
            arr[i][j] -= 2
            q.append((i, j))

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
water = 0

for i in range(N):
    for j in range(N):
        water += arr[i][j]

print(water)
