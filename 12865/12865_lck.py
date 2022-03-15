import sys

input = sys.stdin.readline

n, k = map(int, input().split())

wv_list = []
for _ in range(n):
    w, v = map(int, input().split())
    wv_list.append((w, v))

dp = [[0 for _ in range(k + 1)] for _ in range(n)]

if k - wv_list[0][0] >= 0:
    dp[0][k - wv_list[0][0]] = max(wv_list[0][1], dp[0][k - wv_list[0][0]])

for i in range(1, n):
    if k - wv_list[i][0] >= 0:
        dp[i][k - wv_list[i][0]] = max(wv_list[i][1], dp[i][k - wv_list[i][0]])
    for j in range(k):
        if dp[i - 1][j] != 0:
            dp[i][j] = max(dp[i - 1][j], dp[i][j])
            if j - wv_list[i][0] >= 0:
                dp[i][j - wv_list[i][0]] = max(
                    wv_list[i][1] + dp[i][j], dp[i][j - wv_list[i][0]]
                )


print(max(dp[n - 1]))
