class Sol:
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    def __init__(self):
        N = int(input())

        self.arr = [['.']*6 for _ in range(6)]
        self.arr[2][2] = 'W'
        self.arr[3][3] = 'W'
        self.arr[2][3] = 'B'
        self.arr[3][2] = 'B'

        for i in range(N):
            if (i%2 == 0):
                target = 'B'
            else:
                target = 'W'
            x, y = map(int, input().split())
            x -= 1
            y -= 1

            self.arr[x][y] = target

            for i in range(8):
                flag = self.check(target, x, y, i)
                if (flag):
                    self.reverse(target, x, y, i)

        for i in range(6):
            print("".join(self.arr[i]))

        B = 0
        W = 0
        for i in range(6):
            B += self.arr[i].count('B')
            W += self.arr[i].count('W')
        
        if (B > W):
            print('Black')
        else:
            print('White')

    def reverse(self, target, x, y, di):
        x_ = x
        y_ = y

        while True:
            x_ += self.dx[di]
            y_ += self.dy[di]

            if (self.arr[x_][y_] == target): return
            self.arr[x_][y_] = target


    def check(self, target, x, y, di):
        x_ = x
        y_ = y

        while True:
            x_ += self.dx[di]
            y_ += self.dy[di]

            if not ((0 <= x_ < 6) and (0 <= y_ < 6)): break
            if (self.arr[x_][y_] == '.'): return False
            if (self.arr[x_][y_] == target): return True
        return False

user = Sol()




