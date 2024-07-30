import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(cur_x, cur_y):
    global visit
    visit[cur_x][cur_y] = True

    for i in range(4):
        x_ = cur_x + dx[i]
        y_ = cur_y + dy[i]
        if not ((0 <= x_ < N) and (0 <= y_ < M)): continue
        if visit[x_][y_] == True: continue
        if (arr[x_][y_] == 0): continue
        dfs(x_, y_)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
ans_lst = []

for t in range(1, T+1):
    M, N, K = map(int, input().split())

    arr = [[0]*M for _ in range(N)]
    visit = [[False]*M for _ in range(N)]

    for _ in range(K):
        ty, tx = map(int, input().split())
        arr[tx][ty] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 1 and visit[i][j] == False):
                dfs(i, j)
                cnt += 1

    ans_lst.append(cnt)

for i in ans_lst:
    print(i)