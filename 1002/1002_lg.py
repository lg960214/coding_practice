import sys
import math

input = sys.stdin.readline

class Sol:
    answer = 0

    def __init__(self):
        self.N = int(input())
        for _ in range(self.N):
            self.x1, self.y1, self.r1, self.x2, self.y2, self.r2 = map(int, input().split())
            self.cal()

    def cal(self):
        d1 = math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
        d2 = self.r1 + self.r2
        d3 = abs(self.r1 - self.r2)
      
        if d1 != 0:
            if (d3 < d1 < d2):
                print(2)
            elif (d1 == d2) or (d3 == d1):
                print(1)
            else:
                print(0)
        else:
            if d3 == 0:
                print(-1)
            else:
                print(0)


if __name__ == '__main__':
    user = Sol()