import sys
input = sys.stdin.readline

N = int(input())
requests = sorted(list(map(int, input().split())))
M = int(input())

if sum(requests) <= M:
    result = requests[-1]
else:
    left = 0
    right = int(1e9)
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        for request in requests:
            if request < mid:
                tmp += request
            else:
                tmp += mid
        if tmp > M:
            right = mid - 1
        else:
            left = mid + 1
    result = right
print(result)