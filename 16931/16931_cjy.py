import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Z = 0
board = []
for n in range(N):
    board.append(list(map(int, input().split())))
    Z = max(Z, max(board[n]))

result = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for z in range(1, Z + 1):
    for n in range(N):
        for m in range(M):
            if board[n][m] >= z:
                for direction in directions:
                    cur_n, cur_m = n + direction[0], m + direction[1]
                    if cur_n >= 0 and cur_m >= 0 and cur_n < N and cur_m < M:
                        if board[cur_n][cur_m] < z:
                            result += 1
                    elif cur_n < 0 or cur_m < 0 or cur_n >= N or cur_m >= M:
                        result += 1

print(result + 2 * (N * M))