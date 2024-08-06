from collections import deque

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Sol:
    dx = [0, -1, 0]
    dy = [-1, 0, 1]
    kill = 0
    ans = -1

    def __init__(self):
        self.N, self.M, self.D = map(int, input().split())

        self.arr = [list(map(int, input().split())) for _ in range(self.N)]

        self.putHunter()

        print(self.ans)

    def putHunter(self):
        self.hunters = []
        self.visit = [False]*self.M

        self.DFS(0, 0)

    def DFS(self, level, now):
        if (level == 3):
            self.kill = 0
            self.GAME()
            return

        for i in range(now, self.M):
            if self.visit[i] == True: continue
            self.visit[i] = True
            self.hunters.append(i)
            self.DFS(level+1, i+1)
            self.hunters.pop()
            self.visit[i] = False

    def GAME(self):
        self.board = []
        for i in range(self.N):
            self.board.append(self.arr[i][:])

        flag = 1

        while flag:
            for i in range(3):
                self.BFS(self.hunters[i])

            self.M_BFS()

            flag = self.countMonster()

        self.ans = max(self.kill, self.ans)

    def BFS(self, start):

        q = deque()

        q.append(Node(self.N, start))

        visit = [[False]*self.M for _ in range(self.N)]

        step = 0
        curSize = 0

        while q:
            if (step == self.D): break

            curSize = q.__len__()

            for c in range(curSize):
                target = q.popleft()
                for i in range(3):
                    nx = target.x + self.dx[i]
                    ny = target.y + self.dy[i]

                    if not ((0 <= nx < self.N) and (0 <= ny < self.M)): continue
                    if self.board[nx][ny] == 1 or self.board[nx][ny] == -1:
                        self.board[nx][ny] = -1
                        return

                    if (visit[nx][ny] == True): continue

                    visit[nx][ny] = True
                    q.append(Node(nx, ny))

            step += 1

        return

    def M_BFS(self):

        for i in range(self.N):
            for j in range(self.M):
                if (self.board[i][j] == -1):
                    self.kill += 1
                    self.board[i][j] = 0

        for i in range(self.N-1, 0, -1):
            for j in range(self.M):
                self.board[i][j] = self.board[i-1][j]

        for j in range(self.M):
            self.board[0][j] = 0

    def countMonster(self):
        cnt = 0

        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == 1:
                    cnt += 1

        return cnt

user = Sol()