import sys

input = sys.stdin.readline

k, n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))

# k, n = 4, 11
# data = [802, 743, 457, 539]

left = 1
right = max(data)

while left <= right:
    center = (left + right) // 2
    cables = sum([(length // center) for length in data])
    if cables >= n:
        answer = center
        left = center + 1
    elif cables < n:
        right = center - 1

print(answer)
