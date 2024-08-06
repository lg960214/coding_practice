from collections import deque
from copy import deepcopy
dir = ((0,-1), (-1,0), (0,1)) #좌, 상, 우 순으로 탐색(먼저 발견한게 가장 왼쪽이 됨)

def bfs(r,c): #round r이면 r = R-r이 됨. 즉 라운드 r이면 arr의 0~R-r행만 사용
    global kill
    dq = deque()
    used = [[0]*C for _ in range(r)]
    used[r-1][c] = 1
    dq.append((r-1,c))
    while dq:
        cr, cc = dq.popleft()
        if arr2[cr][cc] == 1: #1만나면 kill에 좌표 추가함(가장 가까우면서 가장 왼쪽이 됨)
            if used[cr][cc] <= D: #사거리보다 작으면 추가, 아니면 이번라운드에 킬 못함
                kill.add((cr,cc))
            return
        for dr, dc in dir:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<r and 0<=nc<C and used[nr][nc] == 0:
                used[nr][nc] = used[cr][cc] + 1
                dq.append((nr,nc))

T = 1
for tc in range(1, T+1):
    R, C, D = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(R)]
    mx = 0
    for a1 in range(0, C-2): #archery
        for a2 in range(a1+1, C-1):
            for a3 in range(a2+1, C):
                arr2 = [deepcopy(lst) for lst in arr] #arr 복사해서 이번 궁수 스쿼드에 사용
                kills = 0 #이번 궁수 스쿼드의 총 킬수
                for r in range(R): #round r = 0이 처음 R-1이 마지막
                    kill = set() #이번 라운드에 bfs를 돌며 죽인 적의 좌표 (중복으로 죽여도 set이라 겹치지 않음)
                    for archery in (a1,a2,a3):
                        bfs(R-r, archery) #bfs를 돌며 kill에 좌표를 추가함
                    for r1, c1 in kill: #kill 좌표 빼서 arr2에 죽인 적을 0으로 바꿈
                        arr2[r1][c1] = 0
                    kills += len(kill) #이번라운드 킬수 추가
                mx = max(mx, kills)
    print(mx)