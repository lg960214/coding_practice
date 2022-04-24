import sys

input = sys.stdin.readline

h, w = map(int, input().strip().split())
data = [input().strip() for _ in range(h)]

answer = 0
check = 0

for i in range(h):
    for j in range(w):
        if data[i][j] == "/" or data[i][j] == "\\":
            answer += 0.5
            check += 1
        elif check % 2:
            answer += 1

print(int(answer))
