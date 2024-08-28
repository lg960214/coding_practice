# 이하라면 -> 고침


from collections import deque

def BFS(x, y):
    global flag

    q = deque()
    q.append((x, y))

    visited_node = set()
    visited_node.add((x, y))

    while q:
        target = q.popleft()

        for i in range(4):
            nx = target[0] + dx[i]
            ny = target[1] + dy[i]
            if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
            mx = min(target[0], nx)
            my = min(target[1], ny)
            if i < 2:
                if sero[mx][my] == False: continue
                sero[mx][my] = False
                visited_node.add((nx, ny))
                q.append((nx, ny))
            else:
                if garo[mx][my] == False: continue
                garo[mx][my] = False
                visited_node.add((nx, ny))
                q.append((nx, ny))

    if len(visited_node) == 1:
        return

    flag = True

    sm_lst = list(visited_node)
    sm = 0
    for i, j in sm_lst:
        sm += arr[i][j]

    val = int(sm / len(sm_lst))

    for i, j in sm_lst:
        arr[i][j] = val

    return

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, L, R = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))

move = 0
flag = True

garo = [[False] * (N - 1) for _ in range(N)]
sero = [[False] * N for _ in range(N - 1)]

while flag:
    flag = False
    # 1. 선 분리
    for i in range(N):
        for j in range(N):
            if j < N-1: # 가로 따지기
                if L <= abs(arr[i][j] - arr[i][j+1]) <= R:
                    garo[i][j] = True
            if i < N-1: # 세로 따지기
                if L <= abs(arr[i][j] - arr[i+1][j]) <= R:
                    sero[i][j] = True

    # 2. 합치고 분리
    for i in range(N):
        for j in range(N):
            BFS(i, j)

    if flag:
        move += 1
    else:
        break

print(move)
