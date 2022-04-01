import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

answer = 0
for i in range(1, n + 1):
    N = 2 ** (n - i)
    y = r // N
    x = c // N
    answer += (N ** 2) * (y * 2 + x)
    r = r % N
    c = c % N

print(answer)
