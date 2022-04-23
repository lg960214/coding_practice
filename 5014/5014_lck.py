from collections import deque


f, s, g, u, d = map(int, input().strip().split())
data = [1] * f


def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        next_floor = [v + u, v - d]
        for floor in next_floor:
            if floor >= f or floor < 0:
                continue
            if data[floor] <= data[v] + 1 and not data[floor] == 1:
                continue
            if floor == s - 1:
                continue
            data[floor] = data[v] + 1
            queue.append(floor)


if s == g:
    print(0)
else:
    bfs(s - 1)
    answer = data[g - 1] - 1
    if answer == 0:
        print("use the stairs")
    else:
        print(answer)
