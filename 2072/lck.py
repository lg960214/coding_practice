def dfs(x, y, a, b, rock):
    global count
    if [x + a, y + b] in rock:
        count += 1
        dfs(x + a, y + b, a, b, rock)


directions = [
    [[1, 1], [-1, -1]],
    [[1, 0], [-1, 0]],
    [[1, -1], [-1, 1]],
    [[0, -1], [0, 1]],
]

n = int(input())
white = []
black = []
answer = -1
for i in range(n):
    if i % 2 == 0:  # black
        black.append(list(map(int, input().split())))
        x, y = black[-1]
        for direction in directions:
            count = 1
            for direc in direction:
                a, b = direc
                dfs(x, y, a, b, black)
            if count == 5:
                if answer == -1:
                    answer = i + 1

    else:  # white
        white.append(list(map(int, input().split())))
        x, y = white[-1]
        for direction in directions:
            count = 1
            for direc in direction:
                a, b = direc
                dfs(x, y, a, b, white)
            if count == 5:
                if answer == -1:
                    answer = i + 1

print(answer)
