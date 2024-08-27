
def dfs(step, x, y, sm):
    global max_
    if step >= 3:
        max_ = max(max_, sm)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if global_visit[nx][ny] == True: continue
        global_visit[nx][ny] = True
        dfs(step+1, nx, ny, sm + arr[nx][ny])
        global_visit[nx][ny] = False

def bfs(x, y, sm):
    global max_

    for except_ in range(4):
        temp_sm = sm

        for i in range(4):
            if i == except_: continue
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or N <= nx or M <= ny: break
            temp_sm += arr[nx][ny]
        else:
            max_ = max(max_, temp_sm)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
global_visit = [[False]*M for _ in range(N)]

max_ = -1

for i in range(N):
    for j in range(M):
        global_visit[i][j] = True
        dfs(0, i, j, arr[i][j])
        bfs(i, j, arr[i][j])
        global_visit[i][j] = False

print(max_)