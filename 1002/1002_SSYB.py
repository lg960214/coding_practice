import math
import sys
input = sys.stdin.readline

N = int(input())
answer = []

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        answer.append(-1)
    elif d == r1 + r2 or max(r1, r2) == min(r1, r2) + d:
        answer.append(1)
    elif max(r1, r2) - min(r1, r2) < d < (r1 + r2):
        answer.append(2)
    else:
        answer.append(0)

for a in answer:
    print(a)