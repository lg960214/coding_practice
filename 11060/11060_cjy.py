import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
maze = list(map(int, input().split()))

queue = deque([[0, maze[0]]]) # index, value(jump)
counts = [-1] * N
counts[0] = 0

while queue:
    tmp = queue.popleft()
    idx, jump = tmp[0], tmp[1]
    for i in range(1, jump + 1):
        j = idx + i
        if j < N and counts[j] == -1:
            queue.append([j, maze[j]])
            counts[j] = counts[idx] + 1
print(counts[N - 1])
