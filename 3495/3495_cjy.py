import sys
input = sys.stdin.readline

h, w = map(int, input().split())
board = [input().strip() for _ in range(h)]
result = 0
for row in range(h):
    result += (board[row].count('/') + board[row].count('\\')) // 2
    tmp = []
    while board[row].count('/'):
        tmp.append(board[row].index('/'))
        board[row] = board[row].replace('/', '.', 1)
    while board[row].count('\\'):
        tmp.append(board[row].index('\\'))
        board[row] = board[row].replace('\\', '.', 1)
    tmp.sort()
    for i in range(0, len(tmp), 2):
        result += tmp[i + 1] - tmp[i] - 1

print(result)
