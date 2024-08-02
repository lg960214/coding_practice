from collections import deque

class loc:
    def __init__(self, z, x, y):
        self.z = z
        self.x = x
        self.y = y

dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]

def bfs():
    global arr

    q = deque()
    visit = [[[False]*M for _ in range(N)] for __ in range(H)]
    
    # z축을 H and k로 상정
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if (arr[k][i][j] == 1):
                    q.append(loc(k, i, j))
                    visit[k][i][j] = True

    day = 0
    curSize = 0

    while q:
        curSize = q.__len__()
        for c in range(curSize):
            target = q.popleft()
            for i in range(6):
                nz = target.z + dz[i]
                nx = target.x + dx[i]
                ny = target.y + dy[i]
                # 탐색 1 : OOB 검사
                if not (0 <= nx < N and 0 <= ny < M and 0 <= nz < H): continue
                # 탐색 2 : return 검사 --> 반환 조건이 좌표가 아니므로, 패스
                # 탐색 3 : 제한 조건 검사 --> -1은 벽
                if (arr[nz][nx][ny] == -1): continue
                # 탐색 4 : 방문 검사
                if (visit[nz][nx][ny] == True): continue
                visit[nz][nx][ny] = True
                arr[nz][nx][ny] = 1
                q.append(loc(nz, nx, ny))

        # 탐색해야 하는 값이 있으면 다음날이 오고
        # 아니면 마무리
        if q:
            day += 1
        else:
            break

    # 안 익은 토마토 검사
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if (arr[k][i][j] == 0):
                    return -1

    return day


M, N, H = map(int, input().split())

arr = []
# 3차원 array 추가 --> 밑단이든 윗단이든 어디서부터 쌓든 결과는 같다
for h in range(H):
    temp_list = [list(map(int, input().split())) for _ in range(N)]
    arr.append(temp_list)

ans = bfs()

print(ans)