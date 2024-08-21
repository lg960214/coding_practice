from collections import deque

dx = [0, 0, 1, 1, -1, -1]
dy = [-2, 2, 1, -1, -1, 1]

def BFS(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy))
    step = 1
    curSize = 0
    while q:
        curSize = q.__len__()
        for c in range(curSize):
            target = q.popleft()

            for i in range(6):
                nx = target[0] + dx[i]
                ny = target[1] + dy[i]

                if nx < 0 or ny < 0 or nx > 2 or ny > 18: continue
                if nx == ex and ny == ey: return step

                q.append((nx, ny))

        step += 1




info_dict = {
    'q': (0, 0), 'w': (0, 2), 'e': (0, 4), 'r': (0, 6), 't': (0, 8), 'y': (0, 10), 'u': (0, 12), 'i': (0, 14), 'o': (0, 16), 'p': (0, 18),
    'a': (1, 1), 's': (1, 3), 'd': (1, 5), 'f': (1, 7), 'g': (1, 9), 'h': (1, 11), 'j': (1, 13), 'k': (1, 15), 'l': (1, 17),
    'z': (2, 2), 'x': (2, 4), 'c': (2, 6), 'v': (2, 8), 'b': (2, 10), 'n': (2, 12), 'm': (2, 14)
}

T = int(input())

for _ in range(T):
    commands = input()
    cnt = 1

    for i in range(1, len(commands)):
        prev = commands[i-1]
        cur = commands[i]

        if prev == cur:
            cnt += 1
            continue

        px, py = info_dict[prev.lower()]
        cx, cy = info_dict[cur.lower()]

        distance = BFS(px, py, cx, cy)
        cnt += (distance*2 + 1)

    print(cnt)