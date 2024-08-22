# @ 문제 분석
# 청소하는 영역의 개수를 구하는 문제
#
# [1] 문제 조건
#  - 칸은 벽(1) 또는 빈 칸(0)
#  - 청소기는 동,서,남,북 중 한 곳을 바라봄
#  - 좌표는 0,0 ~ N-1, M-1
#  - 처음 빈 칸은 전부 청소되지 않은 상태
#    --> visit = True로 바꾼 후 개수를 세면 된다
#  - 로봇 청소기가 있는 칸은 항상 빈 칸
#  - 이후에는 구현 방향이 주어짐
#
# [2] 시간복잡도
#  - N, M <= 50 이라, 중복방문만 최소화해도 터질 일이 없다
#

# @ 설계
# 구현 방향이 명확하므로, 주어진 조건에 충실해서 구현한다.

# @ 검증
# 디버거로 로봇 움직이는 방식과 내 논리가 일치하는 지 학인 --> 완료

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

sx, sy, sd = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]


x = sx
y = sy
d = sd

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    visit[x][y] = True

    # 2. 청소되지 않은 빈 칸 탐색
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if arr[nx][ny] == 1: continue
        if visit[nx][ny] == True: continue
        cnt += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if cnt == 0:
        td = (d + 2) % 4
        nx = x + dx[td]
        ny = y + dy[td]
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        if nx < 0 or ny < 0 or nx >= N or ny >= M: break
        if arr[nx][ny] == 1: break

        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        x = nx
        y = ny
    else: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        d = (d + 3) % 4 # 반 시계 방향으로 90도 회전

        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if arr[nx][ny] == 1: continue
        if visit[nx][ny] == True: continue
        x = nx
        y = ny
        # 1번으로 돌아간다.

ans = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == True:
            ans += 1

print(ans)