import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())
    time = list(map(int, input().strip().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().strip().split())
        graph[y].append(x)
    w = int(input().strip())

    dp = [-1] * (n + 1)

    def dfs(x):
        if not graph[x]:
            dp[x] = time[x - 1]
            return dp[x]
        if not dp[x] == -1:
            return dp[x]

        for node in graph[x]:
            dp[x] = max(dfs(node), dp[x])
        dp[x] += time[x - 1]

        return dp[x]

    dfs(w)
    print(dp[w])
