"""
[1] 문제 분석





[2] 설계 - 완전 탐색
 1. CCTV의 조합 구하기 (4x2x4x4) = 128
 2. 감시범위 구하기 = 8x8 + a (중복 허용)

 backtracking이 가능하나, 하지 않고 진행해도 무방하므로
 구현하고 검사할 것

"""

def go_simulate(CCTV_lst):
    visit = [arr[i][:] for i in range(N)]

    for i, CCTV_info in enumerate(CCTV_lst):
        # CCTV 방향 lst, CCTV 번호, x위치, y위치
        CCTV_dir = CCTV[CCTV_info[1]][CCTV_info[0]]

        x = CCTV_info[2]
        y = CCTV_info[3]

        for d in CCTV_dir:
            nx = x
            ny = y
            while True:
                nx += dx[d]
                ny += dy[d]
                if nx < 0 or ny < 0 or nx >= N or ny >= M: break
                if visit[nx][ny] == 6: break
                visit[nx][ny] = -1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                cnt += 1

    return cnt


def choice_CCTV(step=0, lst=[]):
    global min_
    if step >= CCTV_cnt:
        res = go_simulate(lst)
        min_ = min(res, min_)
        return

    for i in range(len(CCTV[CCTV_loc[step][0]])):
        lst.append(([i] + CCTV_loc[step]))
        choice_CCTV(step+1, lst)
        lst.pop()

# 1 ~ 5번 CCTV 위치 저장
CCTV = [[],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]
        ]

CCTV_loc = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
min_ = 64
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] < 1 or 5 < arr[i][j]: continue
        CCTV_loc.append([arr[i][j], i, j])

# CCTV 방향 정하기
CCTV_cnt = len(CCTV_loc)
choice_CCTV()

print(min_)