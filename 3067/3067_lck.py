import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))
    target = int(input().strip())

    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], target+1):
            dp[j] += dp[j-coins[i]]

    print(dp[-1])
