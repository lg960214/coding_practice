import sys

n = int(input())

times = []
pays = []

for i in range(0, n):
    t, p = map(int, sys.stdin.readline().split(' '))
    times.append(t)
    pays.append(p)

dp = [0] * n
max_pay = 0

for i in range(n-1, -1, -1):
    if i + times[i] > n:
        dp[i] = max_pay
    elif i + times[i] == n:
        dp[i] = max(pays[i], max_pay)
    else:
        dp[i] = max(pays[i] + dp[times[i] + i], max_pay)

    max_pay = max(max_pay, dp[i])

print(max_pay)