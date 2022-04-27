import sys
from collections import deque

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline

class dice:
    def __init__(self):
        self.val = 6
        self.left = 4
        self.right = 3
        self.up = 2
        self.down = 5

    def roll(self, d):
        if d == 'left':
            self.right = self.val
            self.val = self.left
            self.left = 7 - self.right

        if d == 'right':
            self.left = self.val
            self.val = self.right
            self.right = 7 - self.left

        if d == 'up':
            self.down = self.val
            self.val = self.up
            self.up = 7 - self.down

        if d == 'down':
            self.up = self.val
            self.val = self.down
            self.down = 7 - self.up


class Sol:
    score = 0
    dir_list = ['right', 'down', 'left', 'up']
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]


    def __init__(self):
        self.N, self.M, self.K = map(int, input().split())
        self.map = []

        for _ in range(self.N):
            temp = list(map(int, input().split()))
            self.map.append(temp)


        d_idx = 0
        x, y = 0, 0
        
        self.Dice = dice()
        
        while self.K:
            self.K -= 1
            x, y, d_idx = self.move(x, y, d_idx)

            self.Dice.roll(self.dir_list[d_idx])
            A = self.Dice.val
            B = self.get_score(x, y)

            d_idx = self.calculate(d_idx, A, B)

        print(self.score)

    def move(self, x, y, di):
        a = x + self.dx[di]
        b = y + self.dy[di]

        if (0 <= a < self.N) and (0 <= b < self.M):
            return a, b, di
        else:
            di = (di + 2)%4
            a = x + self.dx[di]
            b = y + self.dy[di]

            return a, b, di

    def get_score(self, x, y):
        value = self.map[x][y]
        queue = deque([(x, y)])
        visit = [[0]*self.M for _ in range(self.N)]
        visit[x][y] = 1

        C = 0

        while queue:
            temp_queue = deque()
            for _ in range(len(queue)):
                x_1, y_1 = queue.popleft()
                C += 1
                for i in range(4):
                    x_2 = x_1 + self.dx[i]
                    y_2 = y_1 + self.dy[i]

                    if (0 <= x_2 < self.N) and (0 <= y_2 < self.M):
                        if (self.map[x_2][y_2] == value) and visit[x_2][y_2] == 0:
                            temp_queue.append((x_2, y_2))
                            visit[x_2][y_2] = 1

            
            queue = temp_queue
        self.score += value*C

        return value

    def calculate(self, d_idx, A, B):
        di = d_idx

        if A > B:
            di = (di+1)%4
        elif A < B:
            di = (di-1)%4

        return di


if __name__ == '__main__':
    user = Sol()