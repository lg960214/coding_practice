from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().strip().split())
data = [list(input().strip()) for _ in range(R)]

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(s, star):
    visited = [[False] * C for _ in range(R)]
    if star:
        for r, c in star:
            visited[r][c] = True
    data[s[0]][s[1]] = 0
    next_star_queue = star
    next_s_queue = deque([s])
    while next_s_queue:

        star_queue = next_star_queue
        s_queue = next_s_queue
        next_s_queue = deque([])
        next_star_queue = deque([])
        while star_queue:
            r, c = star_queue.popleft()
            for x, y in directions:
                next_r = r + x
                next_c = c + y
                if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
                    continue
                if data[next_r][next_c] == "D" or data[next_r][next_c] == "X":
                    continue
                if visited[next_r][next_c]:
                    continue
                visited[next_r][next_c] = True
                next_star_queue.append([next_r, next_c])
        while s_queue:
            r, c = s_queue.popleft()
            for x, y in directions:
                next_r = r + x
                next_c = c + y
                if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
                    continue
                if data[next_r][next_c] == "D":
                    return data[r][c] + 1
                if (
                    visited[next_r][next_c]
                    or type(data[next_r][next_c]) == int
                    or data[next_r][next_c] == "X"
                ):
                    continue
                data[next_r][next_c] = data[r][c] + 1
                next_s_queue.append([next_r, next_c])


stars = deque([])
for r in range(R):
    for c in range(C):
        if data[r][c] == "*":
            stars.append([r, c])
        elif data[r][c] == "S":
            s_r, s_c = r, c

answer = bfs([s_r, s_c], stars)
if answer:
    print(answer)
else:
    print("KAKTUS")
