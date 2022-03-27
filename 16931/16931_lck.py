import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

answer = 2 * m * n
answer += sum(data[0]) + sum(data[-1])
for column in data:
    answer += column[0] + column[-1]

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for row in range(n):
    for column in range(m):
        for x, y in directions:
            neighbor_x = row + x
            neighbor_y = column + y
            if (
                neighbor_x < n
                and 0 <= neighbor_x
                and 0 <= neighbor_y
                and neighbor_y < m
            ):
                answer += max(data[row][column] - data[neighbor_x][neighbor_y], 0)

print(answer)
