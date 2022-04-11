import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**7)

class Sol:
    matrix = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    count = 0

    def __init__(self):
        self.M, self.N = map(int, input().split())
        self.visit = [[0]*self.N for _ in range(self.M)]

        for _ in range(self.M):
            temp = list(map(int, input().split()))
            self.matrix.append(temp)
        

        for i in range(self.M):
            for j in range(self.N):
                target = self.matrix[i][j]

                if (target == 1) and (self.visit[i][j] == 0):
                    self.DFS(i, j)

        print(self.count)

    def DFS(self, i, j, visit=0):
        if visit == 0:
            visit += 1
            self.count += 1

        x = i
        y = j
        self.visit[x][y] = 1

        for dx, dy in zip(self.dx, self.dy):
            if (0 <= x+dx < self.M) and (0 <= y+dy < self.N):
                if (self.matrix[x+dx][y+dy] == 1) and (self.visit[x+dx][y+dy] == 0):
                    self.DFS(x+dx, y+dy, visit)

            

        
        


if __name__ == '__main__':
    user = Sol()