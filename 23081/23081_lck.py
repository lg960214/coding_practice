import sys

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data += input().split()

directions = [
    [[1, 0], [-1, 0]],  # 위, 아래
    [[0, 1], [0, -1]],  # 좌, 우
    [[1, 1], [-1, -1]],  # 오른쪽 아래 대각선
    [[1, -1], [-1, 1]],  # 왼쪽 아래 대각선
]


def check(y, x):
    count = 0
    for direction in directions:
        for y_direction, x_direction in direction:
            temp_count = 0
            temp_y, temp_x = y + y_direction, x + x_direction
            while temp_y < n and temp_x < n and temp_y >= 0 and temp_x >= 0:
                if data[temp_y][temp_x] == "W":
                    temp_count += 1
                elif data[temp_y][temp_x] == ".":
                    break
                else:
                    count += temp_count
                    break
                temp_y += y_direction
                temp_x += x_direction
    return count


answer = []
location = []

for Y in range(n - 1, -1, -1):
    for X in range(n - 1, -1, -1):
        if data[Y][X] == ".":
            answer.append(check(Y, X))
            location.append([X, Y])
dictionary = dict(zip(answer, location))

if sum(answer) == 0:
    print("PASS")
else:
    print(*dictionary[max(dictionary)])
    print(max(dictionary))
