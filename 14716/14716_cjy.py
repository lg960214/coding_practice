import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def dfs(r, c, board):
    if r < 0 or r >= M or c < 0 or c >= N:
        return False
    if board[r][c]:
        board[r][c] = 0
        for direction in directions:
            nr = r + direction[0]
            nc = c + direction[1]
            dfs(nr, nc, board)
        return True
    return False

count = 0
for m in range(M):
    for n in range(N):
        if dfs(m, n, board):
            count += 1

print(count)