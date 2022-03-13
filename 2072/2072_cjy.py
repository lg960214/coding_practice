# parameters
PADDING=1
BOARD_SIZE=19+PADDING*2
BLACK=-1
WHITE=1
FLAG=0

# make board
N = int(input())
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# directions
"""
    left_right : (→, ←)
    up_down : (↓, ↑)
    slash : (↗, ↙)
    backslash : (↘, ↖)
"""
left_right = (0, 1)
up_down = (1, 0)
slash = (-1, 1)
backslash = (1, 1)
directions = (left_right, up_down, slash, backslash)


# check function whether out of boundary or not.
def is_boundary(cur_row, cur_col):
    if cur_row < 1 or cur_row > 19 or cur_col < 1 or cur_col > 19:
        return True
    else:
        return False

# game start
for n in range(1, N + 1):
    row, col = map(int, input().split())
    stone = WHITE if n % 2 == 0 else BLACK
    board[row][col] = stone
    start_r = [row, 1, row + min(col - 1, 19 - row), row - min(row - 1, col - 1)]
    start_c = [1, col, col - min(col - 1, 19 - row), col - min(row - 1, col - 1)]
    for i, direction in enumerate(directions):
        cur_row, cur_col = start_r[i], start_c[i]
        count = 0
        tmp = []
        while True:
            if is_boundary(cur_row, cur_col):
                tmp.append(count)
                break
            if board[cur_row][cur_col] == stone:
                count += 1
            else:
                tmp.append(count)
                count = 0
            cur_row += direction[0]
            cur_col += direction[1]
        if 5 in tmp:
            print(n)
            FLAG = 1
            break
    if FLAG:
        break
if not FLAG:
    print(-1)
