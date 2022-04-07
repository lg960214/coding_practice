import sys

input = sys.stdin.readline

n, s, m = map(int, input().strip().split())
data = list(map(int, input().strip().split()))

dp = [0] * (m + 1)
dp_temp = [0] * (m + 1)
dp[s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[j] == i:
            step = data[i - 1]
            if j - step >= 0:
                dp_temp[j - step] = i + 1
            if j + step <= m:
                dp_temp[j + step] = i + 1
    dp = dp_temp
    dp_temp = [0] * (m + 1)

for x in range(m, -1, -1):
    if dp[x] == n + 1:
        print(x)
        break
else:
    print(-1)
