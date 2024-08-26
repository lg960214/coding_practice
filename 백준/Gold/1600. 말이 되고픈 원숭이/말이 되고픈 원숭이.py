# 동작수의 최솟값 = BFS 탐색 시 빠르게 도착하는 경로가 답
from collections import deque


def BFS():
    q = deque()
    visit = [[_init]*M for __ in range(N)]

    q.append((0, 0, 0))
    visit[0][0] = 1

    step = 0
    curSize = 0

    while q:
        curSize = q.__len__()
        for c in range(curSize):
            target = q.popleft()
            for i in range(12):
                nx = target[0] + dx[i]
                ny = target[1] + dy[i]
                if i < 8:
                    nk = target[2] + 1
                else:
                    nk = target[2]

                if 0 > nx or 0 > ny or N <= nx or M <= ny: continue # 범위 초과
                if arr[nx][ny] == 1: continue # 벽
                if visit[nx][ny] == 1<<nk or visit[nx][ny] & (1<<nk)-1: continue # 기존에 이미 효율적인 방식으로 지나감

                if nx == N-1 and ny == M-1: return step + 1 # 종료조건
                visit[nx][ny] = 1<<nk # K 점프 사용기록
                q.append((nx, ny, nk))

        step += 1

    return -1


dx = [-2, -1, 1, 2, 2, 1, -1, -2, 1, 0, -1, 0] # 0~7: 원숭이 경로, 8~11: 일반 경로
dy = [1, 2, 2, 1, -1, -2, -2, -1, 0, 1, 0, -1]

K = int(input())

_init = 1<<K+1

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

if M == 1 and N == 1:
    print(0)
else:
    print(BFS())
