import sys

input = sys.stdin.readline

w, h, f, c, x1, y1, x2, y2 = map(int, input().strip().split())

if f > w // 2:
    f = w - f

width = x2 - x1
double = 0

if x1 < f:
    double = min(f, x2) - x1

width += double
painted = width * (y2 - y1) * (c + 1)

print(w * h - painted)
