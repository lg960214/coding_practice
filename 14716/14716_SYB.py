import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solve(_x, _y):
    dfs = [[1, 0], [-1, 0],
           [0, 1], [0, -1],
           [1, 1], [-1, -1],
           [-1, 1], [1, -1]]

    for w in dfs:
        if board[_y + w[1]][_x + w[0]] == 1:
            board[_y + w[1]][_x + w[0]] = 0
            solve(_x + w[0], _y + w[1])


M, N = map(int, input().split())
board = [[0 for _ in range(N + 2)]]
for _ in range(M):
    board.append([0] + list(map(int, input().split())) + [0])
board.append([0 for _ in range(N + 2)])

cnt = 0
for y in range(1, M+1):
    for x in range(1, N+1):

        if board[y][x] == 1:
            board[y][x] = 0
            solve(x, y)
            cnt += 1

print(cnt)