from collections import deque

class loc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global arr

    # 1. 변수 초기화
    q = deque()
    visit = [[False]*M for _ in range(N)]

    # 2. 초기값 생성
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 1):
                q.append(loc(i, j))
                visit[i][j] = True

    day = 0
    curSize = 0

    while q:
        curSize = q.__len__()
        for c in range(curSize):
            target = q.popleft()
            for i in range(4):
                nx = target.x + dx[i]
                ny = target.y + dy[i]
                # 탐색 1 : OOB 검사
                if not (0 <= nx < N and 0 <= ny < M): continue
                # 탐색 2 : return 검사 --> 반환 조건이 좌표가 아니므로, 패스
                # 탐색 3 : 제한 조건 검사 --> -1은 벽
                if (arr[nx][ny] == -1): continue
                # 탐색 4 : 방문 검사
                if (visit[nx][ny] == True): continue
                visit[nx][ny] = True
                arr[nx][ny] = 1
                q.append(loc(nx, ny))

        # 탐색해야 하는 값이 있으면 다음날이 오고
        # 아니면 마무리
        if q:
            day += 1
        else:
            break

    # 안 익은 토마토 검사
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 0):
                return -1

    return day


M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = bfs()

print(ans)