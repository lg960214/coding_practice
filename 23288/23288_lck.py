from collections import deque
import sys

sys.stdin = open("testcase.txt", "r")
input = sys.stdin.readline

n, m, k = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]


class Dice:
    def __init__(self) -> None:
        self.dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]

    def east(self):
        self.dice[1], self.dice[3][1] = [self.dice[3][1], *self.dice[1][:2]], self.dice[1][2]

    def west(self):
        self.dice[1], self.dice[3][1] = [*self.dice[1][1:], self.dice[3][1]], self.dice[1][0]

    def south(self):
        temp = self.dice[3][1]
        for i in range(3, 0, -1):
            self.dice[i][1] = self.dice[i - 1][1]
        self.dice[0][1] = temp

    def north(self):
        temp = self.dice[0][1]
        for i in range(3):
            self.dice[i][1] = self.dice[i + 1][1]
        self.dice[3][1] = temp


def bfs(start, number):
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    queue = deque([start])
    tiles = 1
    while queue:
        y, x = queue.popleft()
        for direction in directions:
            next_y = y + direction[0]
            next_x = x + direction[1]
            if next_y < 0 or next_x < 0 or next_x >= m or next_y >= n:
                continue
            if not graph[next_y][next_x] == number:
                continue
            if visited[next_y][next_x]:
                continue
            visited[next_y][next_x] = True
            queue.append([next_y, next_x])
            tiles += 1
    return tiles


rotation = ["east", "south", "west", "north"]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
rotation_index = 0
dice = Dice()
dice.east()
answer = 0
r, c = 0, 1

for _ in range(k):
    A = dice.dice[-1][1]
    B = graph[r][c]

    answer += bfs([r, c], B) * B

    if A > B:
        rotation_index += 1
    elif A < B:
        rotation_index -= 1
    rotation_index %= 4
    temp_r = r + directions[rotation_index][0]
    temp_c = c + directions[rotation_index][1]
    if temp_r < 0 or temp_r >= n or temp_c < 0 or temp_c >= m:
        rotation_index -= 2

    rotate_direction = rotation[rotation_index]
    if rotate_direction == "east":
        dice.east()
    elif rotate_direction == "west":
        dice.west()
    elif rotate_direction == "north":
        dice.north()
    else:
        dice.south()

    r, c = r + directions[rotation_index][0], c + directions[rotation_index][1]

print(answer)
