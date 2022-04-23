import sys
input = sys.stdin.readline
CMAX = 100 * 1000 + 1
C, N = map(int, input().split())
info = [[0, 0]]
for _ in range(N):
    cost, customer = map(int, input().split())
    info.append([cost, customer])

memo = [0] * CMAX
result = CMAX
for n in range(1, N + 1):
    for c in range(info[n][0], CMAX):
        memo[c] = max(memo[c], info[n][1] + memo[c - info[n][0]])
        if memo[c] >= C:
            result = min(result, c)
print(result)
