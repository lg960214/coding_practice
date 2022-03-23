import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))


def bfs(data, start, times):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        distance = data[v]
        for x in range(v + 1, min(n, v + distance + 1)):
            if times[x] == 0 or (times[x] > times[v] + 1):
                times[x] = times[v] + 1
                queue.append(x)


times = [0 for _ in range(n)]

bfs(data, 0, times)

if n == 1:
    print(0)
elif times[-1] == 0:
    print(-1)
else:
    print(times[-1])
