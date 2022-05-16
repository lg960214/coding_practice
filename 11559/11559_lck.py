from collections import deque
from copy import deepcopy
import sys

sys.stdin = open("testcase.txt", "r")
input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(12)]

directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def bfs(r, c):
    queue = deque([[r, c]])
    color = data[r][c]
    data[r][c] = "."
    poped = 1
    while queue:
        v, u = queue.popleft()
        for direction in directions:
            next_v, next_u = v + direction[0], u + direction[1]
            if next_v < 0 or next_u < 0 or next_v >= 12 or next_u >= len(data[0]):
                continue
            if data[next_v][next_u] == ".":
                continue
            if not data[next_v][next_u] == color:
                continue
            data[next_v][next_u] = "."
            queue.append([next_v, next_u])
            poped += 1
    return poped


def fall():
    for i in range(len(data[0])):
        for j in range(10, -1, -1):
            if not graph[j][i] == ".":
                a = j
                for k in range(j + 1, 12):
                    if graph[k][i] == ".":
                        a = k
                if not a == j:
                    graph[a][i] = graph[j][i]
                    graph[j][i] = "."


answer = 0
last = 0
while True:
    pop = 0
    for i in range(12):
        for j in range(len(graph[0])):
            if not graph[i][j] == ".":
                data = deepcopy(graph)
                poped = bfs(i, j)
                if poped >= 4:
                    pop = 1
                    graph = data
    if pop:
        answer += 1
    else:
        break
    last = answer

    fall()

print(answer)
