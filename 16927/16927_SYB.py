import sys
input = sys.stdin.readline

def check(_c, n, m):
    if _c <= n-1:
        return _c, 0
    elif _c <= n+m-2:
        return n-1, _c - n + 1
    elif _c <= 2*n + m - 3:
        return 2*n + m - 3 - _c, m-1
    else:
        return 0, 2*n + 2*m - 4 - _c


def move(_x, _y, _x0, _y0, _xn, _yn):

    if _x0 <= _x <_xn and _y == _y0:
        return _x + 1, _y
    elif _x == _xn and _y0 <= _y < _yn:
        return _x, _y+1
    elif _x0 < _x <= _xn and _y == _yn:
        return _x - 1, _y
    elif _x == _x0 and _y0 < _y <= _yn:
        return _x, _y - 1


N, M, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

index_board = [[[y, x] for x in range(M)] for y in range(N)]
answer = [[[0, 0] for x in range(M)] for y in range(N)]

x0, xm, y0, yn = 0, M-1, 0, N-1
while xm - x0 != -1 and yn - y0 != -1:
    c = R % (2 * (xm - x0 + 1) + 2 * (yn - y0 + 1) - 4)
    x_, y_ = check(c, (xm - x0 + 1), (yn - y0 + 1))
    x_ += x0
    y_ += y0

    t = board[y0][x0]
    for x in range(x0, xm):
        answer[y0][x] = index_board[y_][x_]
        x_, y_ = move(x_, y_, x0, y0, xm, yn)
    for y in range(y0, yn):
        answer[y][xm] = index_board[y_][x_]
        x_, y_ = move(x_, y_, x0, y0, xm, yn)
    for x in range(xm, x0, -1):
        answer[yn][x] = index_board[y_][x_]
        x_, y_ = move(x_, y_, x0, y0, xm, yn)
    for y in range(yn, y0, -1):
        answer[y][x0] = index_board[y_][x_]
        x_, y_ = move(x_, y_, x0, y0, xm, yn)

    x0 += 1
    y0 += 1
    yn -= 1
    xm -= 1

for b in answer:
    for y, x in b:
        print(board[y][x], end=" ")
    print("")