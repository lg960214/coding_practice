import sys
from collections import deque

sys.stdin = open("testcase.txt", "r")
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]


def bfs(start):
    queue = deque([start])
    while queue:
        v, u = queue.popleft()
        if graph[v][u] == 1:
            graph[v][u] = 0
            for x, y in directions:
                next_x = u + x
                next_y = v + y
                if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                    queue.append([next_y,next_x])

answer = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            bfs([i,j])
            answer += 1

print(answer)
