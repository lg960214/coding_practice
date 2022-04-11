import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][S] = 1
for n in range(1, N + 1):
    for m in range(M + 1):
        if dp[n - 1][m]:
            if m - V[n - 1] >= 0:
                dp[n][m - V[n - 1]] = 1
            if m + V[n - 1] <= M:
                dp[n][m + V[n - 1]] = 1
if sum(dp[N]):
    print(M - dp[N][::-1].index(1))
else:
    print(-1)
