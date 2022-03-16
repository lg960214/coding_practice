N, K = map(int, input().split())

dp = [0 for i in range(0, K + 1)]
for _ in range(N):
    W, V = map(int, input().split())
    for k in range(K, 0, -1):
        if W <= k:
            dp[k] = max(dp[k], dp[k - W] + V)
print(max(dp))