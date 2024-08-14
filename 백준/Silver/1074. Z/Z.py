def rec(x, y, N, cnt):
    if (N == 2):
        print(cnt + 2*(r-x) + (c-y))
        return

    half = N//2

    if (x <= r < x + half and y <= c < y + half):
        rec(x, y, half, cnt)
    elif (x <= r < x + half and y + half <= c < y + N):
        rec(x, y + half, half, cnt + N**2//4)
    elif (x + half <= r < x + N and y <= c < y + half):
        rec(x + half, y, half, cnt + (N**2)*2//4)
    else:
        rec(x+ half, y+ half, half, cnt + (N**2)*3//4)


N, r, c = map(int, input().split())

N = 1<<N

rec(0, 0, N, 0)


