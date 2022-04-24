from math import floor, sqrt
import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())

    times = (-1 + sqrt(1 + 8 * (n - 1) / k)) / 2
    times_floor = floor(times)
    remainder = (n - 1) - k * (times_floor + 1) * times_floor // 2
    temp = (times_floor + 1) // 2 * k

    if not times_floor % 2:
        # even
        temp = -temp
        last_distance = remainder + temp
    else:
        # odd
        last_distance = temp - remainder

    if times_floor % 2:
        print(last_distance, "L")
    else:
        print(last_distance, "R")
