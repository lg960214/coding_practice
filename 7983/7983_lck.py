import sys

input = sys.stdin.readline

n = int(input().strip())
data = [list(map(int, input().strip().split())) for _ in range(n)]
data.sort(reverse=True, key=lambda x: x[1])

answer = data[0][1]

for d, t in data:
    answer = min(answer, t) - d

print(answer)
