import sys

input = sys.stdin.readline

t, w = map(int, input().strip().split())
data = [int(input().strip()) for x in range(t)]
dp = [[[0] * (w + 1) for _ in range(t)] for _ in range(2)]

if data[0] == 1:
    dp[0][0][0] = 1
else:
    dp[1][0][1] = 1

for i in range(1, t):
    for j in range(w + 1):
        if j % 2:
            # odd
            add = 0
            if data[i] == 2:
                add += 1
            dp[1][i][j] = max(dp[0][i - 1][j - 1], dp[1][i - 1][j]) + add
        else:
            # even
            add = 0
            if data[i] == 1:
                add += 1

            if j == 0:
                dp[0][i][j] += dp[0][i - 1][j] + add
            else:
                dp[0][i][j] += max(dp[0][i - 1][j], dp[1][i - 1][j - 1]) + add

print(max(max(dp[0][-1]), max(dp[1][-1])))
