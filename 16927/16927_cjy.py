from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
num_start = min(N, M) // 2 
lines = deque([])
for i in range(num_start):
    r, c = i, i
    line = deque([arr[r][c]])
    for _ in range(N - 1 - (i * 2)):
        direction = directions[0]
        r += direction[0]
        c += direction[1]
        line.append(arr[r][c])
    for _ in range(M - 1 - (i * 2)):
        direction = directions[1]
        r += direction[0]
        c += direction[1]
        line.append(arr[r][c])
    for _ in range(N - 1 - (i * 2)):
        direction = directions[2]
        r += direction[0]
        c += direction[1]
        line.append(arr[r][c])
    for _ in range(M - 2 - (i * 2)):
        direction = directions[3]
        r += direction[0]
        c += direction[1]
        line.append(arr[r][c])
    line.rotate(R % len(line))
    lines.append(line)

for i in range(num_start):
    line = lines.popleft()
    r, c = i, i
    arr[r][c] = line.popleft()
    for _ in range(N - 1 - (i * 2)):
        direction = directions[0]
        r += direction[0]
        c += direction[1]
        arr[r][c] = line.popleft()
    for _ in range(M - 1 - (i * 2)):
        direction = directions[1]
        r += direction[0]
        c += direction[1]
        arr[r][c] = line.popleft()
    for _ in range(N - 1 - (i * 2)):
        direction = directions[2]
        r += direction[0]
        c += direction[1]
        arr[r][c] = line.popleft()
    for _ in range(M - 2 - (i * 2)):
        direction = directions[3]
        r += direction[0]
        c += direction[1]
        arr[r][c] = line.popleft()
for i in range(N):
    print(*arr[i])
