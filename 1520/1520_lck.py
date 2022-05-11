import sys

sys.setrecursionlimit(50000)
input = sys.stdin.readline

m, n = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dp[0][0] = 1

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(r, c):
    if not dp[r][c] == -1:
        return dp[r][c]

    dp[r][c] = 0
    for x, y in directions:
        next_r, next_c = r + x, c + y
        if next_r < 0 or next_c < 0 or next_r >= m or next_c >= n:
            continue
        if data[next_r][next_c] <= data[r][c]:
            continue
        dp[r][c] += dfs(next_r, next_c)
    return dp[r][c]


print(dfs(m - 1, n - 1))
