import sys

input = sys.stdin.readline

n, k, t = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

left = 0
right = len(data) - 1
count = 0

while left < right:
    need = k - data[left]
    if need < data[right]:
        data[right] -= need
        count += need
        left += 1
    elif need > data[right]:
        data[left] += data[right]
        count += data[right]
        right -= 1
    else:
        left += 1
        right -= 1
        count += need

if sum(data) == 0:
    print("YES")
elif count > t:
    print("NO")
elif left == right:
    if data[left] < k:
        print("NO")
    else:
        print("YES")
else:
    print("YES")
