N, r, c = map(int, input().split())

left, right, up, down = 0, 2 ** N - 1, 0, 2 ** N - 1
cnt = 0
for n in range(N):

    mid = (up + down) // 2
    if mid < r:
        cnt += (2 ** (N-n)) * (2 ** ((N-n) - 1))
        up = mid + 1
    else:
        down = mid

    mid = (left + right) // 2
    if mid < c:
        cnt += (2 ** ((N-n) - 1)) ** 2
        left = mid + 1
    else:
        right = mid

print(cnt)