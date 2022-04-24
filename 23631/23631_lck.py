from math import floor, sqrt
import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())

    times = (-1 + sqrt(1 + 8 * (n - 1) / k)) / 2
    times_floor = floor(times)
    remainder = (n - 1) - k * (times_floor + 1) * times_floor // 2
    last_location = (times_floor + 1) // 2 * k

    if not times_floor % 2:
        # even
        last_distance = remainder - last_location
        print(last_distance, "R")
    else:
        # odd
        last_distance = last_location - remainder
        print(last_distance, "L")
