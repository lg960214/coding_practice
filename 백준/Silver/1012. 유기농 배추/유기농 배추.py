import sys
from collections import deque

input = sys.stdin.readline


class Sol:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def __init__(self):
        T = int(input())
        for _ in range(T):
            self.M, self.N, self.K = map(int, input().split())

            self.matrix = [[0]*self.M for i in range(self.N)]

            for i in range(self.K):
                x, y = map(int, input().split())
                self.matrix[y][x] = 1

            self.BFS()

    
    def BFS(self):
        visit = [[0]*self.M for i in range(self.N)]
        cnt = 0

        for i in range(self.N):
            for j in range(self.M):
                if (visit[i][j] == 0) and (self.matrix[i][j] == 1):
                    cnt += 1
                    queue = deque([[i, j]])

                    while queue:
                        x, y = queue.popleft()

                        for k in range(4):
                            x_1 = x + self.dx[k]
                            y_1 = y + self.dy[k]
                            if (0 <= x_1 < self.N) and (0 <= y_1 < self.M):
                                if (self.matrix[x_1][y_1] == 1) and (visit[x_1][y_1] == 0):
                                    visit[x_1][y_1] = 1
                                    queue.append([x_1,y_1])

        print(cnt)

if __name__ == '__main__':
    user = Sol()