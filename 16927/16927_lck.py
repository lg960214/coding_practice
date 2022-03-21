import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

mini = min(m, n)
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def get_arr():
    y, x = 0, 0
    y_limit, x_limit = n - 1, m - 1
    start_y, start_x = 0, 0
    i = 0
    j = 0
    count = 0
    answer = [[0 for _ in range(m)] for _ in range(n)]
    arr = [[] for _ in range(mini // 2)]
    while count < n * m:
        limits = [[y_limit - j, j], [y_limit - j, x_limit - j], [j, x_limit - j]]

        y_direction = directions[i][0]
        x_direction = directions[i][1]

        next_y, next_x = y + y_direction, x + x_direction
        arr[j].append(data[y][x])
        y, x = next_y, next_x
        count += 1
        if start_x == next_x and start_y == next_y:
            y = start_y + 1
            x = start_x + 1
            start_y = y
            start_x = x
            i = 0
            j += 1
        elif [next_y, next_x] in limits:
            i += 1
            continue
    return arr


arr = get_arr()
answer = [[0 for _ in range(m)] for _ in range(n)]


def rotate():
    y, x = 0, 0
    y_limit, x_limit = n - 1, m - 1
    start_y, start_x = 0, 0
    i = 0
    j = 0
    count = 0
    count_local = 0
    answer = [[0 for _ in range(m)] for _ in range(n)]
    while count < n * m:
        limits = [[y_limit - j, j], [y_limit - j, x_limit - j], [j, x_limit - j]]

        y_direction = directions[i][0]
        x_direction = directions[i][1]

        next_y, next_x = y + y_direction, x + x_direction

        answer[next_y][next_x] = arr[j][(count_local - r + 1) % len(arr[j])]
        y, x = next_y, next_x
        count += 1
        count_local += 1
        if start_x == next_x and start_y == next_y:
            y = start_y + 1
            x = start_x + 1
            start_y = y
            start_x = x
            i = 0
            j += 1
            count_local = 0
        elif [next_y, next_x] in limits:
            i += 1
            continue
    return answer


answer = rotate()
for i in range(n):
    print(*answer[i])
