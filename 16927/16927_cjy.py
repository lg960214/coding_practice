from collections import deque
import sys
sys.stdin = open('testcase.txt', 'r')
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
num_start = min(N, M) // 2 

for start in range(num_start):
    r, c = start, start
    line = deque([arr[r][c]])
    for _ in range(N - 1):
        direction = directions[0]
        r += direction[0]
        c += direction[1]
        line.append(arr[r][c])
    for _ in range(M - 1):
        direction = directions[1]
        r += direction[0]
        c += direction[1]
        line.append(arr[r][c])
    for _ in range(N - 1):
        direction = directions[2]
        r += direction[0]
        c += direction[1]
        line.append(arr[r][c])
    for _ in range(M - 2):
        direction = directions[3]
        r += direction[0]
        c += direction[1]
        line.append(arr[r][c])
    print(line)