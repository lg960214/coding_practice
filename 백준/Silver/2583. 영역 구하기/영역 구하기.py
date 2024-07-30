import sys
sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())

arr = [[0]*N for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(x, y, t):
    global arr

    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if not ((0 <= x_ < M) and (0 <= y_ < N)): continue
        if (arr[x_][y_] != 0): continue
        arr[x_][y_] = t
        dfs(x_, y_, t)


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

cnt = 0
no = 2 # 색칠할 영역 표시

for i in range(M):
    for j in range(N):
        if (arr[i][j] == 0):
            arr[i][j] = no
            dfs(i, j, no)
            cnt += 1
            no += 1


ans_lst = [0]*(no)
# 0번째, 1번째는 sorting 필요 x
ans_lst[0] = 1e6
ans_lst[1] = 1e6

for i in range(M):
    for j in range(N):
        ans_lst[arr[i][j]] += 1

ans_lst.sort()

print(no-2)
for i in range(no-2):
    print(ans_lst[i], end=' ')