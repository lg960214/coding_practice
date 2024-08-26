# @ 문제 분석
#
# [1] 문제 조건
#  - 8×8인 체스판에서 탈출하는 게임
#  - 모든 칸은 빈 칸 또는 벽 중 하나
#
#  - 욱제
#    - 시작 : 캐릭터는 가장 왼쪽 아랫 칸
#    - 도착 : 가장 오른쪽 윗 칸
#    - 이동 - 1초에
#      - 인접한 한 칸
#      - 대각선 방향으로 인접한 한 칸
#      - 현재 위치에 서 있기
#      - 빈 칸으로만 이동 가능
#
#  - 벽이 움직인다
#    - 1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려감
#    - 아래에 행이 없다면 벽이 사라짐
#
#  - 캐릭터가 먼저 이동하고, 그 다음 벽이 이동
#  - 벽이 캐릭터가 있는 칸에 이동 시, 캐릭터는 더 이상 이동 불가
#
# [2] 시간 복잡도
#  - 8x8 chess 칸이고, 시뮬레이션이므로 시간 상으로는 문제가 없을 듯 하다
#
#
# @ 설계
#
# [1] 시뮬레이션
#  - (7, 0)에서 시작, (0, 7) 도착
#  - 현재 위치 또는 대각선 8방 움직이기 가능
#
# BFS() 진행 시 고려사항
#  - target이 벽에 있다면 continue
#  - 아니라면, 다시 queue에 넣고 8방향 BFS 진행
#  - 이러면 공간복잡도가 step마다 9배씩
#    --> 매 step마다 visit을 만들어서 방문체크 진행하면 된다


from collections import deque

def move_wall():
    global arr

    arr = [['.']*N] + arr[:-1]
    return

def move_character():
    global q

    curSize = q.__len__()

    for c in range(curSize):
        target = q.popleft()
        if arr[target[0]][target[1]] == '#': continue

        q.append(target)

        for i in range(8):
            nx = target[0] + dx[i]
            ny = target[1] + dy[i]
            if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
            if nx == 0 and ny == 7: return True
            if arr[nx][ny] == '#': continue
            if visit[nx][ny] == True: continue
            visit[nx][ny] = True
            q.append((nx, ny))

    return False

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N = 8

arr = [list(input()) for _ in range(N)]

flag = False

q = deque()

q.append((7, 0)) # (7, 0) 시작

while q:
    visit = [[False]*N for _ in range(N)]
    for i, j in q:
        visit[i][j] = True

    if move_character():
        flag = True
        break

    move_wall()


if flag:
    print(1)
else:
    print(0)
