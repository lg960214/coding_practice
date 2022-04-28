import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().strip().split())
heights = list(map(int, input().strip().split()))

graph = [set([]) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    if heights[a - 1] > heights[b - 1]:
        graph[b].add(a)
    elif heights[a - 1] < heights[b - 1]:
        graph[a].add(b)


def rec(x):
    if not graph[x]:
        dp[x] = 1
        return 1
    if dp[x]:
        return dp[x]

    maximum = 1
    for node in graph[x]:
        maximum = max(maximum, rec(node) + 1)
    dp[x] = maximum
    return dp[x]


dp = [0] * (n + 1)
for i in range(1, n + 1):
    rec(i)
    print(dp[i])
