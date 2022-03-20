import sys
input = sys.stdin.readline

def solve(b, x, y):
    result_cnt, result_x, result_y = 0, 0, 0
    li = [[1, 0], [0, 1], [1, 1],
          [-1, 0], [0, -1], [-1, -1],
          [1, -1], [-1, 1]]

    for i, j in li:
        xt, yt = x + i, y + j
        cnt = 0

        while b[xt][yt] == "W":
            xt += i
            yt += j
            cnt += 1
        if b[xt][yt] == "B" and (xt != 0 and xt != len(board[0])-1 and yt != 0 and yt != len(board[0])-1):
            result_cnt += cnt

    return result_cnt, x, y


N = int(input())

board = ["".join(["."] * (N + 2))]
for _ in range(N):
    board.append("." + input() + ".")
board.append("".join(["."] * (N + 2)))

result, X, Y = 0, 0, 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if board[i][j] == ".":
            t, xx, yy = solve(board, i, j)
            if t > result:
                result = t
                X = xx
                Y = yy

if result == 0:
    print("PASS")
else:
    print(Y-1, X-1)
    print(result)
