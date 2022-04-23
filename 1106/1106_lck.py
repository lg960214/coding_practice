import sys

input = sys.stdin.readline

c, n = map(int, input().strip().split())

max_size = c + 101
dp = [10000000000] * max_size
dp[0] = 0

for _ in range(n):
    cost, customer = map(int, input().strip().split())
    for i in range(max_size - customer):
        dp[i + customer] = min(dp[i + customer], dp[i] + cost)

print(min(dp[c:]))
