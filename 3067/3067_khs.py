m = int(input())
for _ in range(m):
    a = int(input())
    coins = list(map(int, input().split()))
    n = int(input())
    dp = [0] * (n+1)
    dp[0] = 1
    for c in coins:
        for i in range(c, n+1):
            dp[i] += dp[i - c]
    print(dp[-1])