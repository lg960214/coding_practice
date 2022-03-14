from math import sqrt
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    summation = r1 + r2
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif distance + r1 == r2 or distance + r2 == r1:
        print(1)
    elif distance + r1 < r2 or distance + r2 < r1:
        print(0)
    elif distance == summation:
        print(1)
    elif distance < summation:
        print(2)
    elif distance > summation:
        print(0)
