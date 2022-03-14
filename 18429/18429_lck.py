import sys
from itertools import permutations

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

answer = 0

candidates = permutations(range(n), n)

for candidate in candidates:
    weight = 500
    for i, day in enumerate(candidate):
        weight += data[day] - k
        if weight < 500:
            break
    else:
        answer += 1

print(answer)
