import sys
from collections import deque
input = sys.stdin.readline

def init_unions():
    unions = [[0] * N for _ in range(N)] # union lists
    pop_unions = [0] * (N * N  + 1)# population of each union
    n_unions = [0] * (N * N + 1) # the number of nations for each union
    return unions, pop_unions, n_unions

def is_valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N

def can_moving():
    def get_union(sr, sc):
        queue = deque()
        queue.append((sr, sc))
        while queue:
            r, c = queue.popleft()
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if is_valid_coord(nr, nc) and not unions[nr][nc] and L <= abs(nations[r][c] - nations[nr][nc]) <= R:
                    unions[nr][nc] = union
                    pop_unions[union] += nations[nr][nc]
                    n_unions[union] += 1
                    queue.append((nr, nc))
    union = 0 # union id
    for i in range(N):
        for j in range(N):
            if not unions[i][j]:
                union += 1
                unions[i][j] = union
                pop_unions[union] += nations[i][j]
                n_unions[union] += 1
                get_union(i, j)
    if union == N * N:
        return False
    else:
        return True

                

dr = (0, 1, 0, -1)
dc = (-1, 0, 1, 0)

N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
unions, pop_unions, n_unions = init_unions()
day = 0
while can_moving():
    for i in range(N):
        for j in range(N):
            union = unions[i][j]
            if union:
                nations[i][j] = pop_unions[union] // n_unions[union]
    unions, pop_unions, n_unions = init_unions()
    day += 1
print(day)
