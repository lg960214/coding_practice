from collections import deque

def micro_diffuse():

    visit = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt = 0
                quantity = arr[i][j] // 5

                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 > nx or 0 > ny or N <= nx or M <= ny: continue
                    if arr[nx][ny] == -1: continue
                    cnt += 1
                    visit[nx][ny] += quantity

                visit[i][j] += arr[i][j] - quantity*cnt



    # 동시에 병합
    for i in range(N):
        for j in range(M):
            if arr[i][j] == -1: continue
            arr[i][j] = visit[i][j]


def on_air():

    # g1 : 위쪽
    for i in range(g1-1, 0, -1):
        arr[i][0] = arr[i-1][0]

    for j in range(0, M-1):
        arr[0][j] = arr[0][j+1]

    for i in range(0, g1):
        arr[i][M-1] = arr[i+1][M-1]

    for j in range(M-1, 1, -1):
        arr[g1][j] = arr[g1][j-1]
    else:
        arr[g1][j-1] = 0

    # g2 : 아래쪽
    for i in range(g2+1, N-1):
        arr[i][0] = arr[i+1][0]

    for j in range(0, M-1):
        arr[N-1][j] = arr[N-1][j+1]

    for i in range(N-1, g2, -1):
        arr[i][M-1] = arr[i-1][M-1]

    for j in range(M-1, 1, -1):
        arr[g2][j] = arr[g2][j-1]
    else:
        arr[g2][j-1] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

g1 = -1
g2 = -1
# 공기청정기 위치 파악
for i in range(2, N-2):
    if arr[i][0] == -1:
        g1 = i
        g2 = i+1
        break


for t in range(T):
    # 1. 미세먼지가 확산 - 동시에 일어남
    micro_diffuse()

    # 2. 공기청정기 작동
    on_air()


sm = 2

for i in range(N):
    sm += sum(arr[i])

print(sm)