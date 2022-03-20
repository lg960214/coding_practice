import sys
input = sys.stdin.readline

n = int(input())
board = [[i for i in input().strip()] for _ in range(n)]
directions = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1))

# check function whether out of boundary or not.
def is_boundary(cur_x, cur_y):
    if cur_y < 0 or cur_y > n - 1 or cur_x < 0 or cur_x > n - 1:
        return True
    else:
        return False

def is_valid(x, y):
    for dx, dy in directions:
        if not is_boundary(y + dy, x + dx) and board[y + dy][x + dx] == 'W':
            return True
    return False

max_profit = 0
for y in reversed(range(n)):
    for x in reversed(range(n)):
        if board[y][x] == '.' and is_valid(x, y):
            profit = 0
            for direction in directions:
                cur_x, cur_y = x + direction[0], y + direction[1]
                count = 0
                while True:
                    if is_boundary(cur_y, cur_x):
                        count = 0
                        break
                    if board[cur_y][cur_x] == 'W':
                        count += 1
                    elif board[cur_y][cur_x] == 'B':
                        break
                    else:
                        count = 0
                        break
                    cur_x += direction[0]
                    cur_y += direction[1]
                profit += count
            if max_profit <= profit:
                max_profit = profit
                result = f'{x} {y}'
if max_profit:
    print(result)
    print(max_profit)
else:
    print('PASS')