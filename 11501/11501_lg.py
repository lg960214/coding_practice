import sys


input = sys.stdin.readline

class Sol:
    profit = 0
    buy_list = []

    def __init__(self):
        T = int(input())
        for _ in range(T):
            self.M = int(input())
            self.stock = list(map(int, input().split()))
            max_ = 0

            for i in reversed(range(self.M)):
                value = self.stock[i]

                if value < max_:
                    self.profit += max_ - value
                else:
                    max_ = self.stock[i]

            print(self.profit)
            self.profit = 0

if __name__ == '__main__':
    user = Sol()



