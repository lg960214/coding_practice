class Sol:
    S = 101
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    length = 0

    def __init__(self):
        self.arr = [[0]*self.S for _ in range(self.S)]

        N = int(input())

        for _ in range(N):
            temp = list(map(int, input().split()))

            for i in range(10):
                for j in range(10):
                    self.arr[temp[0]+i][temp[1]+j] = 1

        for i in range(0, self.S):
            for j in range(0, self.S):
                for c in range(4):
                    x_ = i + self.dx[c]
                    y_ = j + self.dy[c]
                    if not ((0 <= x_ < self.S) and (0 <= y_ < self.S)): continue
                    if (self.arr[i][j] != self.arr[x_][y_]):
                        self.length += 1

        self.length /= 2

        print(int(self.length))

user = Sol()