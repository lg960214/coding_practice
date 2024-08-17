from collections import deque

class Node:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

def Find(now):
    if (now == parents[now]): return now

    parents[now] = Find(parents[now])
    return parents[now]

def Union(a, b):
    ra = Find(a)
    rb = Find(b)

    if (ra == rb): return

    parents[max(ra, rb)] = min(ra, rb)

def check_and_merge():
    global day, country, ufq, flag

    while ufq:
        target = ufq.popleft()

        for i in range(4):
            nx = target.x + dx[i]
            ny = target.y + dy[i]

            if nx <= 0 or ny <= 0 or nx > N or ny > N or arr[nx][ny] == 0: continue
            if arr[nx][ny] == target.n or Find(target.n) == Find(arr[nx][ny]): continue

            country += 1
            Union(target.n, arr[nx][ny])

    if country == K:
        print(day)
        flag = True
        return


def BFS():
    global day, q, ufq

    while q:
        curSize = q.__len__()

        for c in range(curSize):
            target = q.popleft()

            for i in range(4):
                nx = target.x + dx[i]
                ny = target.y + dy[i]

                if nx <=0 or ny <= 0 or nx > N or ny > N: continue

                if arr[nx][ny] == 0:
                    arr[nx][ny] = target.n
                    q.append(Node(nx, ny, target.n))
                    ufq.append(Node(nx, ny, target.n))

        day += 1

        check_and_merge()

        if flag: return



dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, K = map(int, input().split())

day = 0
flag = False
q = deque()
ufq = deque()
country = 1

arr = [[0]*(N+1) for _ in range(N+1)]

parents = [i for i in range(K+1)]

for i in range(1, K+1):
    r, c = map(int, input().split())
    ufq.append(Node(r, c, i))
    q.append(Node(r, c, i))
    arr[r][c] = i

check_and_merge()

if flag == False:
    BFS()