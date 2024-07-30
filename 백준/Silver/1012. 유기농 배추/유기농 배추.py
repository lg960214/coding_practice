import sys
sys.setrecursionlimit(10**4)

# 상, 하, 좌, 우
di_lst = [1, -1, 0, 0]
dj_lst = [0, 0, -1, 1]

def dfs(i, j):
    land[i][j] = 0

    for di, dj in zip(di_lst, dj_lst):
        x = i + di
        y = j + dj
        if not (0 <= x < N and 0 <= y < M):
            continue
        if land[x][y] == 1:
            dfs(x, y)
    else:
        return 1

T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())
    land = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        land[Y][X] = 1
    summ = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] != 1:
                continue
            summ += dfs(i, j)
    print(summ)