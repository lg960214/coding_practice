from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

global_visit = [[False]*M for i in range(N)]

q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            q.append((i, j))
            global_visit[i][j] = True

step = 0
curSize = 0

while q:
    curSize = q.__len__()

    for c in range(curSize):
        target = q.popleft()
        cnt = 0
        for i in range(4):
            nx = target[0] + dx[i]
            ny = target[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if arr[nx][ny] == 'X':
                cnt += 1

        if cnt < 2:
            global_visit[target[0]][target[1]] = False


max_x = -1
min_x = 100
max_y = -1
min_y = 100

for i in range(N):
    for j in range(M):
        if global_visit[i][j] == True:
            max_x = max(max_x, i)
            min_x = min(min_x, i)

            max_y = max(max_y, j)
            min_y = min(min_y, j)
        elif global_visit[i][j] == False:
            arr[i][j] = '.'

for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        print(arr[i][j], end='')
    print()