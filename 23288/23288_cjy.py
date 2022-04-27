import sys
from collections import deque
input = sys.stdin.readline

# right, down, left, up
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

class Dice:
    def __init__(self):
        self.top = 1
        self.bottom = 6
        self.north = 2
        self.south = 5
        self.east = 3
        self.west = 4
    
    def roll(self, direction):
        if direction == [0, 1]: # right
            self.top, self.bottom, self.north, self.south, self.east, self.west = \
            self.west, self.east, self.north, self.south, self.top, self.bottom
        elif direction == [1, 0]: # down
            self.top, self.bottom, self.north, self.south, self.east, self.west = \
            self.north, self.south, self.bottom, self.top, self.east, self.west
        elif direction == [0, -1]: # left
            self.top, self.bottom, self.north, self.south, self.east, self.west = \
            self.east, self.west, self.north, self.south, self.bottom, self.top
        elif direction == [-1, 0]: # up
            self.top, self.bottom, self.north, self.south, self.east, self.west = \
            self.south, self.north, self.top, self.bottom, self.east, self.west

def get_direction(origin, A, B):
    if A > B:
        return directions[(directions.index(origin) + 1) % 4]
    elif A < B:
        return directions[(directions.index(origin) - 1) % 4]
    else:
        return origin

def is_boundary(r, c):
    if 0 < r < N + 1 and 0 < c < M + 1:
        return True
    return False

def get_score(r, c):
    n = 1
    score = score_map[r][c]
    queue = deque()
    queue.append((r, c))
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    while queue:
        r, c = queue.popleft()
        visited[r][c] = True
        for i in range(4):
            nr, nc = r + directions[i][0], c + directions[i][1]
            if not is_boundary(nr, nc):
                continue
            if score_map[nr][nc] == score and not visited[nr][nc]:
                n += 1
                queue.append((nr, nc))
                visited[nr][nc] = True
    return n * score

N, M, K = map(int, input().split())

# init score_map with padding
score_map = [[0] * (M + 2)]
for n in range(1, N + 1):
    tmp = [0]
    tmp.extend(list(map(int, input().split())))
    tmp.extend([0])
    score_map.append(tmp)
score_map.append([0] * (M + 2))

dice = Dice()
moving = [0, 1]
dice_loc = [1, 1]
score = 0
for _ in range(K):
    if not is_boundary(dice_loc[0] + moving[0] , dice_loc[1] + moving[1]):
        moving = get_direction(get_direction(moving, 1, 0), 1, 0) # rotate clockwise twice = reverse
    dice.roll(moving)
    dice_loc[0] += moving[0]
    dice_loc[1] += moving[1]
    score += get_score(*dice_loc)
    A, B = dice.bottom, score_map[dice_loc[0]][dice_loc[1]]
    moving = get_direction(moving, A, B)
print(score)
