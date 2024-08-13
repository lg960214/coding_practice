from collections import deque

class loc:
    def __init__(self, x, y):
        self.x = x
        self.y = y


dx = [1, 0, 1]
dy = [0, 1, 1]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dp = [[0] * M for _ in range(N)]
visit = [[False] * M for _ in range(N)]

dp[0][0] = arr[0][0]
visit[0][0] = True
q.append(loc(0, 0))

while q:
    target = q.popleft()

    for i in range(3):
        nx = target.x + dx[i]
        ny = target.y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M): continue
        next_candy = arr[nx][ny] + dp[target.x][target.y]
        if (next_candy <= dp[nx][ny] and visit[nx][ny] == True): continue
        visit[nx][ny] = True
        dp[nx][ny] = next_candy
        q.append(loc(nx, ny))

print(dp[N-1][M-1])



