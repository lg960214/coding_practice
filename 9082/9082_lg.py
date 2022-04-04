import math
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    _ = input()
    count = math.ceil(sum(map(int, input().rstrip()))/3)
    print(count)
    _ = input()
