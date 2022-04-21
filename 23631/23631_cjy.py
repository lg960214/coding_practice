import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    left = 1
    right = 4474
    while left < right:
        mid = (left + right) // 2
        if mid * (mid + 1) * K >= 2 * N:
            right = mid
        else:
            left = mid + 1
    hopping = left
    last_hopping = N - K * (hopping + 1) * hopping // 2 - 1
    if hopping % 2 != 0:
        x = (hopping // 2 + 1) * K
        print(x + last_hopping, 'R')
    else:
        x = -(hopping // 2) * K
        print(x - last_hopping, 'L')
